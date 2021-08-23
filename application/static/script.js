let ask = async function() {
    question = document.getElementById("question").value
    let response = await fetch(`http://localhost:5000/question/${question}`)
    let data = await response.json()
    const chat = document.getElementById("chat")
    chat.innerHTML = `<p><div class="right">${question}</div><br><div class="left">${data["response"]}</div></p>`+chat.innerHTML
}
