var socket = io.connect("ws://192.168.1.167:5000");

socket.on('connect', function() {
  socket.emit('message', 'Client connected')
});

document.getElementById('right').addEventListener('click',function(){
  socket.emit('controller move', "right");
})
document.getElementById('left').addEventListener('click',function(){
  socket.emit('controller move', "left");
})
