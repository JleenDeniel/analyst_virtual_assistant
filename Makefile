# Makefile

# Docker Hub credentials (these should be set in GitHub Actions secrets)
USERNAME=${DOCKER_USERNAME}
REPO=${DOCKER_REPO}
TAG=v1

# Build arguments
TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
OPENAI_API_KEY=${OPENAI_API_KEY}

# Build the Docker image
build:
	docker build --build-arg TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT_TOKEN) --build-arg OPENAI_API_KEY=$(OPENAI_API_KEY) -t $(USERNAME)/$(REPO):$(TAG) .

# Run the Docker container
dockerrun:
	docker run --rm -e TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT_TOKEN) -e OPENAI_API_KEY=$(OPENAI_API_KEY) $(USERNAME)/$(REPO):$(TAG)

# Push the Docker image to Docker Hub
push:
	docker push $(USERNAME)/$(REPO):$(TAG)
