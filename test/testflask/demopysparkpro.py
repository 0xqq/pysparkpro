# coding:utf-8
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from urllib.parse import unquote
from basespark import spark
from dsltest.parser import parser
from dsltest.lexer import lexer
from dsltest.nodes import NodeType


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

    command = parser.parse(cur, lexer=lexer)

    if command.type == NodeType.create_table:
        pass
    elif command.type == NodeType.show_tables:
        pass
    elif command.type == NodeType.drop_table:
        pass
    elif command.type == NodeType.insert:
        pass
    elif command.type == NodeType.alert:
        pass
    elif command.type == NodeType.delete:
        pass
    elif command.type == NodeType.update:
        pass
    elif command.type == NodeType.select:
        data = spark.read.csv("file:///Users/leiqiankun/PycharmProjects/lqkcode/tianchi/pysparkpro/test/testflask/data/tianchi_fresh_comp_train_item.csv",header=True)
        data.createOrReplaceTempView("user")
        datatem = spark.sql(cur)
        datat_response = datatem.rdd.collect()
        emit('server_response', {'data': datat_response})
    elif command.type == NodeType.print_table:
        pass
    elif command.type == NodeType.create_index:
        pass
    elif command.type == NodeType.drop_index:
        pass
    elif command.type == NodeType.create_user:
        pass
    elif command.type == NodeType.grant_user:
        pass
    elif command.type == NodeType.revoke_user:
        pass




@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
