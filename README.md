## Products application.

This application is for listing products.


### Requirements for setting up the project.

1. Python3. 
2. Django
3. Virtualenv.
4. Postgres DB
5. Docker

## Running with Docker.

The alternative way of running this project is by using Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project to spin the container.

### Installation on Mac/Linux.

1 . First clone this repository, but it's private.


2 . Add the following variables in your Environment Variables (.env file) permanently:

```
DATABASE_URL=postgres://user:password@localhost:5432/proucts_db
SECRET_KEY=sample
```


3 . Then, create a virtual environment and activate it as well on Mac/Linux :

```
$ virtualenv env
$ source env/bin/activate
```

4 . After activating the `virtualenv`, then install the necessary dependencies :

```
$ pip3 install -r requirements.txt
```

5 . Then run migrations. 

```
$ ./manage.py migrate
```

## Alternatively.

### Running with Docker.


The alternative way of running this project is by using Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project.


```
 $ docker compose up
```

After all is done, the host and the port will be http://0.0.0.0:8001/, then use corresponding endpoints in the table below :

**Endpoints**

| HTTP Method | End Point                              | Action                  |
|-------------|----------------------------------------|-------------------------|
| POST        | /api/v1/auth/signup/                   | Sign up                 |
| POST        | /api/v1/auth/login/                    | Login                   |
| POST        | /api/v1/products                       | Create products         |
| GET         | /api/v1/products                       | List all products       |
| POST        | /api/v1/products/select/<uuid:product> | Select a single product |



Alternatively, we can access the endpoints via swagger.
[Swagger endpoints](http://localhost:8001/swagger/)

### Running unit tests.

After cloning the application, do the following : 

1. Simply run ```python -m pytest```



### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)
