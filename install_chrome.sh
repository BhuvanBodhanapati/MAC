#!/usr/bin/env bash

# Exit on error
set -e

echo "Installing Chrome..."

# Use sudo to run commands as root
sudo wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install -y google-chrome-stable

# Verify installation
google-chrome --version

echo "Chrome installed successfully."
