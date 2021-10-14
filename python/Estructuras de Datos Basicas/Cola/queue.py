"""
    QUEUE = COLA
    Algoritmo: FIFO = First In First Out = Primero en entrar Primero en salir
    Breve explicacion:
        Si eres de aquellos que alguna vez se tuvo que formar para ir a comprar tortillas, aqui aplica el mismo procedimiento, el primero que llegue se le desapacha primero y sale de la fila.

    La cola requiere 2 punteros, el primero debe ser igual a la posicion del primer elemento en la cola, y otro puntero para el ultimo elemento, de esta forma tenemos un rastro para saber quien llego primero y quien despues.

    De forma similar al stack, lo haremos sin clases, para que sea facil comprender despues.
"""
# Creamos la colita
def crear_cola():
    cola = []
    return cola

# Se forma el primer cliente en la cola
# No se me ocurrio un nombre para el metodo en Espanol xd.
def encolar(cola, elemento):
    cola.append(elemento)
    return "Se formo: " + str(elemento)

# Salir de la cola, es decir ya te despacharon
def desencolar(cola):
    if len(cola) < 1:       # Si no hay nadie en la cola
        return "No hay nadie :v"
    

    return print("Adios", cola.pop(0))      # Se va el primero en formarse.

# Mostrando la colita 7uu7
def mostrar(cola):
    print("Mira mi colita: ", cola)

# Largo de mi cola :v
def largo(cola):
    print("Mi cola tiene: ", len(cola), " elementos.")

def main():

    # Formamos a la gente para las tortillas
    print("#######################################")
    print("##### TORTILLERIA EL PROGRAMER :V #####")
    print("#######################################")
    print("") 
    mi_colita = crear_cola()        # Se crea la colita

    encolar(mi_colita, "Ramon")
    encolar(mi_colita, "Jenny")
    encolar(mi_colita, "Perico")
    encolar(mi_colita, "Pablo")

    largo(mi_colita)                # Largo de mi colita 7uu7
    mostrar(mi_colita)              # Mostramos mi colita

    desencolar(mi_colita)                    # Se va ramon, ya que llego 1ro.

    mostrar(mi_colita)    

    return True

# Prevenir ejecucion de linea arriba sin estar en una fuc.
if __name__ == "__main__":
    main()

