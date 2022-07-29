function registrar_prestamo() {
    activar_botton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            notificacion_success(response.mensaje);
            cerrar_modal_creacion();
        },
        error: function (error) {
            console.log(error);
            notificacion_error(error.responseJSON.mensaje);
            mostrar_erroresCreacion(error);
            activar_botton();

        }
    });
}

