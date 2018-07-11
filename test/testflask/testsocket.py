# coding:utf-8
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from urllib.parse import unquote
from basespark import spark

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('socket.html')


@socketio.on('client_event', namespace='/test')
def client_msg(msg):
    cur = unquote(msg["data"])
    data = spark.read.csv("file:///Users/leiqiankun/PycharmProjects/lqkcode/tianchi/pyspark_code/fresh_comp_offline/tianchi_fresh_comp_train_item.csv", header=True)
    data.createOrReplaceTempView("user")
    datatem = spark.sql(cur)

    emit('server_response', {'data': datatem.rdd.collect()})


@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
