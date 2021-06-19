num=20
nombre="Ana"
print(num,type(num))
print(nombre,type(nombre))
def mensaje(ubo):
    print(ubo)
mensaje("giig")
class sintaxis:
    instancia=0
    def __init__(self,dato="llamando al constructor"):
        self.frase=dato
        sintaxis.instancia=sintaxis.instancia+1

ejer1 = sintaxis()
print(sintaxis.instancia)
ejer2 = sintaxis()
print(ejer1.frase)