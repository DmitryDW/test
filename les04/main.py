from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return request.get_json()
    else:
        return '{' \
               '    "name": "John",' \
               '    "surname": "Doe"' \
               '}'

if __name__ == '__main__':
    app.run()