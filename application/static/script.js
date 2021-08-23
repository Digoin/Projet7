var input = document.getElementById("question");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("validate").click();
    }
});

let ask = async function() {
    question = document.getElementById("question").value
    let response = await fetch(`http://localhost:5000/question/${question}`)
    let data = await response.json()
    const chat = document.getElementById("chat")
    chat.innerHTML = `<p><div class="right">${question}</div><br><div class="left">${data["response"]}</div></p>`+chat.innerHTML
}
