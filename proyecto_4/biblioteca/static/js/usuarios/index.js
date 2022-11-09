var $ = jQuery.noConflict();  
function listadoUsuarios(){      
    $.ajax({
        url:"/usuarios/listado_usuarios/",
        type:"get",
        dataType:"json",
        success: function(response){
            $('#tabla_usuarios').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1 ) + '</td>';
                fila += '<td>' + response[i]["fields"]['username'] + '</td>';
                fila += '<td>' + response[i]["fields"]['nombres'] + '</td>';
                fila += '<td>' + response[i]["fields"]['apellidos'] + '</td>';
                fila += '<td>' + response[i]["fields"]['email'] + '</td>';
                fila += '<td> <button>EDITAR </button><button>ELIMINAR</button> </td>';                
                fila += '</tr>';
                $('#tabla_usuarios').append(fila);
            }
            $('#tabla_usuarios').DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando START a END de TOTAL Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de MAX total entradas)",
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
        error: function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    listadoUsuarios();
});