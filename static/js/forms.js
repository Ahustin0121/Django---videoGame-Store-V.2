document.addEventListener("DOMContentLoaded", function() {
    // Si ves este mensaje en la consola (F12), tu archivo está bien conectado
    console.log("Archivo JS de contacto cargado correctamente.");

    const form = document.getElementById('contactForm');

    // Verificamos que el formulario exista antes de agregarle eventos
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita la recarga automática

            let isValid = true;
            const nombre = document.getElementById('nombreInput');
            const correo = document.getElementById('correoInput');
            const mensaje = document.getElementById('mensajeInput');

            // Limpia las alertas rojas previas
            [nombre, correo, mensaje].forEach(input => input.classList.remove('is-invalid'));

            // Valida el Nombre
            if (nombre.value.trim() === '') {
                nombre.classList.add('is-invalid');
                isValid = false;
            }

            // Valida el Correo
            if (correo.value.trim() === '' || !correo.value.includes('@')) {
                correo.classList.add('is-invalid');
                isValid = false;
            }

            // Valida el Mensaje
            if (mensaje.value.trim() === '') {
                mensaje.classList.add('is-invalid');
                isValid = false;
            }

            // Si pasa todas las validaciones
            if (isValid) {
                alert('¡Mensaje enviado con éxito! Nos pondremos en contacto contigo.');
                form.reset(); // Ahora sí limpiamos el formulario
            }
        });
    } else {
        console.error("Error: No se encontró el id 'contactForm' en el HTML.");
    }
});