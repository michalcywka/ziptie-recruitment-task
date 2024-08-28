# Ziptie recruitment task

## Installation

### Environment:
Windows 10 with Docker Desktop or a machine with docker and docker-compose installed.

### Setup
Clone the repository:

`git clone https://github.com/michalcywka/ziptie-recruitment-task.git`

Go to the main folder:

`cd ziptie-recruitment-task`

Execute:

`docker-compose up --build`

Service should be up and running.

## Interacting with the API

Recommended way to interact with the API and see available endpoints is to use Swagger UI http://127.0.0.1:8000/docs or ReDoc http://127.0.0.1:8000/redoc

There are also a few examples of payloads in the `test.ps1` file.

Database is initially populated with some data.