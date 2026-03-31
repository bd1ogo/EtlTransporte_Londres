import pandas as pd

#Extract
df = pd.read_csv("data/transportes.csv")

#Padronizar as colunas
df.columns = df.columns.str.lower() \
                        .str.replace(" ", "_") \
                        .str.replace("(", "") \
                        .str.replace(")", "")

print("Colunas após padronização:")
print(df.columns)

#Convertendo as datas
df["period_beginning"] = pd.to_datetime(df["period_beginning"], format="%d-%b-%y", errors="coerce")
df["period_ending"] = pd.to_datetime(df["period_ending"], format="%d-%b-%y", errors="coerce")
df["reporting_period"] = df["reporting_period"].fillna(0).astype(int)
df["days_in_period"] = df["days_in_period"].fillna(0).astype(int)
df = df.dropna(subset=["period_beginning", "period_ending"])

#Tratando nulos
df = df.fillna(0)

#Criando coluna Total
df["total_journeys"] = (
    df["bus_journeys_m"] +
    df["underground_journeys_m"] +
    df["dlr_journeys_m"] +
    df["tram_journeys_m"] + 
    df["overground_journeys_m"] +
    df["london_cable_car_journeys_m"] +
    df["tfl_rail_journeys_m"]
)

#Validação
print(df.head())
print(df.info())
