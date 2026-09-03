# Simulacion-Taller-de-Computadoras
Trabajo Tema 1

# Simulación de un Taller de Reparación de Computadoras

## Descripción

Este proyecto consiste en una simulación de un taller de reparación de computadoras, desarrollada en Python utilizando la librería SimPy.
El programa representa el proceso que sigue un cliente cuando lleva una o varias computadoras al taller: desde la llegada, la espera por un técnico, el diagnóstico, la reparación, la prueba y finalmente la entrega con una orden de servicio.

## Objetivo

Simular el proceso de atención de computadoras en un taller de reparación para determinar cuánto tiempo tarda cada equipo en ser atendido y cuáles son los tiempos promedio del proceso.

## Proceso simulado

El sistema sigue las siguientes etapas:

1. El cliente llega al taller con una o varias computadoras.
2. Espera a que un técnico esté disponible.
3. El técnico realiza el diagnóstico.
4. Se realiza la reparación.
5. Se realiza una prueba del equipo.
6. Se genera una orden de servicio y la computadora queda lista para ser entregada al cliente.

## Entidades

Las principales entidades consideradas en el sistema son:

Clientes: quienes llevan las computadoras al taller.

* Computadoras: los equipos que pasan por el proceso de atención.
* Técnicos: los recursos limitados que realizan diagnóstico, reparación y prueba.
* Órdenes de servicio: registros generados para cada reparación realizada.
* En la simulación, las computadoras representan los elementos que pasan por el proceso y los técnicos se representan como recursos limitados.

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

El programa solicita al usuario, desde la **terminal**, los siguientes datos para cada cliente:  
- Cuántas computadoras trae.  
- Número de técnicos disponibles.  
- Tiempo mínimo y máximo de diagnóstico.  
- Tiempo mínimo y máximo de reparación.  

Al finalizar la simulación de ese cliente, se muestran los resultados y automáticamente inicia la atención del siguiente.

---

## Funcionamiento del algoritmo
- Se crea un entorno de simulación con `simpy.Environment()`.  
- Los técnicos se modelan como un recurso limitado mediante `simpy.Resource()`.  
- Los tiempos de diagnóstico y reparación se generan aleatoriamente dentro de los rangos definidos por el usuario.  
- Cada computadora sigue el ciclo completo de atención hasta su entrega.  
- El programa corre en un bucle infinito (`while True`), de modo que cada cliente se atiende uno tras otro sin necesidad de reiniciar el programa.  

---

## Resultados
Al finalizar la simulación de cada cliente, el programa muestra:  
- Los tiempos individuales de espera, diagnóstico, reparación y atención total de cada computadora.  
- Los promedios generales de cada etapa del proceso.  
- Un resumen indicando cuántas computadoras trajo el cliente.  

---

## Conclusión
La simulación permite representar de manera aproximada el funcionamiento de un taller de reparación de computadoras en un escenario continuo de atención a clientes.  
Los resultados obtenidos facilitan el análisis de la eficiencia del servicio y muestran cómo la cantidad de técnicos influye directamente en los tiempos de espera y atención.  
El uso de **SimPy** hace posible modelar sistemas con recursos limitados y estudiar su comportamiento bajo diferentes condiciones de entrada, cliente por cliente.
