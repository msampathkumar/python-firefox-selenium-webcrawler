# Python Official - https://hub.docker.com/_/python
FROM python:slim-buster
EXPOSE 8888

WORKDIR /app

# Developer Tools
RUN apt update && apt install -y iputils-ping vim curl
RUN pip install jupyter

# App Requirements(Firefox, Geko)
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates curl firefox-esr  \
 && rm -fr /var/lib/apt/lists/*     \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl


# App Code Sample
COPY . .
RUN mkdir -p /var/www/.cache /var/www/.mozilla
RUN pip install -r requirements.txt

# COPY . .
# CME ["bash"]
# CMD ["bash", "notebook", "--ip 0.0.0.0", "--allow-root"]
# docker exec --name missing_code_samples -p 8080:8080 -e LOAD_EX=n googledocswebcrawler:1.0-beta /bin/bash
# jupyter notebook --ip 0.0.0.0 --allow-root