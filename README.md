# Docker Scraper

Simple demonstration of running three docker containers with `docker compose`.

The containers:

1. Database container is created from the official PostgreSQL [image](https://hub.docker.com/_/postgres).
2. Web crawler [scrapy](https://scrapy.org/) obtains and stores the list of apartments from https://www.sreality.cz in the database.
3. Simple Flask application connects to the database and shows the list of data.

## Usage

Run `docker compose up` in the project root and navigate to http://0.0.0.0:8080.
