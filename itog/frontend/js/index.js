const url = 'http://127.0.0.1:8000/';
let pokupka = document.getElementById("pokupka");

let zakaz = {
    "product": "Суп"
};

pokupka.onclick = function() {
    console.log("заказ ушел");
    axios.post(url, zakaz)
        .then(response => console.log(response.data))
        .catch(error => console.log(error));
};
