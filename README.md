# Setup

## Install pipenv
```sh
pip install pipenv
```

## Install dependencies
```sh
pipenv install --ignore-pipfile
```

## Run
```sh
pipenv run python app.py
```

## Verify
```sh
$ curl localhost:5000/tests?pretty=true
{
    "_items": [
        {
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "null": null,
            "foo": "bar",
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_id": "59d84ecdb47d26625164ed36",
            "_etag": "6649448751b876b977af3499bd65d6099b7fae7e"
        }
    ],
    "_meta": {
        "max_results": 25,
        "total": 1,
        "page": 1
    }
}
```
