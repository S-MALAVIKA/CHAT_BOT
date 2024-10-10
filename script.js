document.getElementById('send-btn').addEventListener('click', function() {
    var userMessage = document.getElementById('user-input').value;
    if (userMessage) {
        addMessageToChatBox('You: ' + userMessage);
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'message=' + encodeURIComponent(userMessage)
        })
        .then(response => response.json())
        .then(data => {
            addMessageToChatBox('Bot: ' + data.response);
        });
        document.getElementById('user-input').value = '';
    }
});

function addMessageToChatBox(message) {
    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<p>' + message + '</p>';
    chatBox.scrollTop = chatBox.scrollHeight;
}
