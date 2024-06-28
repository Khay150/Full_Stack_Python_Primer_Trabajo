
(function(){

    var formulario = document.getElementsByName('formulario')[0];

    var validarNombre = function(e){
        if (formulario.nombre.value == 0){
            alert("Completa el campo nombre");
            e.preventDefault();
            }
            else{
                if (formulario.nombre.value.length > 20){
                    alert("Nombre extenso");
                    e.preventDefault();
                    }
            }
        };

    var validarApellido = function(e){
        if (formulario.apellido.value == 0){
            alert("Completa el campo apellido");
            e.preventDefault();
            }
            else{
                if (formulario.nombre.value.length > 20){
                    alert("apellido extenso");
                    e.preventDefault();
                    }
            }
        };    

        var validarMail = function(e){
            var mail_ingresado = formulario.mail.value;
            if (mail_ingresado == 0){
                alert("Ingrese un mail valido");
                e.preventDefault();
                }
            var mail_arroba = false;
            var mail_dominio = false;
            for (var i = 0; i < mail_ingresado.length; i++) {
                if (mail_ingresado[i] == "@" && i != 0) {
                    mail_arroba = true;
                }
                else if (mail_ingresado[i] == "." && mail_arroba && i < (mail_ingresado.length-1)){
                    mail_dominio = true;
                }
            }
            if (!mail_arroba || !mail_dominio) {
                alert("Ingrese un mail valido");
                e.preventDefault();
            }
            else{
                if (c > 50){
                    alert("apellido extenso");
                    e.preventDefault();
                    }
                }
            };    

    var validarRadio = function(e){
        if (formulario.sexo[0].checked == true ||
            formulario.sexo[1].checked == true || formulario.sexo[2].checked == true){
        }
        else{
            alert("Completa el campo sexo");
            e.preventDefault();
            }
        };

    var validarCheckbox = function(e){
        var chequeado = false;
        for (var i = 0; i < 6; i++) {
            if (formulario.asunto[i].checked == true){
                chequeado = true
            }
        }
        if (chequeado == false) {
            alert("Seleccione su asunto");
            e.preventDefault();
            }
        };

    var validarTextbox = function(e){
        var texto = formulario.mensaje.value;
        if (texto.trim() == ""){
            alert("Agregue su mensaje");
            e.preventDefault();
            }
        };

    var validar = function(e){
        validarNombre(e);
        validarApellido(e);
        validarMail(e);
        validarRadio(e);
        validarCheckbox(e);
        validarTextbox(e);
    };
    formulario.addEventListener("submit", validar);
}())