# Makefile

# Docker Hub credentials (these should be set in GitHub Actions secrets)
USERNAME=${DOCKER_USERNAME}
REPO=${DOCKER_REPO}
TAG=v1

IMAGE = $(USERNAME)/$(REPO):$(TAG)

# Build arguments
TELEGRAM_BOT=${TELEGRAM_BOT_TOKEN}
OPENAI_API=${OPENAI_API_KEY}

# Build the Docker image
build:
	@echo "Build image $(IMAGE)"
	docker build --build-arg TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT) --build-arg OPENAI_API_KEY=$(OPENAI_API) -t $(IMAGE) .	
	
# Run the Docker container
dockerrun:
	docker run --rm -e TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT) -e OPENAI_API_KEY=$(OPENAI_API) $(USERNAME)/$(REPO):$(TAG)

# Pull the Docker container
dockerpull:
	docker pull $(USERNAME)/$(REPO):$(TAG)

# Push the Docker image to Docker Hub
push:
	docker push $(USERNAME)/$(REPO):$(TAG)
