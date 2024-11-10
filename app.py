from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
