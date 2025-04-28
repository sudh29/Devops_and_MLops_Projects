# Podman_Example

## 1 Hello

podman build --tag python-podman .
podman run python-podman

## 2 Flask

podman build --tag python-podman .
podman run --publish 5000:5000 python-podman
http://127.0.0.1:5000

## 3 Selenium

podman build -t selenium-python-chrome .

podman run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium-python-chrome
podman run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium-python-chrome bash

podman run -it --rm --shm-size=2g selenium-python-chrome
podman run -it --rm --shm-size=2g selenium-python-chrome bash
