var $ = jQuery.noConflict();  
function listadoUsuarios(){      
    $.ajax({
        url:"/usuarios/listado_usuarios/",
        type:"get",
        dataType:"json",
        success: function(response){
            $('#tabla_usuarios tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1 ) + '</td>';
                fila += '<td>' + response[i]['username'] + '</td>';
                fila += '<td>' + response[i]['nombres'] + '</td>';   
                fila += '<td>' + response[i]['apellidos'] + '</td>';  
                fila += '<td>' + response[i]['email'] + '</td>';  
                fila += '<td> <button>Editar</button><button>Eliminar</button> </td>';         
                fila += '</tr>';
                $('#tabla_usuarios tbody').append(fila);
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