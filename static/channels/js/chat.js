document.addEventListener('DOMContentLoaded', () => {
    var roomName = JSON.parse(document.getElementById('room-name').textContent);
    var username = JSON.parse(document.getElementById('username').textContent);
    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/' + roomName + '/');

    chatSocket.onmessage = function(event) {
        var data = JSON.parse(event.data);
        var message = data['message'];
        var author = data['username'];
        var timestamp = data['timestamp'];

        // Append message to chat log
        var chatLog = document.getElementById('chat-log');
        var messageElem = document.createElement('div');
        messageElem.innerHTML = author + ' (' + timestamp + '): ' + message;
        chatLog.appendChild(messageElem);
    };

    chatSocket.onclose = function(event) {
        console.error('Chat socket closed unexpectedly');
    };

    // Handle form submission
    var form = document.getElementById('chat-form');
    var input = document.getElementById('message-input');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        var message = input.value;
        chatSocket.send(JSON.stringify({
            'message': message,
            'username': username
        }));
        input.value = '';
    });
});
