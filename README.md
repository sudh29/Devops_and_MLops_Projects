# Podman_Example

## 1 Hello

podman build --tag python-podman .
podman run python-podman

## 2 Flask

podman build --tag python-podman .
podman run --publish 5000:5000 python-podman
http://127.0.0.1:5000

## 3 Selenium

podman build -t selenium-python .
docker build -t selenium-firefox-fedora .
podman run -t --rm --network host -v $(pwd)/browser-test.py:/browser-test.py:z selenium-python python3 browser-test.py
