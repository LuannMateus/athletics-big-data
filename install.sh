#!/bin/bash

# Install the required packages
python3 setup.py bdist_wheel && pip install . && playwright install 