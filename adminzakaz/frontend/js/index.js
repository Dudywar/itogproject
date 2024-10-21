const socket = io('http://127.0.0.1:8000/');

socket.on('new_order', function(data) {
    let orderlist = document.getElementById("order");
    let order = document.createElement("<p></p>");
    order.textContent = `Номер заказа: ${data.id}, Заказ: ${data.product}`;
    orderlist.appendChild(order);
});