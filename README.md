# Sreality Scrapy

Application based on the [Scrapy](https://scrapy.org/) framework that extracts the first 500 flats (title and image url) from https://www.sreality.cz/.
Data are stored in a [Postgres](https://www.postgresql.org/) DB and they can be accessed via a simple [Flask](https://flask.palletsprojects.com/en/3.0.x/) web application.
Each component is containerized via [Docker](https://docs.docker.com/) and orchestrated via [*docker compose*](https://docs.docker.com/compose/).

List of containers involved:
- db - Postgres DB
- adminer - DB admin console
- scrapy - data scraper
- web - Flask web app

## Setup and run

- Clone the repo
- Start the application
    ```
    cd <repo-root>
    docker compose up
    ```

## Web links

- Adminer (DB admin page) http://127.0.0.1:8081

- Web page with scraped flats (Flask endpoint) http://127.0.0.1:8080/

