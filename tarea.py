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
# ejercicio 2 contar palabras unicas
class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())

# Ejercicio 3. gestor de compras  con totales.
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)

        return resultado
c = CarroCompras()

c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)

print(c.total_carrito())
print(c.articulos_por_rango(2.00, 2.80))
# Ejercicio 4.
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida

        return resultado
inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5, 6]))
# Ejercicio 5.
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        return {
            'pares': self.pares,
            'impares': self.impares
        }

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())
# Ejercicio 6. 
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.minima())
print(gt.maxima())
print(gt.promedio())
# Ejercicio 7
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)
gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))
print(gp.edad_promedio())
# Ejercicio 8.
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = 0
        equipo_mayor = ""

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor:
                mayor = len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor
eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Ana")
print(eq.equipo_mayor_integrantes())
# Ejercicio 9.
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:
            if letra.isdigit():
                digitos += 1
            elif letra.isalpha():
                if self.solo_vocales(letra):
                    vocales += 1
                else:
                    consonantes += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }
    
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
print(astr.texto_mas_largo)
# Ejercicio 10.
class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []

        for descripcion, prioridad in self.tareas:
            if prioridad == "alta":
                resultado.append((descripcion, prioridad))

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())
t.eliminar_completada("Estudiar")
print(t.tareas)
# Ejercicio 11.
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        elemento_mayor = None
        frecuencia_mayor = 0

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > frecuencia_mayor:
                frecuencia_mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))
 
# Ejercicio 12. 
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()

        for rango in rangos:
            inicio, fin = rango
            numeros = self.crear_rango(inicio, fin)

            for numero in numeros:
                unicos.add(numero)

        return list(unicos)
sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))
# ejercicio 13
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []

        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = listas[0]

        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])

        return resultado
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
print(cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))
# ejercicio 14.
class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)

        return resultado

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_nota = -1

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())
# ejercicio 15.
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        suma = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma += i

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado
df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 8, 12))
# ejercicio 16.
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        inicio = ord ('a')

        posicion = ord(letra.lower()) - inicio
        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(nueva_posicion + inicio)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado

cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))
# ejercicio 17
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)

ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))
# ejercicio 18.
import math

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = float('inf')

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (5, 5)))
# ejercicio 19.
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True

        return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado
inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(25))
#Ejercicio 20.
class AnalizadorPatrones:
    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self, texto):
        palabras = texto.split()
        return set(palabras)
ap = AnalizadorPatrones()
print(ap.encontrar_palabras("el gato está aquí", "g"))
print(ap.agrupar_por_longitud("el gato está aquí"))
print(ap.palabras_unicas("el gato el perro"))