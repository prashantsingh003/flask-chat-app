from flask import Flask, redirect,render_template,request, url_for
from forms import JoiningForm
from flask_socketio import SocketIO, join_room

app=Flask(__name__)
socketio=SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
    username=request.args.get('username')
    room=request.args.get('room')
    if username and room:
        return render_template('chat.html',username=username,room=room )
    else:
        return redirect(url_for('home'))

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info(f'{data["username"]} has sent message \"{data["message"]}\" to the room {data["room"]}')
    socketio.emit('receive_message',data,room=data['room'])

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info(f'*****{data["username"]} joined room - {data["room"]}*****')
    join_room(data['room'])
    socketio.emit('join_room_announcement',data,room=data['room'])

if __name__=='__main__':
    socketio.run(app,debug=True)