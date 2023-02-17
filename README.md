# Simple FastAPI App as a template.

[![Python 3.11](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/downloads/release/python-3110/)\
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%23316192.svg?style=for-the-badge&logo=docker&logoColor=white)

## Description
A simple application that makes it possible to get the price of pairs on binance.com.
Once a day it parses all pairs and updates the prices for pairs every 5 seconds.

## Setup
1. `git clone https://github.com/Sanchows/fastapi-template.git`
2. `cd test-task/`
3. `docker-compose up --build`
4. `curl -X 'GET' 'http://127.0.0.1:8000/api/v1/currency/ETHUSDT' -H 'accept: application/json'`
5. `To open docs:` http://127.0.0.1:8000/docs



Based on the https://github.com/geekceo/FastAPI-app-Redis-Docker repository with my changes.
