// this prevent the form to reload the page when you focus it and press enter
var input = document.getElementById("question");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("validate").click();
    }
});

// this function is the main of the page and have multiple uses
let ask = async function() {
    question = document.getElementById("question").value
    const chat = document.getElementById("chat")

    // we put a loader when grandpy is loading the response
    chat.innerHTML = `<p class="left, loader" id=loader></p><p class="right">${question}</p>`+chat.innerHTML

    // the function call the question function from views.py
    let response = await fetch(`https://powerful-plateau-08757.herokuapp.com/question/${question}`)
    let data = await response.json()

    // we remove the loader
    let loader = document.getElementById("loader")
    loader.classList.remove("loader")

    // there we get rid of the loader and put the repsonse of the api
    chat.innerHTML = `<p class="left">${data["response"]}</p>`+ chat.innerHTML

    // we call the function of google maps API
    if (data["map"] === true) {
        chat.innerHTML = `<div id="map"></div>` + chat.innerHTML
        initMap(data["latitude"], data["longitude"])
    }
}


// this part is a code gave by google the google maps API to display a map
let map;

function initMap(latitude, longitude) {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: latitude, lng: longitude },
        zoom: 16,
  });
}