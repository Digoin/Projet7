var input = document.getElementById("question");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("validate").click();
    }
});

let ask = async function() {
    question = document.getElementById("question").value
    const chat = document.getElementById("chat")
    chat.innerHTML = `<p class="right">${question}</p>`+chat.innerHTML
    chat_save = chat.innerHTML
    chat.innerHTML = `<img class="dots" src="static/image/3dots.gif">`+chat_save
    try {let response = await fetch(`http://localhost:5000/question/${question}`)}
    catch (error) {
        console.error(error)
    }
    let data = await response.json()
    chat.innerHTML = `<p class="left">${data["response"]}</p>`+ chat_save
    chat.innerHTML = `<div id="map"></div>` + chat.innerHTML
    initMap(data["latitude"], data["longitude"])
}

let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
  });
}