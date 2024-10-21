const url = 'http://127.0.0.1:8000/';
let pokupka = document.getElementById("pokupka");
let id = 0

pokupka.onclick = function() {
    console.log("заказ ушел");
    id++;
    console.log(id)
    let zakaz = {
        "id": id,
        "product": "Суп"
    };
    axios.post(url, zakaz)
        .then(response => {
            console.log(response.data)
            alert(response.data.message)
            res = response.data.data.product
            alert(`${res} скоро будет готов`)
        })
        .catch(error => console.log(error))
};
