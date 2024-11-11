document.getElementById('fetchButton').addEventListener('click', () => {
    fetch('/api')
        .then(response => {
            if (!response.ok) {
                throw new Error('Сетевая ошибка при получении данных.');
            }
            return response.json();
        })
        .then(data => {
        document.getElementById('paragraph').textContent = data.body;
        console.log(data.body);
        })
});



function loadData(){
    const textarea = document.getElementById('myTextarea');

    const data = textarea.value;
    console.log(data);
    const options = {
        method: 'POST', // Метод запроса
        headers: {
            'Content-Type': 'application/json' // Указываем тип содержимого
        },
        body: JSON.stringify(data) // Преобразуем данные в строку JSON
    };
    return options
}

document.getElementById('sendButton').addEventListener('click', () => {
    const options = loadData();
    fetch('/api', options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Сетевая ошибка при получении данных.');
            }
            console.log('post');
            return response.json();
        })
});