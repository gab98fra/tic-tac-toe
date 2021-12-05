from django.shortcuts import redirect

class AccesoMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
                
        if request.user.is_authenticated:
    
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("api_list")
         