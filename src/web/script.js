// 1. Select the HTML elements using their IDs
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// 2. Define your Flask API URL (Update this if using ngrok)
const apiUrl = "http://127.0.0.1:5000/chat";

// 3. Make the Send Button trigger the function
sendBtn.addEventListener("click", sendMessage);

// Allow the user to press "Enter" to send
userInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {
    const messageText = userInput.value.trim();
    if (messageText === "") return;

    // Show the user's message on the screen
    chatBox.innerHTML += `<div class="user-message">You: ${messageText}</div>`;
    userInput.value = ""; // Clear the input field

    // Show a loading indicator
    const typingId = "typing-" + Date.now();
    chatBox.innerHTML += `<div id="${typingId}" class="bot-message">AI is thinking...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom

    try {
        // 4. THE INTEGRATION: Send the request to your Flask API
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: messageText })
        });

        const data = await response.json();
        
        // Remove the "thinking..." text
        document.getElementById(typingId).remove();

        // 5. Display the AI's actual response
        if (response.ok) {
            chatBox.innerHTML += `<div class="bot-message">AI: ${data.reply}</div>`;
        } else {
            chatBox.innerHTML += `<div class="bot-message" style="color: red;">Error: ${data.error}</div>`;
        }

    } catch (error) {
        document.getElementById(typingId).remove();
        chatBox.innerHTML += `<div class="bot-message" style="color: red;">Connection failed. Is Flask running?</div>`;
    }
    
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom again
}