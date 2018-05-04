# flask-logging-sample

First, configure logging via `logging.yml`.

The default configuration demonstrates three logging handlers:
stdout, file, and logstash.

Next, start the `simple` Flask application with three logging endpoints using:

    flask run

Then, query any of the following three endpoints

 - http://localhost:5000/ping
 - http://localhost:5000/fault
 - http://localhost:5000/rarefault

Each endpoint will generate one or more sample log entries.
