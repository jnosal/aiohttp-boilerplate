#!/bin/bash
gunicorn 'src.__main__:create_app' \
 --worker-class aiohttp.worker.GunicornUVLoopWebWorker \
 --timeout 30 \
 --log-level debug \
 --reload \
 --bind 0.0.0.0:6666