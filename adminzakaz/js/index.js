const socket = io('http://127.0.0.1:8000/');
const url = 'http://127.0.0.1:8000/complete_order';

socket.on('new_order', function(data) {
    let orderlist = document.getElementById("order");
    let orderItem = document.createElement("div");
    orderItem.setAttribute("id", `order-${data.id}`);
    
    orderItem.innerHTML = `
        <p>Номер заказа: ${data.id}, Заказ: ${data.product}</p>
        <button id="btn-${data.id}">Заказ готов</button>
    `;
    orderlist.appendChild(orderItem);

    document.getElementById(`btn-${data.id}`).onclick = function() {
        document.getElementById(`order-${data.id}`).remove();

        axios.post(url, { "id": data.id })
            .then(function (response) {
                console.log(response.data.message);
            })
            .catch(function (error) {
                console.error(error);
            });
    };
});
