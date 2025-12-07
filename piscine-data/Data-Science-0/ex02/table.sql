

CREATE TABLE IF NOT EXISTS data_2022_oct (
	event_time TIMESTAMP,
	event_type VARCHAR(255),
	product_id INT,
	price NUMERIC(10, 2),
	user_id BIGINT,
	user_session UUID
);

COPY data_2022_oct (event_time, event_type, product_id, price, user_id, user_session) FROM '/mnt/subject/customer/data_2022_oct.csv' WITH (FORMAT csv, DELIMITER ',', HEADER true);