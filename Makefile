check-docker:
	@docker -v >/dev/null 2>&1 || { echo "Docker is not installed. Please install Docker before proceeding."; exit 1; }
	@echo "Docker detected"

build: check-docker
	@echo "Building the project..."
	@cd docker_tut && sudo docker-compose -f docker-compose.yml build

run: check-docker
	@echo "Running the project..."
	@cd docker_tut && sudo docker-compose -f docker-compose-notest.yml up

run_test: check-docker
	@echo "Running the project and tets..."
	@cd docker_tut && sudo docker-compose -f docker-compose.yml up -d
	@cd qa && ./local_full_test.sh

stop:
	@echo "Stopping the project..."
	@cd docker_tut && sudo docker-compose -f docker-compose-notest.yml down

stop_clear_db: stop
	@read -p "Are you sure you want to proceed? (y/n): " answer; \
	if [ "$$answer" = "y" ] || [ "$$answer" = "Y" ]; then \
		echo "Proceeding..."; \
		echo "Clearing the database..."; \
		cd docker_tut && sudo docker volume rm docker_tut_db; \
	else \
		echo "Cancelled."; \
		exit 0; \
	fi

clear_docker: stop_clear_db
	@echo "Clearing Docker resources..."
	@cd docker_tut && sudo docker system prune -af
