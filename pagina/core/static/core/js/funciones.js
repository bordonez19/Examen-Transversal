$(document).ready(function(){
    $("#formulario").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 5
            },
              correo: {
                  required: true,
                  email: true
              },
              contrasena: {
                  required: true,
                  minlength: 8
              },
              telefono: {
                  required: true,
                  minlength: 8
              },
              comentario: {
                  required: true,
                  minlength: 1
              }
        },
        messages: {
            nombre: {
                required: "Ingrese su nombre completo.",
                minlength: "Ingrese al menos 5 caracteres."
            },
              correo: {
                  required: "Ingrese su email",
                  email: "Ingrese un email válido"
              },
              contrasena: {
                    required: "Ingrese una contraseña de 8 carácteres",
                    minlength: "Ingrese contraseña con 8 carácteres"
              },
              telefono: {
                  required: "Ingrese su número de contacto",
                  minlength: "Ingrese a lo menos 8 números"
              },
              comentario: {
                  required: "Ingrese motivo de desuscripción",
                  minlength: "Ingrese a lo menos un comentario"
              }
         }
      });
  });