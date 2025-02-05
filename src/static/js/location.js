console.log("Hello from location.js")

navigator.geolocation.getCurrentPosition((position)=>{
    const {latitude, longitude} = position.coords
    console.log(latitude, longitude)
    if(!localStorage.getItem("location")){
        fetchLocation(latitude, longitude)
    }else{
        let country = localStorage.getItem("location")
        document.getElementById("location").textContent = country       
    }
}, (error)=>{
    console.log(error)
})

function fetchLocation(latitude, longitude){
    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`)
    .then(response=> response.json())
    .then(data=>{
        console.log(data)
        const country = data.address?.country
        document.getElementById("location").textContent = country
        localStorage.setItem("location", country)
    })
    .catch(error=>{
        console.error(error)
    })
}