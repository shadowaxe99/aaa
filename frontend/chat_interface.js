```javascript
// frontend/chat_interface.js

// DOM Elements
const chatInput = document.getElementById('chat-input');
const chatOutput = document.getElementById('chat-output');
const sendButton = document.getElementById('send-button');

// Event Listener for Send Button
sendButton.addEventListener('click', () => {
    let userCommand = chatInput.value;
    chatInput.value = '';

    // Send user command to backend
    fetch('/process-command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ command: userCommand }),
    })
    .then(response => response.json())
    .then(data => {
        // Display generated code in chat output
        chatOutput.value = data.code;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
```