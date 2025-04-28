FROM fedora:latest

# 1. Install Python3, pip, Firefox, and utilities
RUN dnf -y install python3 python3-pip firefox \
    # Install libraries Firefox needs
    libX11 libXcomposite libXcursor libXdamage libXext libXi libXtst alsa-lib \
    # Clean package cache
    && dnf clean all

# 2. Download and install GeckoDriver
ARG GECKO_VERSION=0.33.0
RUN curl -L "https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VERSION}/geckodriver-v${GECKO_VERSION}-linux64.tar.gz" \
        | tar xz -C /usr/local/bin \
    && chmod +x /usr/local/bin/geckodriver \
    && geckodriver --version

# 3. Install Selenium Python binding
RUN pip3 install selenium

# Set working directory
WORKDIR /app

# Copy test script
COPY browser-test.py .

# Default command
CMD ["python3", "browser-test.py"]
