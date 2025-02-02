console.log("Connecting.....")
const port = location.protocol === 'https:' ? 'wss': 'ws'
const url = `${port}://${location.host}/notification/`

function connect(){
    const socket = new WebSocket(url)
    // On Message

    socket.addEventListener("message", function(event){

        data = JSON.parse(event.data)
        
        const message = document.querySelector("#message") 
        
        message.classList.remove("hidden")
        
        message.textContent = data
    })

}

document.addEventListener("DOMContentLoaded", connect())