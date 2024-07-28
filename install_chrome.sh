#!/usr/bin/env bash

# Exit on error
set -e

echo "Downloading and unpacking Chrome..."

# Create a directory for Chrome
mkdir -p $HOME/chrome
cd $HOME/chrome

# Download a pre-built Chrome binary
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Extract the contents of the .deb package
ar x google-chrome-stable_current_amd64.deb
tar -xvf data.tar.xz

# Ensure target directories are clean before moving new files
rm -rf $HOME/chrome/opt/google/chrome
mkdir -p $HOME/chrome/opt/google/chrome

# Move the Chrome binary to the target directory
mv opt/google/chrome/* $HOME/chrome/opt/google/chrome/

# Clean up
rm -rf opt google-chrome-stable_current_amd64.deb data.tar.xz

# Verify installation
$HOME/chrome/opt/google/chrome/google-chrome --version

echo "Chrome installed successfully."
