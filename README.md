# Podman_Example

## 1 Hello

podman build --tag python-podman .
podman run python-podman

## 2 Flask

podman build --tag python-podman .
podman run --publish 5000:5000 python-podman
http://127.0.0.1:5000

## 3 Selenium

podman build -t selenium-chrome .

podman run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium-chrome
podman run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium-chrome bash

podman run -it --rm --shm-size=2g selenium-chrome
podman run -it --rm --shm-size=2g selenium-chrome bash

## 4 Selenium Python

podman build -t python-chrome .

podman run -it --rm --shm-size=2g python-chrome
podman run -it --rm --shm-size=2g python-chrome bash

## 5 Selenium Grid Docker

podman-compose -f docker-compose-v3.yml up # Uses existing images (builds only if missing).
podman-compose -f docker-compose-v3.yml up --build #Forces a rebuild of images before starting.
podman-compose -f docker-compose-v3.yml down

podman exec -it selenium-hub /bin/sh
podman exec -it selenium-node-chrome /bin/sh

podman cp browser-test.py selenium-node-chrome:/home/

podman-compose logs -f chrome

## Podman Commands

### Container Management

podman ps # List running containers
podman ps -a # List all containers, including stopped ones
podman run [options] IMAGE [COMMAND] # Create and start a new container
podman stop -a # Stop all running containers
podman rm -a # Remove all containers
podman exec -it CONTAINER COMMAND # Execute a command in a running container
podman logs CONTAINER # Fetch logs of a container
podman inspect CONTAINER # Display detailed information on a container
podman stats # Display a live stream of container resource usage

### Image Management

podman images # List all local images
podman pull IMAGE # Pull an image from a registry
podman rmi -a --force # Forcefully remove all images
podman image prune # Remove unused images
podman build -t IMAGE_NAME PATH # Build an image from a Dockerfile
podman tag SOURCE_IMAGE TARGET_IMAGE # Add a new tag to an image
podman push IMAGE # Push an image to a registry

### Volume & Filesystem

podman volume ls # List volumes
podman volume create VOLUME_NAME # Create a new volume
podman volume rm VOLUME_NAME # Remove a volume
podman cp SOURCE DESTINATION # Copy files between host and container
podman diff CONTAINER # Inspect changes to a container's filesystem

### Networking

podman network ls # List networks
podman network create NETWORK_NAME # Create a new network
podman network rm NETWORK_NAME # Remove a network
podman port CONTAINER # List port mappings for a container

### Pod Management

podman pod create --name POD_NAME # Create a new pod
podman pod ps # List running pods
podman pod stop POD_NAME # Stop a running pod
podman pod rm POD_NAME # Remove a pod

### Miscellaneous

podman version # Display Podman version information
podman info # Display system information
podman system prune # Remove unused data (containers, images, volumes)
podman login REGISTRY # Log in to a container registry
podman logout REGISTRY # Log out from a container registry
podman --help # Display help information
