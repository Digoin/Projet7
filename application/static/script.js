let ask = async function() {
    let response = await fetch("http://localhost:5000/question/5+avenue+anatole+france")
    console.log(await response.json())
}
