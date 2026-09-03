import simpy
import random


def computadora(env, cliente, nombre, taller, resultados,
                diag_min, diag_max,
                reparacion_min, reparacion_max):

    llegada = env.now
    print(f"[{env.now:.2f}] {cliente} trae su {nombre} al taller.")

    # Solicitar técnico
    with taller.request() as solicitud_tecnico:
        yield solicitud_tecnico

        inicio = env.now
        espera = inicio - llegada
        print(f"[{env.now:.2f}] Técnico atiende {nombre} del {cliente}.")

        # Diagnóstico
        diagnostico = random.uniform(diag_min, diag_max)
        print(f"[{env.now:.2f}] {nombre} - Diagnóstico: {diagnostico:.2f} min")
        yield env.timeout(diagnostico)

        # Reparación
        reparacion = random.uniform(reparacion_min, reparacion_max)
        print(f"[{env.now:.2f}] {nombre} - Reparación: {reparacion:.2f} min")
        yield env.timeout(reparacion)

        # Prueba
        print(f"[{env.now:.2f}] {nombre} - Realizando prueba.")
        yield env.timeout(5)

        print(f"[{env.now:.2f}] {nombre} - Lista para entregar al {cliente}.")

    total = env.now - llegada

    # Registrar orden de servicio
    resultados.append({
        "cliente": cliente,
        "nombre": nombre,
        "espera": espera,
        "diagnostico": diagnostico,
        "reparacion": reparacion,
        "total": total,
        "orden_servicio": f"OS-{cliente}-{nombre}"
    })


def llegada_cliente(env, cliente_id, num_computadoras, taller, resultados,
                    diag_min, diag_max,
                    reparacion_min, reparacion_max):
    """Cada cliente puede traer varias computadoras"""
    cliente = f"Cliente {cliente_id}"
    for i in range(1, num_computadoras + 1):
        yield env.timeout(random.uniform(2, 8))  # llegada escalonada
        nombre = f"Computadora {i}"
        env.process(
            computadora(env, cliente, nombre, taller, resultados,
                        diag_min, diag_max,
                        reparacion_min, reparacion_max)
        )

# SIMULACIÓN CONTINUA

cliente_id = 1  # contador de clientes

while True:
    print("\n==============================================")
    print(f"   SIMULACIÓN PARA CLIENTE {cliente_id}")
    print("==============================================")

    # Datos de entrada para este cliente
    num_computadoras = int(input(f"¿Cuántas computadoras trae el Cliente {cliente_id}? "))
    numero_tecnicos = int(input("Número de técnicos disponibles: "))
    diag_min = float(input("Tiempo mínimo de diagnóstico (min): "))
    diag_max = float(input("Tiempo máximo de diagnóstico (min): "))
    reparacion_min = float(input("Tiempo mínimo de reparación (min): "))
    reparacion_max = float(input("Tiempo máximo de reparación (min): "))

    # Crear entorno
    env = simpy.Environment()
    taller = simpy.Resource(env, capacity=numero_tecnicos)
    resultados = []

    # Procesar computadoras del cliente
    env.process(
        llegada_cliente(env, cliente_id, num_computadoras, taller, resultados,
                        diag_min, diag_max,
                        reparacion_min, reparacion_max)
    )

    env.run()

    # RESULTADOS
    
    print("\n==============================================")
    print("           RESULTADOS")
    print("==============================================")

    for r in resultados:
        print(f"\nOrden de servicio: {r['orden_servicio']}")
        print(f"Cliente: {r['cliente']}")
        print(f"Equipo: {r['nombre']}")
        print(f"  Espera:       {r['espera']:.2f} min")
        print(f"  Diagnóstico:  {r['diagnostico']:.2f} min")
        print(f"  Reparación:   {r['reparacion']:.2f} min")
        print(f"  Tiempo total: {r['total']:.2f} min")

    # PROMEDIOS
  
    if resultados:
        espera_promedio = sum(r["espera"] for r in resultados) / len(resultados)
        diagnostico_promedio = sum(r["diagnostico"] for r in resultados) / len(resultados)
        reparacion_promedio = sum(r["reparacion"] for r in resultados) / len(resultados)
        total_promedio = sum(r["total"] for r in resultados) / len(resultados)

        print("\n==============================================")
        print("           PROMEDIOS")
        print("==============================================")
        print(f"Espera promedio: {espera_promedio:.2f} minutos")
        print(f"Diagnóstico promedio: {diagnostico_promedio:.2f} minutos")
        print(f"Reparación promedio: {reparacion_promedio:.2f} minutos")
        print(f"Tiempo total promedio: {total_promedio:.2f} minutos")

    print("\n==============================================")
    print("       SIMULACIÓN FINALIZADA")
    print("==============================================")

    # Pasar al siguiente cliente automáticamente
    cliente_id += 1
