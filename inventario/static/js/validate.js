$("#form_categoria").validate({
    rules:{
        nombre_cat:{
            required:true,
        },
        descripcion_cat:{
            required:true,
        }
    },
    messages:{
        nombre_cat:{
            required:"Por favor, ingrese alguna categoria",
        },
        descripcion_cat:{
            required:"Por favor, ingrese alguna descripción",
        }
    },
});