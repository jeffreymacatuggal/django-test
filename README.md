
# Django Rest Api w/ Scrapy

This is a python test that scrape data from a website then save the data in database the retrieve scrape data using Django Rest Api.



## Install and run locally from a virtual environment

1. Open your terminal and clone this project

```shell
git clone https://github.com/jeffreymacatuggal/django-test.git
```

2. change your directory to this project
```shell
cd django-test
```

3. create a virtual environment and make sure there's already a [Python 3.11+](https://www.python.org/downloads/) and [PIP 23.2+](https://pip.pypa.io/en/stable/installation/) installed globally in your machine

```shell
python -m venv venv
```
or

```shell
python3 -m venv venv
```


4. Activate the virtual environment for Windows
```shell
venv\scripts\activate
```

For MacOS
```shell
source venv/bin/activate
```

5. Install packages in requirements.txt
```shell
pip install -r requirements.txt
```
or
```shell
pip3 install -r requirements.txt
```

6. Run the server 
```shell
python manage.py runserver
```



## Run scrapy spider

Use this command to run scrapy spider and save scrape data in database
```shell
python manage.py scrape_products
````


## Interact w/ REST API

make sure the server is running then open your browser and go to this 
```
http://127.0.0.1:8000/products/
````

## API Documentation

make sure the server is running then open your browser and go to this url for 
documentaion of Products API
```
http://127.0.0.1:8000/swagger/schema/
````
