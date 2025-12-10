CREATE TABLE IF NOT EXISTS :file (
	product_id INT,
	category_id BIGINT,
	category_code VARCHAR(255),
	brand VARCHAR(255)
);

\set path '/mnt/data/' :file '.csv'
COPY :file (product_id, category_id, category_code, brand) FROM :'path' WITH (FORMAT csv, DELIMITER ',', HEADER true);