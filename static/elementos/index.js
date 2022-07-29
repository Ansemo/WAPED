// var $ = jQuery.noConflict();

function listarElementos() {
    $.ajax({
        url: "/Elementos/listado_Elementos/",
        type: "get",
        dataType: "json",
        success: function (response) {
            console.log(response)
            if ($.fn.DataTable.isDataTable('#tabla_elementos')) {
                $('#tabla_elementos').DataTable().destroy();
            }
            $('#tabla_elementos tbody').html("")
            for (let i = 0; i < response.length; i++) {
                let estado = '', estadoinactivo = '';
                if (response[i]['disponivilidad'] == true) {estado += '<span class="badge bg-success">Disponible</span>'}
                if (response[i]['disponivilidad'] == false) {estado += '<span class="badge bg-danger">No disponible</span>'}
                let fila = '<tr>';
                // fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]['numero'] + '</td>';
                fila += '<td>' + response[i]['categoria'] + '</td>';
                fila += '<td>' + response[i]['sub_categoria'] + '</td>';
                fila += '<td>' + response[i]['estado'] + '</td>';
                fila += '<td>' + estado + '</td>';
                // fila += '<td>' + response[i]['imagen'] + '</td>';
                fila += '<td><a href="'+ response[i]['imagen'] +'"  target="_blank" ><img src="' + response[i]['imagen'] + '" height="50px" width="50px" /></a></td>';
                fila += '<td>' + '<button class="btn btn-success" onclick="abrir_modal_edicion(\'/Elementos/actualizar_elemento/' + response[i]['id'] + '/\')"><i class="bi bi-pencil-square"></i></button>\n' +
                    '             <button class="btn btn-danger" onclick="abrir_modal_eliminacion(\'/Elementos/eliminar_elemento/' + response[i]['id'] + '/\')"><i class="bi bi-trash"></i></button>\n';
                fila += '</tr>';
                $('#tabla_elementos tbody').append(fila)
            }
            // <button type="button" className="btn btn-success"><i className="bi bi-check-circle"></i></button>
            $('#tabla_elementos ').DataTable({
                "order": [[ 3, "desc" ]],
                pageLength: 5,
                lengthMenu: [[5, 10, 20, -1], [5, 10, 20, 'Todos']],
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Elementos",
                    infoEmpty: "Mostrando 0 to 0 of 0 Elementos",
                    infoFiltered: "(Filtrado de _MAX_ total Elementos)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Elementos",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin Elementos encontrados",
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
            console.log(error)
        },
    });
}

function registrar_Elemento() {
    activar_botton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            notificacion_success(response.mensaje);
            listarElementos();
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

function editar_Elemento() {
    activar_botton();
    let data = new FormData($('#form_edicion').get(0))
    $.ajax({
        data: data,
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            notificacion_success(response.mensaje);
            listarElementos();
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

function eliminar_Elemento(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
        },
        url: '/Elementos/eliminar_elemento/' + pk + '/',
        type: 'post',
        success: function (response) {
            notificacion_success(response.mensaje);
            listarElementos();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            console.log(error);
            notificacion_error(error.responseJSON.mensaje);
        }
    });
}

function editar_prestamo() {
    activar_botton();
    let data = new FormData($('#form_activar').get(0))
    $.ajax({
        data: data,
        url: $('#form_activar').attr('action'),
        type: $('#form_activar').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            notificacion_success(response.mensaje);
            listarElementos();
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

$(document).ready(function () {
    listarElementos();
});

