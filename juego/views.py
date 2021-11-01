from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from juego.models import PartidaModel, OpcionModel
from juego.utils import opcion_maquina
from juego.mixins import GanadorMixin, ganador_partida

class HomeView(TemplateView):
    """Pagina principal: después de iniciar sesión
    

        :TemplateView: vista django basado en clases
    """

    template_name="juego/index.html"
    model=PartidaModel

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        "Se crea la partida de juego"

        partida=self.model.objects.create(user=request.user)
        partida.save()
        return redirect("partida_juego", pk=partida.id)

class JuegoView(View):
    """Juego en curso


        :View: Vista django basado en clases
    """
    
    template_name="juego/juego.html"
    model=OpcionModel

    def get_queryset_opcion(self, id):
        "Retorna las opciones seleccionadas por partida"

        try:
            data=self.model.objects.filter(partida=id)
                    
        except:
        
            data=None
        
        return data
    
    def get_queryset_ganador(self, opciones, partida):
        "Determina si hay un ganador"

        opciones_usuario=[]
        for op in opciones.filter(user="admin"):
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
            
        elif len(opciones)>=9:#Empate
            partida.estado=True
            partida.ganador=str(ganador[1])
            partida.save()


    def get_queryset(self, id):
        "Retorna la partida"

        partida=PartidaModel.objects.get(id=id)

        return partida

    def get(self, request, *args, **kwargs):
        
        #Opciones seleccionadas por partida
        data_opcion=self.get_queryset_opcion(kwargs["pk"])
        
        #Opciones seleccionadas
        opcion={"id_partida":kwargs["pk"]}
        if data_opcion: #Si ya existe registros en la partida

            #Opción máquina:
            opcion_maq=opcion_maquina(data_opcion)
            partida=self.get_queryset(kwargs["pk"])
            if opcion_maq:
                opcion_seleccionada=self.model.objects.create(opcion=int(opcion_maq), user="maquina", partida=partida)
                opcion_seleccionada.save()

            # Todas las opciones seleccionadas
            for op in self.get_queryset_opcion(kwargs["pk"]): 
                opcion["a" + str(op.opcion)]=str(op.user)
            
            # Determinar si hay un ganador
            if len(data_opcion)>=4 and partida.estado==False:
                self.get_queryset_ganador(data_opcion, partida)

            #Parametros de Ganador
            opcion["ganador"]=str(partida.ganador)
            opcion["estado"]=partida.estado

        return render(request, self.template_name, opcion)

    def post(self, request, *args, **kwargs):

        #Partida
        data=request.POST.get("opcion")
        partida=self.get_queryset(kwargs["pk"])
        
        #Opción usuario
        opcion_seleccionada=self.model.objects.create(opcion=int(data), user=str(request.user), partida=partida)
        opcion_seleccionada.save()

        return redirect("partida_juego", pk=kwargs["pk"])

class EstadisticasView(ListView):
    """Resultados de las partidas


        :ListView:Vista django basado en clases
    """

    template_name="juego/estadisticas.html"
    model=PartidaModel
    context_object_name="estadisticas"
    