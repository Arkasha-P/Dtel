from flask import Flask, request, render_template
from db.sql import * 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_panel', methods=['POST'])
def submit():
    mac = request.form.get('mac')  # Получение значения поля 'text' из формы
    ip = request.form.get('ip')
    adress = request.form.get('adress')
    entrance = request.form.get('entrance')
    serial_number = request.form.get('serial_number')
    ext_entrance = request.form.get('ext_entrance')
    reley = request.form.get('reley')

    add_panel(mac,ip)
    set_panel_adress(mac,adress)
    set_panel_entrance(mac,entrance)
    set_panel_serial_number(mac,serial_number)
    set_panel_ext_entrance(mac,ext_entrance)
    set_panel_reley(mac,reley)

    return f'Панель добавлена в БД: {mac, " - ", ip}'

if __name__ == '__main__':
      app.run(debug=True)