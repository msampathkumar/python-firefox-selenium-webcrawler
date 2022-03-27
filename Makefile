APP_VERSION=1.0-beta
APP_NAME=python-firefox-selenium-webcrawler
APP_RUN_NAME=running-webcrawler

help:	## Help Command
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

version: ## Prints Build version
	set -e; \
	export APP_VERSION=${APP_VERSION}
	@echo "Image Version "${APP_VERSION}

build: ## Build docker image
	docker build --rm -t ${APP_NAME}:${APP_VERSION} .

run: ## Run the docker in background
	docker run -d \
	--name ${APP_RUN_NAME} \
	-p 5555:5555 \
	-p 8080:8080 \
	-e LOAD_EX=n \
	${APP_NAME}:${APP_VERSION} bash
	docker rm $(docker ps --filter status=exited -q)

rm: ## Remove the docker image
	docker rm -f ${APP_RUN_NAME}

exec: ## Run the docker images in interactive mode
	docker run -it --rm --name ${APP_RUN_NAME}  -p 8888:8888 ${APP_NAME}:${APP_VERSION} bash
