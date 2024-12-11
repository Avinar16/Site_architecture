

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('.up').addEventListener('click', function () {
        sendCommand('up');
    });
    document.querySelector('.down').addEventListener('click', function () {
        sendCommand('down');
    });
    document.querySelector('.left').addEventListener('click', function () {
        sendCommand('left');
    });
    document.querySelector('.right').addEventListener('click', function () {
        sendCommand('right');
    });
    document.querySelector('.center').addEventListener('click', function () {
        sendCommand('grab');
    });
    document.getElementById('send_report').addEventListener('click', function () {
        text = document.getElementById('reportTitle').value
        sendReport(text)
    });
    function sendCommand(command) {
        fetch('/manipulator/command/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: command })
        }).then(data => {
            loadGrid();
            console.log('Success');
        }).catch(error => {
            console.error('Error:', error);
        });
    }
    function load_reports_list() {
        fetch('/manipulator/get_reports/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                let report_counter = 1
                data.forEach(element => {

                    const container = document.getElementById('report_div');
                    const reportDiv = document.createElement('div');
                    reportDiv.className = 'report';
                    const reportP = document.createElement('p');
                    reportP.id = 'report_' + report_counter;
                    report_counter++;
                    reportP.innerText = element.fields.name;


                    const reportButton = document.createElement('button');
                    reportButton.className = 'btn';
                    reportButton.innerText = 'LOAD';
                    reportDiv.appendChild(reportP);
                    reportDiv.appendChild(reportButton);
                    container.appendChild(reportDiv);

                    reportButton.addEventListener('click', function () {
                        loadSave(element.fields.name);
                    });

                });


            }).catch(error => {
                console.error('Error:', error);
            });
    }
    function loadSave(name) {
        fetch('/manipulator/load_save/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name})
        }).then(data => {
            loadGrid();
        }).catch(error => {
            console.error('Error:', error);
        });
        
    }
    function sendReport(name) {
        fetch('/manipulator/send_report/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name })
        }).catch(error => {
            console.error('Error:', error);
        });
        load_reports_list();
    }
    function loadGrid() {
        fetch('/manipulator/load')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json(); // или response.text() если ожидается текст
            })
            .then(data => {
                for (let i = 0; i < 256; i++) {
                    const cell = document.getElementById(i);
                    while (cell.firstChild) {
                        cell.removeChild(cell.firstChild);
                    }
                    if (data['data'][i] == "1") {
                        const image = document.createElement('img');
                        image.className = 'cell_img'
                        image.src = './images/crate.png';
                        image.alt = '1';
                        cell.appendChild(image);
                    }
                    else if (data["data"][i] == "m") {
                        const image = document.createElement('img');
                        image.className = 'cell_img'
                        image.src = '/images/manipulator.png';
                        image.alt = 'm';
                        cell.appendChild(image);
                    }
                }
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }
    loadGrid();
    load_reports_list();
});