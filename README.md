# library_api

## Installation

Clone this project:

```
git clone https://github.com/rafaelhenrique/library_api.git
```

Enter on directory:

```
cd library_api
```

Create virtualenv:

```
python3.5 -m venv .venv
```

Activate your virtualenv:

```
source .venv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

## Run project

Activate your virtualenv:

```
source .venv/bin/activate
```

Then run:

```
python3.5 app.py
```

## Make requests

### Get all books

```
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:5000/v1/books"
```

### Get an specific book

```
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:5000/v1/books/<id of book>"
```

### Create an book

```
curl -X POST -H "Content-Type: application/json" -d '{ \
    "title": "Title of Book", \
    "tags": ["my-tag"], \
    "authors": ["Rafael Henrique da Silva Correia"], \
    "publishing": "Test" \
}' "http://127.0.0.1:5000/v1/books"
```

### Update information about book

```
curl -X PUT -H "Content-Type: application/json" -d '{ \
    "title": "Harry Potter e a Criança Amaldiçoada", \
    "tags": ["fantasy", "harry-potter"], \
    "authors": ["J. K. Rowling", "Jack Thorne", "John Tiffany"], \
    "publishing": "Rocco" \
}' "http://127.0.0.1:5000/v1/books/<id of book>"
```

### Delete/Remove an specific book

```
curl -X DELETE -H "Content-Type: application/json" "http://127.0.0.1:5000/v1/books/<id of book>"
```

