DB_USER="cprojean"
DB_NAME="piscineds"
CUSTOMER_CSV_DIR="/mnt/data/customer"
ITEMS_CSV="/mnt/data/item/item.csv"

echo "Creating customers table..."
psql -U "$DB_USER" -d "$DB_NAME" -c "
CREATE UNLOGGED TABLE IF NOT EXISTS customers (
    event_time TIMESTAMPTZ,
    event_type VARCHAR(50),
    product_id INT,
    price NUMERIC(10, 2),
    user_id BIGINT,
    user_session UUID
);"

echo "Loading data from $CUSTOMER_CSV_DIR..."
for file in "$CUSTOMER_CSV_DIR"/*.csv; do
    table_name=$(basename "$file" .csv)
    
    echo "Processing $table_name..."
    
    psql -U "$DB_USER" -d "$DB_NAME" -c "
        CREATE TABLE IF NOT EXISTS $table_name (
            event_time TIMESTAMPTZ,
            event_type VARCHAR(50),
            product_id INT,
            price NUMERIC(10, 2),
            user_id BIGINT,
            user_session UUID
        );

        COPY $table_name FROM '$file' WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');

        INSERT INTO customers SELECT * FROM $table_name;

        DROP TABLE $table_name;
    "
done

echo "Removing duplicates..."
psql -U "$DB_USER" -d "$DB_NAME" -c "
    CREATE UNLOGGED TABLE customers_cleaned AS
    WITH calculated_lag AS (
        SELECT
            *,
            LAG(event_time) OVER (
                PARTITION BY event_type, product_id, price, user_id, user_session
                ORDER BY event_time
            ) as prev_event_time
        FROM customers
    )
    SELECT event_time, event_type, product_id, price, user_id, user_session
    FROM calculated_lag
    WHERE prev_event_time IS NULL
       OR event_time - prev_event_time > interval '1 second';

    DROP TABLE customers;
    ALTER TABLE customers_cleaned RENAME TO customers;
"

echo "Importing items..."
psql -U "$DB_USER" -d "$DB_NAME" -c "
    CREATE TABLE IF NOT EXISTS items (
        product_id INT,
        category_id BIGINT,
        category_code VARCHAR(50),
        brand VARCHAR(50)
    );
    
    COPY items (product_id, category_id, category_code, brand)
    FROM '$ITEMS_CSV'
    WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');
"

echo "Merging final data..."
psql -U "$DB_USER" -d "$DB_NAME" -c "
    CREATE UNLOGGED TABLE customers_merged AS
    SELECT
        c.*,
        i.category_id,
        i.category_code,
        i.brand
    FROM customers c
    LEFT JOIN (
        SELECT DISTINCT ON (product_id) *
        FROM items
        ORDER BY product_id
    ) i ON c.product_id = i.product_id;

    DROP TABLE customers;
    ALTER TABLE customers_merged RENAME TO customers;
    
    DROP TABLE items;
"

echo "Completed successfully."