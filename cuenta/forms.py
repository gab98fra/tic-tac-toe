from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    """Formulario Iniciar sesión


        :AuthenticationForm: Formulario de autenticación interna django
    """
    
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Usuario'
        self.fields['username'].widget.attrs['maxlength']=30
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
        self.fields['password'].widget.attrs['maxlength']=30


