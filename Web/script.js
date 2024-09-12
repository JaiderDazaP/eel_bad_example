
function changeContent(buttonId) {
    console.log("Botón clickeado:", buttonId);

    // Cambiar el título en la barra superior
    const pageTitle = document.getElementById('page-title');
    pageTitle.innerText = capitalizeFirstLetter(buttonId);

    // Pedir a Eel que cargue el archivo HTML adecuado
    eel.load_page(buttonId)((htmlContent) => {
        console.log("Contenido HTML cargado:", htmlContent);
        const dynamicContent = document.getElementById('dynamic-content');
        dynamicContent.innerHTML = htmlContent;
    });

    // Cambiar el color del botón seleccionado
    const activeButton = document.querySelector('.menu-item.active');
    if (activeButton) {
        activeButton.classList.remove('active'); // Remover la clase activa del botón anterior
    }

    const newActiveButton = document.getElementById(buttonId);
    newActiveButton.classList.add('active'); // Añadir la clase activa al nuevo botón
}


// Función para capitalizar la primera letra del texto
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

window.onload = function() {
    changeContent('dashboard');
}

