from celeryapp import app

@app.task
def add(x, y):
    return x + y

@app.task
def sub(x, y):
    return x - y

@app.task
def mul(x, y):
    return x * y

@app.task
def div(x, y):
    return x / y

