const url = 'http://127.0.0.1:8000/';
const socket = io('http://127.0.0.1:8000/');
let pokupka = document.getElementById("pokupka");
let stat = document.getElementById("status");
let id = 0;

socket.on('order_completed', function(zak) {
    stat.innerHTML = `<h1>Заказ готов</h1>`;
});

pokupka.onclick = function() {
    stat.innerHTML = `<h1>Заказ готовится</h1>`; 
    console.log("заказ ушел");
    id++;
    console.log(id);
    
    let zakaz = {
        "id": id,
        "product": "Суп"
    };

    axios.post(url, zakaz)
        .then(response => {
            console.log(response.data);
        })
        .catch(error => console.log(error));
};
