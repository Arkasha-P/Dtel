from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api_request', methods=['POST'])
def api_request():
    # Получение данных из формы
    data = request.form.get('data')
    
    # Отправка API-запроса
    response = requests.post('https://api.example.com', data=data)
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)