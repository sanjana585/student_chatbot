document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const clearBtn = document.getElementById('clear-btn');

    // Store the initial HTML to allow resetting the chat
    const initialHtml = chatBox.innerHTML;

    function appendMessage(sender, text) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = text;

        messageDiv.appendChild(contentDiv);
        chatBox.appendChild(messageDiv);
        scrollToBottom();
    }

    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('message', 'bot-message');
        typingDiv.id = 'typing-indicator';

        typingDiv.innerHTML = `
            <div class="typing-indicator">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        `;

        chatBox.appendChild(typingDiv);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    function scrollToBottom() {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function disableChat() {
        userInput.disabled = true;
        sendBtn.disabled = true;
        userInput.placeholder = "Chat session ended. Refresh to restart.";
    }

    const exitBtn = document.getElementById('exit-btn');
    if (exitBtn) {
        exitBtn.addEventListener('click', () => {
            appendMessage('bot', 'Chat session terminated. Goodbye!');
            disableChat();
        });
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        // Append user message to the UI
        appendMessage('user', text);
        userInput.value = '';

        // Added quick frontend check for exit command
        if (text.toLowerCase() === 'exit' || text.toLowerCase() === 'quit') {
            setTimeout(() => {
                appendMessage('bot', 'Goodbye! Have a great day.');
                disableChat();
            }, 500);
            return;
        }

        // Show typing animation while waiting for response
        showTypingIndicator();

        try {
            const response = await fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: text }),
            });

            removeTypingIndicator();

            if (response.ok) {
                const data = await response.json();
                // Adding a tiny delay to simulate actual typing time
                setTimeout(() => {
                    appendMessage('bot', data.response);
                }, 300);
            } else {
                appendMessage('bot', 'Sorry, I encountered an error connecting to the server.');
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            removeTypingIndicator();
            appendMessage('bot', 'Sorry, my server is currently unreachable.');
        }
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    clearBtn.addEventListener('click', () => {
        // Reset the chatBox HTML to its initial state
        chatBox.innerHTML = initialHtml;
        // Re-enable chat if it was disabled
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.placeholder = "Type your question here...";
    });
});
