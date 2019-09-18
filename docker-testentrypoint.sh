#!/bin/bash
find src/ \( -name __pycache__ -o -name '*.pyc' \) -delete
py.test --cov=src
