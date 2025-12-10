

CREATE TABLE IF NOT EXISTS :file (
	event_time TIMESTAMP,
	event_type VARCHAR(255),
	product_id INT,
	price NUMERIC(10, 2),
	user_id BIGINT,
	user_session UUID
);

\set path '/mnt/data/customer/' :file '.csv'
COPY :file (event_time, event_type, product_id, price, user_id, user_session) FROM :'path' WITH (FORMAT csv, DELIMITER ',', HEADER true);