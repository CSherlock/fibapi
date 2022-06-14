# Fibonacci API

A small API that returns Fibonacci numbers. Built using Python and Flask.

## Background

A Fibonacci number is one which is part of the sequence such that each number is the sum of the previous two numbers, starting with:

    1, 1, 2, 3...

## Task

The goal is to figure out the first index that can be given where the application returns an invalid Fibonacci number (i.e. not in the Fibonacci sequence).

**You are permitted to use any available resources to you to assist with this, including Google searching**

You should also think about what tests you could create to test this API.

## Running the API

To run the API locally, you will require *Python 3.8.x*. Install the dependencies by running `pip install -r requirements.txt`. You can then start the server by simply running `python runserver.py`

You can also use Docker by building the container using the provided Dockerfile:

    docker build . -t fibapi:latest
    docker run -p 5555:5555 fibapi:latest
