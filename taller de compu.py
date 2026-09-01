import simpy
import random


def computadora(env, nombre, taller, resultados,
                diag_min, diag_max,
                reparacion_min, reparacion_max):

    llegada = env.now

    print(f"[{env.now:.2f}] {nombre} llega al taller.")

    with taller.request() as solicitud:

        yield solicitud

        inicio = env.now
        espera = inicio - llegada

        print(f"[{env.now:.2f}] {nombre} comienza la atención.")

        # Diagnóstico
        diagnostico = random.uniform(diag_min, diag_max)

        print(
            f"[{env.now:.2f}] {nombre} - "
            f"Diagnóstico: {diagnostico:.2f} min"
        )

        yield env.timeout(diagnostico)

        # Reparación
        reparacion = random.uniform(
            reparacion_min,
            reparacion_max
        )

        print(
            f"[{env.now:.2f}] {nombre} - "
            f"Reparación: {reparacion:.2f} min"
        )

        yield env.timeout(reparacion)

        # Prueba
        print(
            f"[{env.now:.2f}] {nombre} - "
            "Realizando prueba."
        )

        yield env.timeout(5)

        print(
            f"[{env.now:.2f}] {nombre} - "
            "Lista para entregar."
        )

    total = env.now - llegada

    resultados.append({
        "nombre": nombre,
        "espera": espera,
        "diagnostico": diagnostico,
        "reparacion": reparacion,
        "total": total
    })


def llegada_computadora(
    env,
    numero,
    taller,
    resultados,
    diag_min,
    diag_max,
    reparacion_min,
    reparacion_max
):

    yield env.timeout(random.uniform(2, 8))

    env.process(
        computadora(
            env,
            f"Computadora {numero}",
            taller,
            resultados,
            diag_min,
            diag_max,
            reparacion_min,
            reparacion_max
        )
    )


# ==============================================
# PROGRAMA PRINCIPAL
# ==============================================

print("==============================================")
print("     TALLER DE REPARACIÓN DE COMPUTADORAS")
print("==============================================")

numero_computadoras = int(
    input("Número de computadoras: ")
)

numero_tecnicos = int(
    input("Número de técnicos: ")
)

diag_min = float(
    input("Tiempo mínimo de diagnóstico (min): ")
)

diag_max = float(
    input("Tiempo máximo de diagnóstico (min): ")
)

reparacion_min = float(
    input("Tiempo mínimo de reparación (min): ")
)

reparacion_max = float(
    input("Tiempo máximo de reparación (min): ")
)


# Crear entorno
env = simpy.Environment()

# Crear técnicos
taller = simpy.Resource(
    env,
    capacity=numero_tecnicos
)

resultados = []


# Crear llegada de computadoras
for i in range(1, numero_computadoras + 1):

    env.process(
        llegada_computadora(
            env,
            i,
            taller,
            resultados,
            diag_min,
            diag_max,
            reparacion_min,
            reparacion_max
        )
    )


# Ejecutar simulación
env.run()


# ==============================================
# RESULTADOS
# ==============================================

print("\n==============================================")
print("           RESULTADOS")
print("==============================================")


for r in resultados:

    print(f"\n{r['nombre']}")
    print(f"  Espera:       {r['espera']:.2f} min")
    print(f"  Diagnóstico:  {r['diagnostico']:.2f} min")
    print(f"  Reparación:   {r['reparacion']:.2f} min")
    print(f"  Tiempo total: {r['total']:.2f} min")


# ==============================================
# PROMEDIOS
# ==============================================

if resultados:

    espera_promedio = sum(
        r["espera"] for r in resultados
    ) / len(resultados)

    diagnostico_promedio = sum(
        r["diagnostico"] for r in resultados
    ) / len(resultados)

    reparacion_promedio = sum(
        r["reparacion"] for r in resultados
    ) / len(resultados)

    total_promedio = sum(
        r["total"] for r in resultados
    ) / len(resultados)


    print("\n==============================================")
    print("           PROMEDIOS")
    print("==============================================")

    print(
        f"Espera promedio: "
        f"{espera_promedio:.2f} minutos"
    )

    print(
        f"Diagnóstico promedio: "
        f"{diagnostico_promedio:.2f} minutos"
    )

    print(
        f"Reparación promedio: "
        f"{reparacion_promedio:.2f} minutos"
    )

    print(
        f"Tiempo total promedio: "
        f"{total_promedio:.2f} minutos"
    )

print("\n==============================================")
print("       SIMULACIÓN FINALIZADA")
print("==============================================")