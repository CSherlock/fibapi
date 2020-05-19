# Fibonacci API

A small API that returns Fibonacci numbers. Built using Python and Flask.

## Task

The goal is to figure out the highest input index that be given where the application continues to return a valid Fibonacci number in the given index/position of the sequence.

You should also attempt to write API tests that prove where this occurs. This can be in whatever language you feel most comfortable using

## Running the API

To run the API locally, you will require *Python 3.8.x*. You can start the server by simply running `python runserver.py`

You can also build a Docker container using the provided Dockerfile by following:

    docker build . -t fibapi:latest
    docker run -p 5555:5555 fibapi:latest