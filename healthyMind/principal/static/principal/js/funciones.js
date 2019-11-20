//global

$(document).ready(function(){
    $('#mensajeF').hide();
})


$(document).ready(function(){

    $('.proximamente').click(function(){
        alert('Sección disponible en la proxima versión.');
    })
})


//-------Validacion Registro jQuery----------

  //global

var error = document.getElementById('mensajeF');

function validarEmail(mail)
    {


        var expr = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/);
        if($('#txtEmail').val() == '')
            {
                error.innerHTML='';
                $('#btn').click(function(){$('#mensajeF').show().fadeIn(5000)});
                messageErrors('Campo Email vacio');
                return false;


            }else if(expr.test(mail)==false)

            {
                error.innerHTML='';
                $('#btn').click(function(){$('#mensajeF').show()});
                messageErrors('Por favor, ingrese un mail correcto.');
               return  false;
            }

        if (mail != '' && expr.test(mail)==true)
        {
            return true;
        }
    }





function messageErrors(message)
{

    error.innerHTML += '<li> Error :' + message + '</li>';

}



//Main


    $('#btn').click(function(e){

    var mail= $('#txtEmail').val(),
        pass = $('#txtPassword').val();

        //Condiciones
    if(pass=='')
       {
         error.innerHTML='';
         messageErrors('Campo Contraseña Vacio');
       }

       if(validarEmail(mail)==true && pass!='')
           {
                 $('#btn').click(function(){

                    $('#formulario').submit();
                     alert('Registro Completado');
                 });

           }else{
               e.preventDefault();
           }
    })

/*$(document).ready(function(){


    $('#btn').click(function(e){
        var mail = $('#txtEmail').val(),
            formulario= $('#formulario').val(),
            pass= $('#txtPassword').val();


        console.log(mail);

        $('#btn').submit();
        e.preventDefault();

    })



})*/
