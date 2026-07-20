 async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const userText = input.value.trim();
    if (userText === "") return;

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.textContent = userText;
    chatBox.appendChild(userMessage);

    input.value = "";

    // Show typing indicator
    const typingMessage = document.createElement("div");
    typingMessage.className = "message bot-message";
    typingMessage.id = "typing";
    typingMessage.textContent = " AI is Typing...";
    chatBox.appendChild(typingMessage);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userText })
        });

        const data = await response.json();

        // Remove typing indicator
        document.getElementById("typing").remove();

        // Display AI response
        const botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        botMessage.textContent = data.reply || "Sorry, I didn't understand that.";
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        document.getElementById("typing").remove();

        const errorMessage = document.createElement("div");
        errorMessage.className = "message bot-message";
        errorMessage.textContent = "Sorry, something went wrong. Please try again.";
        chatBox.appendChild(errorMessage);
    }
}

async function createTicket() {
    const name = document.getElementById("ticket-name").value;
    const issue = document.getElementById("ticket-issue").value;

    if (name.trim() === "" || issue.trim() === "") {
        alert("Please fill all fields");
        return;
    }

    const response = await fetch("/create-ticket", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name, issue: issue })
    });

    const data = await response.json();

    if (data.status === "error") {
        alert(`Ticket failed: ${data.message}`);
        return;
    }

    alert(`Ticket #${data.ticket_id} created successfully!`);

    document.getElementById("ticket-name").value = "";
    document.getElementById("ticket-issue").value = "";
}
