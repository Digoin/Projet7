let ask = async function() {
    let response = await fetch("http://localhost:5000/api/")
    console.log(await response.json())
}
