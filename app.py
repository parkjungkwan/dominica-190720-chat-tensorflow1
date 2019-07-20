from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

usernames = {}
number_of_users = 0

"""
pip install flask-socketio
pip install python-dotenv
"""
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))
@app.route('/weather')
def weather():
    return render_template('weather.html'.format(path))

@socketio.on('new message', namespace='/chat')
def new_message(data):
    emit('new message',
         {'username' : session['username'],
          'message' : data},
         broadcast=True)

@socketio.on('connection', namespace='/chat')
def user_connected():
    print ('USER CONNECTED !!')

@socketio.on('typing', namespace='/chat')
def typing_response():
    try:
        emit('typing', {'username' : session['username']}, broadcast=True)
    except:
        pass

@socketio.on('stop typing', namespace='/chat')
def stop_typing():
    try:
        emit('stop typing', {'username' : session['username']}, broadcast=True)
    except:
        pass

@socketio.on('disconnect', namespace='/chat')
def disconnect():
    global usernames
    global number_of_users

    try:
        del usernames[session['username']]
        number_of_users -= 1
        emit('user left', {'username' : session['username'],
             'numUsers': number_of_users}, broadcast=True)
    except:
        pass

@socketio.on('add user', namespace='/chat')
def add_user(data):
    global usernames
    global number_of_users


    session['username'] = data
    usernames[data] = session['username']

    number_of_users += 1
    emit('login', {'numUsers' : number_of_users})
    emit('user joined', {'username' : session['username'],
                         'numUsers': number_of_users},
         broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
    # app.run()