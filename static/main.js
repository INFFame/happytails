// Evento eye para signin y signup
document.addEventListener('DOMContentLoaded', function() {
    // Selecciona todos los campos de contraseña y los iconos de alternar contraseña
    const passwordFields = document.querySelectorAll('.form__icon input[type="password"]');
    const passwordToggles = document.querySelectorAll('.form__icon .bi');

    // Agrega un evento de clic a cada icono de alternar contraseña
    passwordToggles.forEach((toggle, index) => {
        toggle.addEventListener('click', function() {
            // Encuentra el campo de contraseña asociado al icono de alternar contraseña actual
            const passwordField = passwordFields[index];
            // Alterna entre mostrar y ocultar la contraseña
            if (passwordField.type === 'password') {
                passwordField.type = 'text'; // Muestra la contraseña
                toggle.classList.remove('bi-eye-slash-fill'); // Cambia el icono al icono de ojo cerrado
                toggle.classList.add('bi-eye-fill');
            } else {
                passwordField.type = 'password'; // Oculta la contraseña
                toggle.classList.remove('bi-eye-fill'); // Cambia el icono al icono de ojo abierto
                toggle.classList.add('bi-eye-slash-fill');
            }
        });
    });
});



function actualizarHorarios() {
    // Obtener el elemento select de los veterinarios
    const selectVeterinario = document.getElementById('veterinario');
    // Obtener el valor seleccionado del veterinario
    const veterinarioId = selectVeterinario.value;
    
    // Obtener el valor seleccionado de la fecha
    const fechaSeleccionada = document.getElementById('fecha').value;

    // Verificar si se seleccionó un veterinario y una fecha
    if (veterinarioId && fechaSeleccionada) {
        // Crear un objeto FormData para enviar datos al servidor
        const formData = new FormData();
        formData.append('veterinario_id', veterinarioId);
        formData.append('fecha', fechaSeleccionada);
        
        // Enviar una solicitud POST al servidor
        fetch('/agendar_hora/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al obtener horarios: ' + response.statusText);
            }
            return response.text(); // Obtener los horarios como texto
        })
        .then(data => {
            // Actualizar los horarios disponibles en el formulario
            const selectHorario = document.getElementById('id_horario_disponible');
            selectHorario.innerHTML = data; // Insertar los horarios directamente como HTML
        })
        .catch(error => console.error(error));
    }
}
