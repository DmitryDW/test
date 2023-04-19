from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request.status_code = 204
        return request.get_json()
    else:
        return '{' \
               '    "name": "John",' \
               '    "surname": "Doe"' \
               '}'

@app.route('/api/user/info', methods=['GET'])
def api_user_info():
    return '{' \
               '    "name": "John",' \
               '    "surname": "John"' \
               '}'

if __name__ == '__main__':
    app.run()
