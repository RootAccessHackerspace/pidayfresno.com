#!/bin/bash

# Remove previous build artifacts
rm -rf .build/

# Create a fresh build
cactus build

# Import .build into the gh-pages branch and push to Github
ghp-import .build/ --push
