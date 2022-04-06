build:
	docker compose build

run:
	docker compose up -d

runci:
	docker compose up -d app

lint:
	docker compose exec -T app pre-commit run --all-files
