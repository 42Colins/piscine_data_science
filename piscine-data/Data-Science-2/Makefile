DOCKER_COMPOSE = docker compose -f dockers/ex00/docker-compose.yml

all: up ex00 ex01 ex02 ex03

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
	
ex00:
	docker exec postgres sh /mnt/scripts/ex00/add_tables.sh
	
ex01:
	docker exec postgres psql -U cprojean -d piscineds -f /mnt/scripts/ex01/customers.sql
	
ex02:
	docker exec postgres psql -U cprojean -d piscineds -f /mnt/scripts/ex02/remove_duplicates.sql
	
ex03:
	docker exec postgres psql -U cprojean -d piscineds -f /mnt/scripts/ex03/fusion.sql
	
everyone:
	docker exec postgres sh /mnt/scripts/ex00/all.sh

	
.PHONY: all up down clean stop ex00 ex01 ex02 ex03 ex04 clean-tables