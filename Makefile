.PHONY: help build start start_verbose stop clean

# #@-- help command to show usage of make commands --@#
# help:
# 	@echo "----------------------------------------------------------------------------"
# 	@echo "-                     Available commands                                   -"
# 	@echo "----------------------------------------------------------------------------"
# 	@echo "---> make build         - To build the docker image"
# 	@echo "---> make start         - To start the containers in the background"
# 	@echo "---> make start_verbose - To start the containers verbosely"
# 	@echo "---> make stop          - To stop the api containers"
# 	@echo "---> make clean         - To delete the application image"
# 	@echo "---> make help          - To show usage commands"
# 	@echo "----------------------------------------------------------------------------"


# #@-- command to build the application--@#
# build:
# 	@echo "Building application image"
# 	docker-compose build

#@-- command to start the container in the background --@#
start:
	@echo "Staring Up Dev Server"
	pipenv run python manage.py runserver

# #@-- command to start the application --@#
# start_verbose:
# 	@echo "Start up the api containers after building"
# 	@echo ""
# 	docker-compose up

# #@-- command to stop the application --@#
# stop:
# 	@echo "Stop running the api containers"
# 	@echo ""
# 	docker-compose down

# #@-- command to remove the images created --@#
# clean:
# 	@echo "\033[31m  Remove application image"
# 	@echo ""
# 	bash cleanup.sh

# #@-- help should be run by default when no command is specified --@#
# default: help

tests:
	@echo ">>>>>Running Tests >>>>>"
	pipenv run pytest

tests_verbose:
	@echo ">>>>>Running Tests Verbosely>>>>>"
	pipenv run pytest -v -s --setup-show
