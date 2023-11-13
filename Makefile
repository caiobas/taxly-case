up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

update:
	docker-compose down && docker-compose build && docker-compose up -d