async function sendMessage() {
  const input = document.getElementById("userInput");
  const chat = document.getElementById("chatBox");
  const typing = document.getElementById("typing");

  if (!input.value.trim()) return;

  chat.innerHTML += `<div class="user-msg"><span>${input.value}</span></div>`;
  typing.style.display = "block";

  const query = input.value;
  input.value = "";

  const res = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  });

  const data = await res.json();

  typing.style.display = "none";

  chat.innerHTML += `
    <div class="bot-msg">
      <img src="https://i.pinimg.com/736x/15/34/92/153492d5cc36e23919920d27ab4b08cc.jpg" />
      <span>${data.answer}</span>
    </div>
  `;

  chat.scrollTop = chat.scrollHeight;
}
