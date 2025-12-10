DO
$$
DECLARE
    r RECORD;
	target_table CONSTANT TEXT := 'customers';
    source_schema CONSTANT TEXT := 'public';
BEGIN
	CREATE TABLE IF NOT EXISTS customers (
		event_time TIMESTAMP,
		event_type VARCHAR(255),
		product_id INT,
		price NUMERIC(10, 2),
		user_id BIGINT,
		user_session UUID
	);
    FOR r IN (
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_name LIKE '%data%'
    )
    LOOP
EXECUTE 'INSERT INTO ' || quote_ident(target_table) || 
        ' SELECT * FROM ' || quote_ident(source_schema) || '.' || quote_ident(r.table_name);
END LOOP;
END
$$;