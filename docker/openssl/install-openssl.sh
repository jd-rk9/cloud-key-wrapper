#!/bin/bash

# Create the directory for the eventual OpenSSL binaries
mkdir -p ${HOME}/local/ssl

# Create the build directory
mkdir -p ${HOME}/build/openssl

# Extract the archive to ${HOME}/build/openssl
tar xzvf /path/to/downloaded-openssl.tar.gz \
  -C ${HOME}/build/openssl/ \
  --strip-components 1

  