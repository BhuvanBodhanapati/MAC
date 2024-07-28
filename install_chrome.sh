#!/usr/bin/env bash

# Exit on error
set -e

echo "Downloading and unpacking Chrome..."

# Create a directory for Chrome
mkdir -p $HOME/chrome
cd $HOME/chrome

# Download a pre-built Chrome binary
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Extract the contents of the .deb package
ar x google-chrome-stable_current_amd64.deb

# Extract the data.tar.xz file
tar -xvf data.tar.xz

# Check if the extracted directory exists and is not empty
if [ -d "opt/google/chrome" ]; then
    echo "Moving Chrome files to target directory..."

    # Ensure target directory is clean before moving new files
    rm -rf $HOME/chrome/opt/google/chrome
    mkdir -p $HOME/chrome/opt/google/chrome

    # Move the Chrome binary to the target directory
    mv opt/google/chrome/* $HOME/chrome/opt/google/chrome/ || {
        echo "Failed to move Chrome files. Please check the source directory."
        exit 1
    }

    echo "Chrome binary moved successfully."
else
    echo "Chrome extraction failed or directory not found."
    exit 1
fi

# Clean up
rm -rf opt google-chrome-stable_current_amd64.deb data.tar.xz

# Verify installation
$HOME/chrome/opt/google/chrome/google-chrome --version || {
    echo "Chrome installation verification failed."
    exit 1
}

echo "Chrome installed successfully."
