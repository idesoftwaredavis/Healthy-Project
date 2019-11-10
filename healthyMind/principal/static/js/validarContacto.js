$(document).ready(function(){
    
    $('.proximamente').click(function(){
        alert('Sección disponible en la proxima versión.');
    })
})



(function(){
    var formulario = document.getElementById('formulario'),
        nombres = formulario.txtNombre,
        apellidos = formulario.txtApellidos,
        correo = formulario.txtEmail,
        terminos = formulario.terminos,
        error = document.getElementById('error');
    
    var combo = document.getElementById('combobox');



function validarNombre(e)
{
    if(nombres.value == "")
    {
       console.log('Nombre Obligatorio'); 
       error.style.display='block';
       error.innerHTML += '<li>Por favor completa el nombre</li>'
       e.preventDefault();
    }else
    {
        error.style.display= 'none';
    }
}
    
    
function validarApellido(e)
{
    if(apellidos.value == "")
    {
       console.log('Nombre Obligatorio'); 
       error.style.display='block';
       error.innerHTML += '<li>Por favor completa el apellido</li>'
       e.preventDefault();
    }else
    {
        error.style.display= 'none';
    }
}

 
function validarCorreo(e)
{
    validar = new RegExp(/^\w+([\.\+\-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/);
    //condicion
     if(correo.value == "")
    {
       console.log('Por favor completa el correo'); 
       error.style.display='block';
       error.innerHTML += '<li>Por favor completa el correo</li>'
       e.preventDefault();
    }else
    {
        error.style.display='none';
    }
    
    if (validar.test(correo.value)==false)
        {
            error.style.display='block';
            error.innerHTML += '<li>Por favor ingrese un correo valido</li>'
            e.preventDefault();
        }else
            {
                error.style.display='none';
            }
}


    
function validarSexo(e)
{
   if(sexo.value=="" || sexo.value ==null)
    {
         console.log('porfavor completa el sexo');
        error.style.display='block';
        error.innerHTML += '<l1>Por favor completa el correo </li>'
        
        e.preventDefault();
    }
    else
        {
            error.style.display='none';    
        }
}

function validarTerminos(e)
{
    if(terminos.checked == false)
        {
            
         console.log('Es necesario aceptar los terminos y condiciones');
         error.style.display='block';
         error.innerHTML += '<l1>Por favor completa las condiciones  </li>'

        e.preventDefault();
        }
}
    
    
    function combobox(e){
        if(combo.selectedIndex==0)
            {
                error.style.display='block';
                error.innerHTML += '<li>Por favor ingrese un elemento  </li>'
                e.preventDefault();
            }else if (combo.selectedIndex!=0)
                {
                    error.style.display='none';
                }
        
        
       
    }

function validarFormulario(e)
{
    error.innerHTML = '';
    validarNombre(e);
    validarApellido(e);
    validarCorreo(e);
    validarTerminos(e);
    combobox(e);
}
formulario.addEventListener('submit', validarFormulario);
}())



