DO $$
DECLARE
    initial_customers_count INTEGER;
    final_customers_count INTEGER;
    updated_rows_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO initial_customers_count FROM customers;
    RAISE NOTICE 'Initial customers count : %', initial_customers_count;

    ALTER TABLE customers
        ADD COLUMN IF NOT EXISTS category_id BIGINT,
        ADD COLUMN IF NOT EXISTS category_code VARCHAR(100),
        ADD COLUMN IF NOT EXISTS brand VARCHAR(100);

    RAISE NOTICE 'Added missing columns to customers table (if any)';

    CREATE INDEX IF NOT EXISTS idx_item_product_id ON item(product_id);
    CREATE INDEX IF NOT EXISTS idx_customers_product_id ON customers(product_id);
    RAISE NOTICE 'Ensured necessary indexes are present.';

    UPDATE customers AS c
    SET
        category_id   = i.category_id,
        category_code = i.category_code,
        brand         = i.brand
    FROM
        item AS i
    WHERE i.product_id = c.product_id
      AND (
        c.category_id   IS DISTINCT FROM i.category_id OR
        c.category_code IS DISTINCT FROM i.category_code OR
        c.brand         IS DISTINCT FROM i.brand
      );
END $$;