```javascript
// Importing necessary modules
import ChatInterface from './chat_interface.js';
import Theme from './theme.js';
import Responsive from './responsive.js';

// Initializing chat interface
const chatInterface = new ChatInterface();

// Initializing theme
const theme = new Theme();

// Initializing responsive design
const responsive = new Responsive();

// Function to handle user command
function handleUserCommand(command) {
    // Send command to backend
    fetch('/handle_command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({command: command})
    })
    .then(response => response.json())
    .then(data => {
        // Display generated code in chat interface
        chatInterface.displayCode(data.code);
    })
    .catch(error => console.error('Error:', error));
}

// Event listener for chat input
document.getElementById('chat-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        // Get user command
        const command = this.value;
        // Clear input field
        this.value = '';
        // Handle user command
        handleUserCommand(command);
    }
});

// Event listener for theme selection
document.getElementById('theme-selection').addEventListener('change', function() {
    // Apply selected theme
    theme.applyTheme(this.value);
});

// Event listener for window resize
window.addEventListener('resize', function() {
    // Apply responsive design
    responsive.applyResponsiveDesign();
});
```