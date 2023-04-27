function sendMessage() {
  var message = document.getElementById("input-box").value;
  document.getElementById("input-box").value = "";

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/send_message");
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onload = function() {
    if (xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      var chatBox = document.getElementById("chat-box");
      chatBox.innerHTML += "<p><strong>You:</strong> " + message + "</p>";
      chatBox.innerHTML += "<p><strong>Chat Bot:</strong> " + response.message + "</p>";
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  };
  xhr.send(JSON.stringify({ "message": message }));
}
