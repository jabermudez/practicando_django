var $ = jQuery.noConflict();  
function listadoUsuarios(){
      
    $.ajax({
        url:"/usuarios/listado_usuarios/",
        type:"get",
        dataType:"json",
        success:function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    listadoUsuarios()
});