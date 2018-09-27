[![Build Status](https://travis-ci.org/mwinel/todo-list-api.svg?branch=develop)](https://travis-ci.org/mwinel/todo-list-api)

# todo-list-api
This is api provides users with the ability to add todo-items to their todo-lists.

### Stack
- Python
- Flask

### Installation and Set Up


Clone the repo from GitHub:

```
https://github.com/mwinel/todo-list-api.git
cd todo-list-api
```

### Create and activate virtualenv

```
python -m venv venv
venv\Scripts\activate => for windows
```

### Requirements

```
pip install -r requirements
```

### Set enviroment variables

```
set FLASK_APP="run.py"
```

### Run the Application

```
flask run
```

### Sample Requests

Index
```
HTTP/1.0 200 OK
GET http://localhost:5000/api/index

Request Headers:
cache-control:"no-cache"
postman-token:"7d1ee037-cbc7-4028-85c3-1bead661f507"
user-agent:"PostmanRuntime/7.3.0"
accept:"*/*"
host:"localhost:5000"
accept-encoding:"gzip, deflate"

Response Headers:
content-type:"application/json"
content-length:"36"
server:"Werkzeug/0.14.1 Python/3.6.5"
date:"Thu, 27 Sep 2018 05:46:15 GMT"

Response Body:
{
    "message": "Hello World"
}

```

### Runnint unit tests

```
python tests.py 
```

### API Endpoints

| Resource URL | Methods | Description | Requires Auth |
| -------- | ------------- | --------- |--------------- |
| `/api/index` | `GET`  | The index | `FALSE` |

### Testing Endpoints

Test endpoints in Postman or Curl.
