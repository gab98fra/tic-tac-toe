import random as rd

OPCIONES=[1,2,3,4,5,6,7,8,9]

def opcion_maquina(opciones_seleccionadas):
    "Retorna una opción máquina de manera aleatoria"
    
    #Opciones seleccionadas
    op_seleccionadas=[]
    for op in opciones_seleccionadas:
        op_seleccionadas.append(op.opcion)
    
    #Opciones disponibles
    opciones_disponibles=[]
    for op in OPCIONES: # Recorrer todas las opciones_disponibles

        if op in op_seleccionadas: # Continuar
            pass
        else: # Si no se encuentra agregar a la lista vacía
            opciones_disponibles.append(op)

    #Escoger un número aleatorio
    if len(opciones_disponibles)>=1:
        resultado=rd.choice(opciones_disponibles)

        return resultado
    
    return None

#Combinaciones ganadoras
#Horizontal
GANADOR1=[1,2,3]
GANADOR2=[4,5,6]
GANADOR3=[7,8,9]
#Vertical
GANADOR4=[1,4,7]
GANADOR5=[2,5,8]
GANADOR6=[3,6,9]
#Diagonales
GANADOR7=[1,5,9]
GANADOR8=[7,5,3]

def ganador_partida(opciones_usuario, opciones_maquina):
    "Determina el ganador de la partida"
    
    # ---------------Usuario-----------------------
    contador=0
    for op in range(len(opciones_usuario)):
        if opciones_usuario[op] in GANADOR1:#Si se encuentra en la lista
    
            user="admin"    
            contador=contador +1
                    
        if contador==3: # Ganador
            
            return [contador, user]
    
    contador=0
    for op in range(len(opciones_usuario)):

        if opciones_usuario[op] in GANADOR2:#Si se encuentra en la lista
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_usuario)):
        
        if opciones_usuario[op] in GANADOR3:#Si se encuentra en la lista
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_usuario)):
        
        if opciones_usuario[op] in GANADOR4:#Si se encuentra en la lista
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_usuario)):

        if opciones_usuario[op] in GANADOR5:
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_usuario)):

        if opciones_usuario[op] in GANADOR6:
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_usuario)):
        
        if opciones_usuario[op] in GANADOR7:
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_usuario)):
        
        if opciones_usuario[op] in GANADOR8:
            
            user="admin"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    # ---------------Máquina-----------------------
    contador=0
    for op in range(len(opciones_maquina)):
        
        if opciones_maquina[op] in GANADOR1:#Si se encuentra en la lista
    
            user="maquina"    
            contador=contador +1
                    
        if contador==3: # Ganador
            
            return [contador, user]        

    contador=0
    for op in range(len(opciones_maquina)):

        if opciones_maquina[op] in GANADOR2:#Si se encuentra en la lista
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_maquina)):
        
        if opciones_maquina[op] in GANADOR3:#Si se encuentra en la lista
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_maquina)):
        
        if opciones_maquina[op] in GANADOR4:#Si se encuentra en la lista
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_maquina)):

        if opciones_maquina[op] in GANADOR5:
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_maquina)):

        if opciones_maquina[op] in GANADOR6:
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_maquina)):
        
        if opciones_maquina[op] in GANADOR7:
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

    contador=0
    for op in range(len(opciones_maquina)):
        
        if opciones_maquina[op] in GANADOR8:
            
            user="maquina"
            contador=contador +1
            
        if contador==3: # Ganador
            
            return [contador, user]

        else:
            return [0, "EMPATE"]


