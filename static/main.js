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

document.addEventListener('DOMContentLoaded', function() {
    var popoverTrigger = document.getElementById('avatar-button');
    var popover = new bootstrap.Popover(popoverTrigger, {
        content: document.getElementById('popover-content').innerHTML,
        html: true,
        placement: 'bottom',
        trigger: 'click'
    });

    document.addEventListener('click', function (e) {
        if (!popoverTrigger.contains(e.target) && !document.querySelector('.popover')?.contains(e.target)) {
            popover.hide();
        }
    });
});





document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submit-btn').addEventListener('click', function(event) {
        event.preventDefault(); // Evita el envío predeterminado del formulario
        
        // Realiza validaciones adicionales si es necesario
        if (formIsValid()) {
            // Muestra un mensaje de éxito con SweetAlert2
            Swal.fire({
                icon: 'success',
                title: '¡La hora ha sido tomada correctamente!',
                showConfirmButton: true,
                // timer: 20000 // Tiempo en milisegundos (1.5 segundos)
            }).then((result) => {
                if (result.isConfirmed) {
                    // Envía el formulario si el usuario hace clic en "OK"
                    document.getElementById('agenda-form').submit();
                    window.location.href = '/';
                }
            });
        }
    });

    // Función para validar el formulario
    function formIsValid() {
        // Aquí puedes realizar validaciones adicionales si es necesario
        // Por ejemplo, validar que la fecha de la cita no sea anterior a hoy
        var fechaCitaInput = document.getElementById('id_fecha_cita');
        var fechaCita = new Date(fechaCitaInput.value);
        var hoy = new Date();
        
        if (fechaCita < hoy) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'La fecha de la cita no puede ser anterior a la fecha actual.',
            });
            return false;
        }

        // Aquí puedes agregar más validaciones según tus requerimientos

        return true; // Retorna true si todas las validaciones pasan
    }
});