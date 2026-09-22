# Ejercicio 1.
class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


calificador = Calificador()

resultado = calificador.cargar_notas(50, 70, 60, 130, -10)

print("Notas validadas:", resultado)

print("Promedio:", calificador.promedio())
# Ejercicio 2 Analizador de Palabras.
class AnalizadorPalabras:

    def __init__(self):
        self.palabras = []

    def agregar_palabra(self, palabra):
        self.palabras.append(palabra)

    def agregar_multiples(self, *palabras):
        for palabra in palabras:
            self.palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras)

    def palabra_mas_larga(self):
        return max(self.palabras, key=len)

    def palabras_cortas(self, maximo):
        resultado = []

        for palabra in self.palabras:
            if len(palabra) <= maximo:
                resultado.append(palabra)

        return resultado


ap = AnalizadorPalabras()

ap.agregar_multiples(
    "hola",
    "python",
    "sol",
    "programacion"
)

print(ap.palabras)
print(ap.contar_palabras())
print(ap.palabra_mas_larga())
print(ap.palabras_cortas(4))
#Ejercicio 3. 
class GestorProductos:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def agregar_multiples(self, *productos):
        for nombre, precio in productos:
            self.productos[nombre] = precio

    def precio_total(self):
        return sum(self.productos.values())

    def productos_caros(self, precio_minimo):
        resultado = []

        for nombre, precio in self.productos.items():
            if precio > precio_minimo:
                resultado.append(nombre)

        return resultado


gp = GestorProductos()

gp.agregar_producto("pan", 2.50)
gp.agregar_producto("leche", 3.00)

gp.agregar_multiples(
    ("queso", 5.00),
    ("arroz", 1.50)
)

print(gp.productos)
print(gp.precio_total())
print(gp.productos_caros(2.50))
#Ejercicio 4-Separador de Numeros.
class SeparadorNumeros:

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

    def cantidad_pares(self):
        return len(self.pares)

    def cantidad_impares(self):
        return len(self.impares)


sn = SeparadorNumeros()

sn.separar(2, 7, 10, 15, 20, 21, 30)

print(sn.pares)
print(sn.impares)
print(sn.cantidad_pares())
print(sn.cantidad_impares())
#Ejercicio 5- Registro de temperatura.
class RegistroTemperaturas:

    def __init__(self):
        self.temperaturas = []

    def registrar(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.temperaturas.append(temp)

    def temperatura_minima(self):
        return min(self.temperaturas)

    def temperatura_maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def temperaturas_altas(self, limite):
        resultado = []

        for temp in self.temperaturas:
            if temp >= limite:
                resultado.append(temp)

        return resultado


rt = RegistroTemperaturas()

rt.registrar_multiples(25, 30, 18, 35, 28)

print(rt.temperaturas)
print(rt.temperatura_minima())
print(rt.temperatura_maxima())
print(rt.promedio())
print(rt.temperaturas_altas(30))
#Ejercicio 6- Gestor de estudiante.
class GestorEstudiantes:

    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, edad):
        self.estudiantes[nombre] = edad

    def estudiantes_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.estudiantes.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        return sum(self.estudiantes.values()) / len(self.estudiantes)

    def estudiante_mayor(self):
        return max(self.estudiantes, key=self.estudiantes.get)


ge = GestorEstudiantes()

ge.agregar_estudiante("Ana", 20)
ge.agregar_estudiante("Luis", 17)
ge.agregar_estudiante("Carlos", 25)
ge.agregar_estudiante("Maria", 19)

print(ge.estudiantes)
print(ge.estudiantes_mayores(18))
print(ge.edad_promedio())
print(ge.estudiante_mayor())
#Ejercicio 7- Gestor de equipos.
class GestorEquipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre):
        self.equipos[nombre] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def cantidad_jugadores(self, equipo):
        return len(self.equipos[equipo])

    def equipo_mayor(self):
        return max(
            self.equipos,
            key=lambda equipo: len(self.equipos[equipo])
        )


ge = GestorEquipos()

ge.crear_equipo("A")
ge.crear_equipo("B")

ge.agregar_jugador("A", "Juan")
ge.agregar_jugador("A", "Pedro")

ge.agregar_jugador("B", "Ana")
ge.agregar_jugador("B", "Luis")
ge.agregar_jugador("B", "Carlos")

print(ge.equipos)
print(ge.cantidad_jugadores("B"))
print(ge.equipo_mayor())
#Ejercicio 8- Analizar Texto.
class AnalizadorTexto:

    def __init__(self):
        self.texto_mas_largo = ""

    def analizar(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0
        espacios = 0

        for caracter in texto.lower():

            if caracter in "aeiou":
                vocales += 1

            elif caracter.isalpha():
                consonantes += 1

            elif caracter.isdigit():
                digitos += 1

            elif caracter == " ":
                espacios += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos,
            "espacios": espacios
        }


at = AnalizadorTexto()

print(at.analizar("Hola Python 123"))
#Ejercicio 9- Gestión de Tareas.
class GestorTareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def tareas_por_prioridad(self, prioridad):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == prioridad:
                resultado.append(tarea)

        return resultado

    def eliminar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False

    def cantidad_tareas(self):
        return len(self.tareas)
#Ejercicio 10- Frecuencia de un elemento 
class FrecuenciaElementos:

    def __init__(self):
        self.frecuencias = {}

    def agregar(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def agregar_multiples(self, *elementos):
        for elemento in elementos:
            self.agregar(elemento)

    def frecuencia(self, elemento):
        return self.frecuencias.get(elemento, 0)

    def elemento_mas_frecuente(self):
        return max(self.frecuencias, key=self.frecuencias.get)
#Ejercicio 11- Generar Rango.
class GeneradorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def numeros_pares(self, inicio, fin):
        resultado = []

        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                resultado.append(numero)

        return resultado

    def numeros_impares(self, inicio, fin):
        resultado = []

        for numero in range(inicio, fin + 1):
            if numero % 2 != 0:
                resultado.append(numero)

        return resultado

    def rangos_multiples(self, *rangos):
        resultado = set()

        for inicio, fin in rangos:
            for numero in range(inicio, fin + 1):
                resultado.add(numero)

        return resultado
#Ejercicio 12- intercalar.
class Intercalador:

    def intercalar(self, lista1, lista2):
        resultado = []

        for a, b in zip(lista1, lista2):
            resultado.append(a)
            resultado.append(b)

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        for grupo in zip(*listas):
            for elemento in grupo:
                resultado.append(elemento)

        return resultado


i = Intercalador()

print(i.intercalar([1, 2, 3], [10, 20, 30]))
#Ejercicio 13- Registro de las calificaciones.
class RegistroCalificaciones:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def aprobados(self, nota_minima):
        resultado = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)

        return resultado

    def promedio(self):
        return sum(self.notas.values()) / len(self.notas)

    def mejor_estudiante(self):
        return max(self.notas, key=self.notas.get)

    def nota_estudiante(self, estudiante):
        return self.notas.get(estudiante)


rc = RegistroCalificaciones()

rc.registrar("Ana", 9)
rc.registrar("Luis", 6)
rc.registrar("Carlos", 10)
rc.registrar("Maria", 7)

print(rc.notas)
print(rc.aprobados(7))
print(rc.promedio())
print(rc.mejor_estudiante())
print(rc.nota_estudiante("Ana"))
#Ejercicio 14-
class AnalizadorDivisores:

    def divisores(self, numero):
        resultado = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                resultado.append(i)

        return resultado

    def es_primo(self, numero):
        return len(self.divisores(numero)) == 2

    def divisores_multiples(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.divisores(numero)

        return resultado


ad = AnalizadorDivisores()

print(ad.divisores(12))
print(ad.es_primo(7))
print(ad.es_primo(10))
print(ad.divisores_multiples(6, 8, 10))
#Ejercicio 15- Numeros Especiales.
class NumerosEspeciales:

    def es_perfecto(self, numero):
        suma = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma += i

        return suma == numero

    def es_par(self, numero):
        return numero % 2 == 0

    def es_impar(self, numero):
        return numero % 2 != 0

    def analizar_multiples(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.es_perfecto(numero)

        return resultado


ne = NumerosEspeciales()

print(ne.es_perfecto(6))
print(ne.es_perfecto(10))
print(ne.es_par(8))
print(ne.es_impar(7))
print(ne.analizar_multiples(6, 10, 28, 12))
#Ejercicio 16- cifrar
class Cifrador:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        posicion = ord(letra) - ord("a")
        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(ord("a") + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra.lower():

            if letra in "abcdefghijklmnopqrstuvwxyz":
                resultado += self.codificar_letra(
                    letra,
                    desplazamiento
                )

        self.historial[palabra] = resultado

        return resultado


c = Cifrador()

print(c.codificar_palabra("hola", 3))
print(c.codificar_palabra("python", 2))
print(c.historial)
#Ejercicio 17- Calificacion de edades 
class ClasificadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar(self, edad):

        if edad <= 11:
            return "niño"

        elif edad <= 17:
            return "adolescente"

        elif edad <= 64:
            return "adulto"

        else:
            return "mayor"

    def agrupar(self, *edades):

        for edad in edades:
            categoria = self.clasificar(edad)
            self.grupos[categoria].append(edad)

    def promedio_categoria(self, categoria):

        edades = self.grupos[categoria]

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)


ce = ClasificadorEdades()

ce.agrupar(8, 12, 15, 20, 25, 40, 70, 80)

print(ce.grupos)
print(ce.clasificar(20))
print(ce.promedio_categoria("adulto"))
print(ce.promedio_categoria("niño"))
#Ejercicio 18- Contador de Numeros 
class ContadorNumeros:

    def __init__(self):
        self.numeros = []

    def agregar(self, numero):
        self.numeros.append(numero)

    def agregar_muchos(self, *numeros):
        for numero in numeros:
            self.numeros.append(numero)

    def contar_pares(self):
        contador = 0

        for numero in self.numeros:
            if numero % 2 == 0:
                contador += 1

        return contador

    def contar_impares(self):
        contador = 0

        for numero in self.numeros:
            if numero % 2 != 0:
                contador += 1

        return contador


cn = ContadorNumeros()

cn.agregar_muchos(2, 5, 8, 11, 14, 20)

print(cn.numeros)
print(cn.contar_pares())
print(cn.contar_impares())
#Ejercicio 19- Gestor de Nombres
class GestorNombres:

    def __init__(self):
        self.nombres = []

    def agregar(self, nombre):
        self.nombres.append(nombre)

    def agregar_muchos(self, *nombres):
        for nombre in nombres:
            self.nombres.append(nombre)

    def nombres_largos(self, cantidad):
        resultado = []

        for nombre in self.nombres:
            if len(nombre) >= cantidad:
                resultado.append(nombre)

        return resultado

    def cantidad_nombres(self):
        return len(self.nombres)

    def primer_nombre(self):
        return self.nombres[0]


gn = GestorNombres()

gn.agregar_muchos("Ana", "Carlos", "Juan", "Alejandro", "Maria")

print(gn.nombres)
print(gn.nombres_largos(6))
print(gn.cantidad_nombres())
print(gn.primer_nombre())
#Ejercicio 20- Registro de Ciudades
class RegistroCiudades:

    def __init__(self):
        self.ciudades = {}

    def agregar(self, ciudad, habitantes):
        self.ciudades[ciudad] = habitantes

    def agregar_muchas(self, *datos):
        for ciudad, habitantes in datos:
            self.ciudades[ciudad] = habitantes

    def ciudades_grandes(self, minimo):
        resultado = []

        for ciudad, habitantes in self.ciudades.items():
            if habitantes >= minimo:
                resultado.append(ciudad)

        return resultado

    def ciudad_mas_poblada(self):
        return max(self.ciudades, key=self.ciudades.get)

    def cantidad_ciudades(self):
        return len(self.ciudades)


rc = RegistroCiudades()

rc.agregar_muchas(
    ("Guayaquil", 2700000),
    ("Quito", 2800000),
    ("Cuenca", 600000),
    ("Loja", 200000)
)

print(rc.ciudades)
print(rc.ciudades_grandes(1000000))
print(rc.ciudad_mas_poblada())
print(rc.cantidad_ciudades())