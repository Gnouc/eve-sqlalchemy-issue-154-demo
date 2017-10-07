from eve import Eve


SETTINGS = {
    'DEBUG': True,
    'DOMAIN': {'tests': {}},
    'ALLOW_UNKNOWN': True,
    'HATEOAS': False,
}

app = Eve(settings=SETTINGS)


@app.before_first_request
def insert_data():
    app.data.driver.db.tests.insert({"foo": "bar", "null": None})


app.run()
