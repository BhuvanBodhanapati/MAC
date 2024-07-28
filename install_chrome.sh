#!/usr/bin/env bash

# Exit on error
set -e

echo "Downloading and unpacking Chrome..."

# Create a directory for Chrome
mkdir -p /tmp/chrome
cd /tmp/chrome

# Download a pre-built Chrome binary
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Extract the contents of the .deb package
ar x google-chrome-stable_current_amd64.deb
tar -xvf data.tar.xz

# Move the Chrome binary to a directory included in the PATH
mkdir -p $HOME/chrome
mv opt/google/chrome/* $HOME/chrome/

# Clean up
rm -rf /tmp/chrome

echo "Chrome installed successfully."
