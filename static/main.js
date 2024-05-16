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

