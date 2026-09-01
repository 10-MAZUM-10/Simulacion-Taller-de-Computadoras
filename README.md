# Simulacion-Taller-de-Computadoras
Trabajo Tema 1

# Simulación de un Taller de Reparación de Computadoras

## Descripción

Este proyecto consiste en una simulación de un **taller de reparación de computadoras**, desarrollada en Python utilizando la librería **SimPy**.

El programa representa el proceso que sigue una computadora desde que llega al taller hasta que termina su reparación y queda lista para ser entregada al cliente.

La simulación permite observar el tiempo que tarda cada computadora en ser atendida y analizar el tiempo de espera, diagnóstico y reparación.

## Objetivo

Simular el proceso de atención de computadoras en un taller de reparación para determinar cuánto tiempo tarda cada equipo en ser atendido y cuáles son los tiempos promedio del proceso.

## Proceso simulado

El sistema sigue las siguientes etapas:

1. La computadora llega al taller.
2. Espera a que un técnico esté disponible.
3. El técnico realiza el diagnóstico.
4. Se realiza la reparación.
5. Se realiza una prueba del equipo.
6. La computadora queda lista para ser entregada.

## Entidades

Las principales entidades consideradas en el sistema son:

* Clientes
* Computadoras
* Técnicos
* Herramientas
* Órdenes de servicio

En la simulación, las computadoras representan los elementos que pasan por el proceso y los técnicos se representan como recursos limitados.

## Variables

El programa utiliza las siguientes variables:

* Número de computadoras.
* Número de técnicos.
* Tiempo mínimo de diagnóstico.
* Tiempo máximo de diagnóstico.
* Tiempo mínimo de reparación.
* Tiempo máximo de reparación.
* Tiempo de espera.
* Tiempo de diagnóstico.
* Tiempo de reparación.
* Tiempo total de atención.

## Datos de entrada

El programa funciona desde la **terminal** y solicita al usuario los datos necesarios para realizar la simulación:

```text
Número de computadoras
Número de técnicos
Tiempo mínimo de diagnóstico
Tiempo máximo de diagnóstico
Tiempo mínimo de reparación
Tiempo máximo de reparación
```

Los tiempos pueden establecerse utilizando los datos obtenidos durante la observación del taller.

## Funcionamiento del algoritmo

El programa crea un entorno de simulación utilizando `simpy.Environment()`.

Los técnicos se representan mediante un recurso:

```python
taller = simpy.Resource(env, capacity=numero_tecnicos)
```

Esto permite simular que solamente puede atenderse un número determinado de computadoras al mismo tiempo, dependiendo de la cantidad de técnicos disponibles.

Los tiempos de diagnóstico y reparación se generan dentro de los rangos introducidos por el usuario.

Por ejemplo:

```python
diagnostico = random.uniform(diag_min, diag_max)
```

De esta manera, cada computadora puede tener un tiempo diferente de diagnóstico y reparación.

## Resultados

Al finalizar la simulación, el programa muestra en la terminal los resultados obtenidos para cada computadora:

* Tiempo de espera.
* Tiempo de diagnóstico.
* Tiempo de reparación.
* Tiempo total en el taller.

También calcula los promedios generales:

* Espera promedio.
* Diagnóstico promedio.
* Reparación promedio.
* Tiempo total promedio.

## Ejemplo de entrada

```text
==============================================
     TALLER DE REPARACIÓN DE COMPUTADORAS
==============================================

Número de computadoras: 10
Número de técnicos: 2
Tiempo mínimo de diagnóstico (min): 10
Tiempo máximo de diagnóstico (min): 30
Tiempo mínimo de reparación (min): 20
Tiempo máximo de reparación (min): 60
```

## Ejemplo de salida

```text
==============================================
           RESULTADOS
==============================================

Computadora 1
  Espera:       0.00 min
  Diagnóstico:  18.42 min
  Reparación:   35.71 min
  Tiempo total: 59.13 min

Computadora 2
  Espera:       5.32 min
  Diagnóstico:  24.18 min
  Reparación:   42.63 min
  Tiempo total: 77.13 min

==============================================
           PROMEDIOS
==============================================

Espera promedio: 8.46 minutos
Diagnóstico promedio: 20.74 minutos
Reparación promedio: 39.82 minutos
Tiempo total promedio: 69.02 minutos
```

*Los valores anteriores son únicamente un ejemplo; los resultados reales cambian debido a la simulación aleatoria.*

## Tecnologías utilizadas

* **Python 3.10**
* **SimPy 4.1.2**
* **Visual Studio Code**
* **Random**, librería incluida en Python.

## Instalación

Para instalar SimPy se utiliza el siguiente comando:

```bash
python -m pip install simpy
```

## Ejecución

Para ejecutar el programa desde la terminal:

```bash
python simulacion_taller.py
```

Después, el programa solicitará los datos necesarios para realizar la simulación.

## Conclusión

La simulación permite representar de manera aproximada el funcionamiento de un taller de reparación de computadoras. Con los resultados obtenidos se puede analizar el tiempo que permanecen los equipos en el taller y observar cómo la cantidad de técnicos influye en los tiempos de espera.

El uso de **SimPy** permite representar procesos donde existen recursos limitados, como los técnicos de un taller, y analizar el comportamiento del sistema mediante diferentes datos de entrada.
