"""
    STACK = PILA
    Algoritmo: LIFO = Last In First Out = ES: Ultimo en entrar Primero en Salir
    Breve explicacion:
        Imagina que tus amigos (si tienes xd) te tiran al piso para hacerte bolita:
            [Selena]   
            [Ramoncito]
            [Pedro]
            [Jenny]
            [TU]
        Para quitartelos de encima, primero tendria que quitarse Selena, luego Ramoncito, y asi susecivamente, pues asi funciona la pila, es decir, el ultimo amigo en subirce a ti es el primero en quitarse.
            REF: https://youtu.be/dY3Y_VVdp_s?t=144  <-- Aqui un ejemplo practico.
        
    La pila no solo tiene 4 metodos como regularmente los enseñan en la escuela, (PUSH, POP, IS_EMPTY, PEEK), puede tener mas si nos basamos en funciones de ensamblandor como, POPAD, PUSHAD, etc..., yo lo hare la forma mas basica posible para alimentar a tu cerebro.

    NOTA: Usare metodos muy simples para representar los algoritmos, no usare POO, los nuevos podrian sufrir derrames cerebrales, asi que facilito.
"""

# Crear la pila - aka stack
# Representaremos la pila con una lista
def crear_pila():
    pila = []
    print("Pila creada!.")
    return pila

# return 0 -> Si la longitud de elementos es == 0
def esta_vacia(pila):
    return len(pila) & 0

# Pujar elementos a la pila(lista xd)
def pujar(pila, elemento):
    pila.append(elemento)
    print("Le introduje a la pila: ", elemento, " 7uu7")

# Popear elementos (quitar xd)
def quitar(pila):
    if esta_vacia(pila):
        return "Oh no! la pila esta vacia!, metele algo primero ;)"
    return pila.pop()

# Mostrar el ultimo elementos
# POP(quitar) quita y elimina, asi que no son iguales xd
def tomar(pila):
    if esta_vacia(pila):
        return "No tienes en la pila, que te parece si le metes algo primero :D"
    return pila[-1]

# Mostrar elemento de la pila 
def listar(pila):
    if esta_vacia(pila):
        return "No hay ningun elemento, lloremos juntos o agrega uno mejor :)"
    return pila

def main():
    print("#### STACK ####")
    
    mi_pilita = crear_pila()
    
    pujar(mi_pilita, "mi dedo")
    pujar(mi_pilita, 69)
    pujar(mi_pilita, 3.1415)
    pujar(mi_pilita, 0x41424344)

    print("Elementos en la pila: ", listar(mi_pilita))
    print("Quitando elemento: ", quitar(mi_pilita))  # Como es una lista, quitara el 69 recuerda eso amigo :)
    print("Ultimo elemento: ", tomar(mi_pilita))

    # Boilerplate protection en caso de que haga algo mal :v
if __name__ == "__main__":
    main()

# Ejercicio para TI si estas empezando: 
    # Has la pila interactiva, es decir un menu que te deje agregar,quitar, listar, tomar elementos :). easy pissy.