from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# 模拟的实时数据源
def get_real_time_data():
    # 这里只是返回一个模拟的数据，实际应用中，你可能需要通过网络请求或其他方式获取
    return f"实时数据: {time.strftime('%Y-%m-%d %H:%M:%S')}"


# 定时任务，模拟实时数据更新
@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    # 启动一个后台线程来发送实时数据
    from threading import Thread
    def background_thread():
        count = 0
        while True:
            time.sleep(1)  # 每秒发送一次数据
            count += 1
            socketio.emit('my_response',
                          {'data': get_real_time_data(), 'count': count},
                          namespace='/test')
    thread = Thread(target=background_thread)
    thread.start()


@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)