function listarUsuarios() {
    $.ajax({
        url: "/listado_usuarios/",
        type: "get",
        dataType: "json",
        success: function (response) {
            if ($.fn.DataTable.isDataTable('#tabla_usuario')) {
                $('#tabla_usuario').DataTable().destroy();
            }
            $('#tabla_usuario tbody').html("")
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]['fields']['username'] + '</td>';
                fila += '<td>' + response[i]['fields']['nombres'] + '</td>';
                fila += '<td>' + response[i]['fields']['apellidos'] + '</td>';
                fila += '<td><a href="/media/' + response[i]['fields']['imagen'] + '"  target="_blank" ><img src="/media/' + response[i]['fields']['imagen'] + '" height="50px" width="50px" /></a></td>';
                fila += '<td>' + response[i]['fields']['email'] + '</td>';
                fila += '<td>' + response[i]['fields']['email'] + '</td>';
                fila += '<td>' + '<button class="btn btn-success" onclick="abrir_modal_edicion(\'/actualizar_usuarios/' + response[i]['pk'] + '/\')"><i class="bi bi-pencil-square"></i></button>\n' +
                    '             <button class="btn btn-danger" onclick="abrir_modal_eliminacion(\'/eliminar_usuarios/' + response[i]['pk'] + '/\')"><i class="bi bi-trash"></i></button>\n';
                fila += '</tr>';
                $('#tabla_usuario tbody').append(fila)
            }

            $('#tabla_usuario').DataTable({
                pageLength: 5,
                lengthMenu: [[5, 10, 20, -1], [5, 10, 20, 'Todos']],
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de _MAX_ total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                        first: "Primero",
                        last: "Ultimo",
                        next: "Siguiente",
                        previous: "Anterior",
                    },
                },

            });

        },
        error: function (error) {

        },
    });
}

function registrar_usuario() {
    activar_botton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            notificacion_success(response.mensaje);
            listarUsuarios();
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

function editar_usuario() {
    activar_botton();
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            notificacion_success(response.mensaje);
            listarUsuarios();
            cerrar_modal_dicion();
        },
        error: function (error) {
            console.log(error);
            notificacion_error(error.responseJSON.mensaje);
            mostrar_erroresEdicion(error);
            activar_botton();

        }
    });
}

function eliminar_usuario(pk) {
    // console.log($("[name='csrfmiddlewaretoken']").val())
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
        },
        url: '/eliminar_usuarios/' + pk + '/',
        type: 'post',
        success: function (response) {
            notificacion_success(response.mensaje);
            listarUsuarios();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            console.log(error);
            notificacion_error(error.responseJSON.mensaje);
        }
    });
}


$(document).ready(function () {
    listarUsuarios();
});

