from django.shortcuts import redirect
from juego.models import PartidaModel, OpcionModel
from juego.utils import ganador_partida

class GanadorMixin(object):
    "Valida el ganador de la partida"

    def dispatch(self, request, *args, **kwargs):
        
        try:
            partida=PartidaModel.objects.get(id=kwargs["pk"])
            opciones=OpcionModel.objects.filter(partida=partida)

        except:
            opciones=[]

        if len(opciones)>=3 and partida.estado==False:
            
            opciones_usuario=[]
            for op in opciones.filter(user="adminsuper"):
                opciones_usuario.append(op.opcion)
            
            opciones_maquina=[]
            for op in opciones.filter(user="maquina"):
                opciones_maquina.append(op.opcion)

            #Determinar si hay ganador
            ganador=ganador_partida(opciones_usuario, opciones_maquina)
            
            if ganador[0]==3:#Hay un ganador
                
                partida.estado=True
                partida.ganador=str(ganador[1])
                partida.save()

                return redirect("partida_juego", pk=kwargs["pk"])
            
            elif len(opciones)>=9:#Empate
                partida.estado=True
                partida.ganador=str(ganador[1])
                partida.save()

                return redirect("partida_juego", pk=kwargs["pk"])
            
            else:
                return super().dispatch(request, *args, **kwargs)     

        else:
            return super().dispatch(request, *args, **kwargs)     

