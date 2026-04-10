import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="transportes_londres"
)
query = "SELECT * FROM transportes"
df = pd.read_sql(query, conn)
conn.close()

print("\n VISÃO GERAL DOS DADOS")
print(df.head())
print("\n ESTATÍSTICAS DESCRITIVAS")
print(df.describe())

totais = {
    "Bus": df["bus_journeys_m"].sum(),
    "Metro": df["underground_journeys_m"].sum(),
    "DLR": df["dlr_journeys_m"].sum(),
    "Tram": df["tram_journeys_m"].sum(),
    "Overground": df["overground_journeys_m"].sum()
}
print("\n TOTAL DE VIAGENS POR MODAL")
for k, v in totais.items():
    print(f"{k}: {v:,.2f}")

df = df.sort_values("period_beginning")
print("\n DADOS ORDENADOS POR DATA")
print(df[["period_beginning", "total_journeys"]].head())

modal_mais_usado = max(totais, key=totais.get)
print(f"\n Modal mais utilizado: {modal_mais_usado}")

min_bus = df.loc[df["bus_journeys_m"].idxmin()]
print("\n MÊS COM MENOR USO DE ÔNIBUS")
print(min_bus[["period_beginning", "bus_journeys_m"]])

# Gráficos
df = df.sort_values("period_beginning")

plt.figure()
plt.plot(df["period_beginning"], df["total_journeys"])
plt.title("Total Journeys Over Time")
plt.xlabel("Date")
plt.ylabel("Total Journeys")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

totais = {
    "Bus": df["bus_journeys_m"].sum(),
    "Metro": df["underground_journeys_m"].sum(),
    "DLR": df["dlr_journeys_m"].sum(),
    "Tram": df["tram_journeys_m"].sum(),
    "Overground": df["overground_journeys_m"].sum()
}

plt.figure()
plt.bar(totais.keys(), totais.values())
plt.title("Total Journeys by Transport Type")
plt.xticks(rotation=45)
plt.show()
