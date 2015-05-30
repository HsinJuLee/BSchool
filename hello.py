from flask import Flask
import os

print(os.environ['APP_SETTINGS'])

app = Flask(__name__)
app.config.from_objects(os.environ['APP_SETTINGS'])


@app.route("/")
def hello():
    return "Schools and houses go here!"

if __name__ == "__main__":
    app.run()