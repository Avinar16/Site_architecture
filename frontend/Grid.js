document.addEventListener("DOMContentLoaded", function() {
    const gridContainer = document.getElementById('grid');
    for (let i = 0; i < 256; i++) {
        
        const cell = document.createElement('div');
        cell.className = 'cell';
        cell.id = i;
        cell.dataset.row = i % 16;
        cell.dataset.col = Math.floor(i / 16);


        gridContainer.appendChild(cell);
        
    }
});
