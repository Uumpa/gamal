# Gamal

API For Camels

## Local Development

### Install

Create a virtualenv (using Python 3.8)

```
python3.8 -m venv venv
```

Update pip

```
venv/bin/pip install --upgrade pip
```

Install dependencies

```
venv/bin/pip install -r requirements.txt 
```

### Use

Activate virtualenv

```
. venv/bin/activate
```

Start the FastAPI server with automatic reload on changes

```
uvicorn gamal.main:app --reload
```

* See the homepage at http://localhost:8000
* See the API docs at http://localhost:8000/docs
