import pandas as pd

ARCHIVO = "mapa_semantico_eva_limpio.csv"

df = pd.read_csv(ARCHIVO)

print("BUSCADOR EVA - MANUSCRITO VOYNICH")
print("=" * 50)

while True:
    busqueda = input("\nIngresa palabra EVA, familia, planta o folio (o escribe salir): ").strip().lower()

    if busqueda == "salir":
        print("Buscador cerrado.")
        break

    resultados = df[
        df.astype(str).apply(
            lambda fila: fila.str.lower().str.contains(busqueda).any(),
            axis=1
        )
    ]

    if resultados.empty:
        print("No se encontraron resultados.")
    else:
        print(f"\nResultados encontrados: {len(resultados)}")
        print("-" * 50)

        for _, row in resultados.iterrows():
            print(f"Folio: {row['folio']}")
            print(f"Planta: {row['planta']}")
            print(f"Uso médico: {row['uso_medico']}")
            print(f"Palabra EVA: {row['palabra_eva']}")
            print(f"Familia: {row['familia']}")
            print(f"Significado probable: {row['significado_probable']}")
            print("-" * 50)