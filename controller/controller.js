//var ipaddr = document.getElementById('rec-id').innerHTML
//var socket = io.connect( ipaddr );

var socket = io.connect("10.0.0.43:5000")

socket.on("connect", function() {
  socket.emit("message", "Client connected")
});

document.getElementById("right").addEventListener("click",function(){
  socket.emit("button", "255");
})
document.getElementById("left").addEventListener("click",function(){
  socket.emit("button", "-255");
})
