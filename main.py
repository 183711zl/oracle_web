from flask import Flask
from flask import request,render_template
import demo
app=Flask(__name__)

@app.route('/')
def  homepage():
    return render_template('demo.html')

@app.route('/information')
def list_connection_show():
    nodeinfo = demo.list_connection()
    return render_template('connection_show.html',information=nodeinfo)

@app.route('/show')
def machine():
    a=demo.show_machine()
    return render_template('show.html',open=a[0],close=a[1])


@app.route('/close')
def close_connection():
    num=demo.close_connection()
    return render_template('close.html',think=num)
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create',methods=['POST'])
def create_():
    name = request.form['name']
    isok=demo.create(name)
    return render_template('create.html',isok=isok)
@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/start', methods=['POST'])
def start_():
    name = request.form['name']
    isok = demo.start(name)
    return render_template('start.html', isok=isok)

@app.route('/shutdown')
def shutdown():
    return render_template('shutdown.html')


@app.route('/shutdown', methods=['POST'])
def shutdown_():
    name = request.form['name']
    isok = demo.shutdown(name)
    return render_template('shutdown.html', isok=isok)



@app.route('/del')
def del_():
    return render_template('del.html')


@app.route('/del', methods=['POST'])
def del__():
    name = request.form['name']
    isok = demo.destroy(name)
    return render_template('del.html', isok=isok)


if __name__ == '__main__':
    app.run(host='192.168.1.155',debug=True)
