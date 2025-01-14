const port = location.protocol === 'https:' ? 'wss': 'ws'
const url = `${port}://${location.host}/notification/`

function connect(){
    const socket = new WebSocket(url)
    // On Message
    socket.addEventListener("message", function(event){
        console.log(event.type)
        console.log("SERVER ", event.data)
        data = JSON.parse(event.data)
        const message = document.querySelector("#message") 
        message.classList.remove("hidden")
        message.textContent = data
        setInterval(()=>{
            message.classList.add("hidden")
        }, 10000)
    })

}

document.addEventListener("load", connect())