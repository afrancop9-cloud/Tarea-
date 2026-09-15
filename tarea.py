# Ejercicio 1 validor de notas con promedio,
class calificador:
    def _init_(self):
        self.notas=[]
        def validar_notas(self,nota):
            return 0 <= nota <= 100
        def cargar_notas(self, *args):
            for nota in args:
                if self.validar_notas(nota):
                   self.notas.append(nota)
                return self.nota
            def promedio (self):
                if len(self.notas) ==0:
                    return 0 
                return sum(self.notas)/ len(self.notas)

        cal= calificador()
        cal.cargar_notas(40,60,80,20)
        print(cal.notas)
        print(cal.promedio())
