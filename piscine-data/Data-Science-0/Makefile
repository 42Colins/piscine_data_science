DOCKER_COMPOSE = docker compose -f ex00/docker-compose.yml

all: up ex02 ex03 ex04

up:
	${DOCKER_COMPOSE} up -d
	
down:
	${DOCKER_COMPOSE} down
	
clean:
	${DOCKER_COMPOSE} down --rmi all --volumes --remove-orphans
	
stop:
	${DOCKER_COMPOSE} stop
	
clean-tables:
	docker exec postgres psql -U cprojean -d piscineds -c "DO \$$\$$ DECLARE r RECORD; BEGIN FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP EXECUTE 'DROP TABLE IF EXISTS \"' || r.tablename || '\" CASCADE'; END LOOP; END \$$\$$;"
	
ex02:
	docker exec postgres psql -U cprojean -d piscineds -f /mnt/table.sql
	
ex03:
	docker exec postgres psql -U cprojean -d piscineds -f /mnt/automatic_table.sh
	
ex04:
	docker exec postgres psql -U cprojean -d piscineds -f /mnt/items_table.sh