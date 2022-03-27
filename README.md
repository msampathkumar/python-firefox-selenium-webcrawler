# Python - Firefox - Selenium - Webcrawler

Use the attached `Makefile` to try following commands, from your github repository

```bash
bash$ make
help:    Help Command
version:  Prints Build version
build:  Build docker image
run:  Run the docker in background
rm:  Remove the docker image
exec:  Run the docker images in interactive mode
```

#### To build docker from scratch

```bash
bash$ make build
docker build --rm -t python-firefox-selenium-webcrawler:1.0-beta .
[+] Building 8.7s (14/14) FINISHED                                                                                                                                                                                         
 => [internal] load build definition from Dockerfile                                                                                                                                                                  0.0s
 => => transferring dockerfile: 40B                                                                                                                                                                                   0.0s
 => [internal] load .dockerignore                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:slim-buster                                                                                                                                                 1.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                         0.0s
 => [1/8] FROM docker.io/library/python:slim-buster@sha256:8bc3bd8e4d9f49a051efa8c91b2fa530551b7cd639e089e58c1faee845dcb14b                                                                                           0.0s
 => [internal] load build context                                                                                                                                                                                     0.1s
 => => transferring context: 169.41kB                                                                                                                                                                                 0.1s
 => CACHED [2/8] WORKDIR /app                                                                                                                                                                                         0.0s
 => CACHED [3/8] RUN apt update && apt install -y iputils-ping vim curl                                                                                                                                               0.0s
 => CACHED [4/8] RUN pip install jupyter                                                                                                                                                                              0.0s
 => CACHED [5/8] RUN apt-get update  && apt-get install -y --no-install-recommends ca-certificates curl firefox-esr   && rm -fr /var/lib/apt/lists/*      && curl -L https://github.com/mozilla/geckodriver/releases  0.0s
 => [6/8] COPY . .                                                                                                                                                                                                    0.3s
 => [7/8] RUN mkdir -p /var/www/.cache /var/www/.mozilla                                                                                                                                                              0.3s
 => [8/8] RUN pip install -r requirements.txt                                                                                                                                                                         6.2s
 => exporting to image                                                                                                                                                                                                0.4s
 => => exporting layers                                                                                                                                                                                               0.4s
 => => writing image sha256:846c58360e18cffb9ace8fe2912024244d4bf1396d226e78ea5f843dfe00fd29                                                                                                                          0.0s
 => => naming to docker.io/library/python-firefox-selenium-webcrawler:1.0-beta                                                                                                                                        0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
$
```

#### To run Jupyter notebook
```bash
bash$ make exec
docker run -it --rm --name running-webcrawler  -p 8888:8888 python-firefox-selenium-webcrawler:1.0-beta bash
root@0bc52b446b9c:/app# jupyter notebook --ip 0.0.0.0 --allow-root
```

#### To test run Crawler
```bash
bash$ make exec
docker run -it --rm --name running-webcrawler  -p 8888:8888 python-firefox-selenium-webcrawler:1.0-beta bash
root@fce39b67b74f:/app# ls -l
total 28
-rw-r--r-- 1 root root  910 Mar 27 19:21 Dockerfile
-rw-r--r-- 1 root root  823 Mar 27 19:28 Makefile
-rw-r--r-- 1 root root  664 Mar 27 19:28 README.md
-rw-r--r-- 1 root root 2531 Mar 27 17:37 crawler.py
-rw-r--r-- 1 root root   62 Mar 27 18:34 requirements.txt
-rw-r--r-- 1 root root   91 Mar 27 18:57 urls_list
drwxr-xr-x 4 root root 4096 Mar 27 19:28 venv
root@fce39b67b74f:/app# python crawler.py
start_time is 1648409486.1282618
THREAD_COUNTS is 4
#Running https://www.google.com/#
#Running https://www.yahoo.com/#
#Running https://duckduckgo.com/#
#Running https://www.msn.com/#
Wait Error: https://www.google.com/ 
Message: 
Stacktrace:
WebDriverError@chrome://remote/content/shared/webdriver/Errors.jsm:181:5
NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.jsm:393:5
element.find/</<@chrome://remote/content/marionette/element.js:305:16


Wait Error: https://www.yahoo.com/ 
Message: 
Stacktrace:
WebDriverError@chrome://remote/content/shared/webdriver/Errors.jsm:181:5
NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.jsm:393:5
element.find/</<@chrome://remote/content/marionette/element.js:305:16


Wait Error: https://duckduckgo.com/ 
Message: 
Stacktrace:
WebDriverError@chrome://remote/content/shared/webdriver/Errors.jsm:181:5
NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.jsm:393:5
element.find/</<@chrome://remote/content/marionette/element.js:305:16


Wait Error: https://www.msn.com/ 
Message: 
Stacktrace:
WebDriverError@chrome://remote/content/shared/webdriver/Errors.jsm:181:5
NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.jsm:393:5
element.find/</<@chrome://remote/content/marionette/element.js:305:16


#NoDataFound https://www.google.com/#
#Saving to html_files/https:##www.google.com#.html#
#NoDataFound https://www.yahoo.com/#
#Saving to html_files/https:##www.yahoo.com#.html#
#NoDataFound https://duckduckgo.com/#
#Saving to html_files/https:##duckduckgo.com#.html#
#NoDataFound https://www.msn.com/#
#Saving to html_files/https:##www.msn.com#.html#
Done!
Total is 52.174859046936035
root@fce39b67b74f:/app# ls -l 
total 36
-rw-r--r-- 1 root root  910 Mar 27 19:21 Dockerfile
-rw-r--r-- 1 root root  823 Mar 27 19:28 Makefile
-rw-r--r-- 1 root root  664 Mar 27 19:28 README.md
-rw-r--r-- 1 root root 2531 Mar 27 17:37 crawler.py
-rw-r--r-- 1 root root 3852 Mar 27 19:31 geckodriver.log
drwxr-xr-x 2 root root 4096 Mar 27 19:32 html_files
-rw-r--r-- 1 root root   62 Mar 27 18:34 requirements.txt
-rw-r--r-- 1 root root   91 Mar 27 18:57 urls_list
drwxr-xr-x 4 root root 4096 Mar 27 19:28 venv
root@fce39b67b74f:/app# ls -l html_files/
total 732
-rw-r--r-- 1 root root  37537 Mar 27 19:32 https:##duckduckgo.com#.html
-rw-r--r-- 1 root root 162622 Mar 27 19:32 https:##www.google.com#.html
-rw-r--r-- 1 root root 502789 Mar 27 19:32 https:##www.msn.com#.html
-rw-r--r-- 1 root root  37159 Mar 27 19:32 https:##www.yahoo.com#.html
root@fce39b67b74f:/app# 
```