import mysql.connector
from transform import df  # importando o dataframe já tratado

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456"
    )

def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS transportes_londres")

    print("Banco criado")

    cursor.close()
    conexao.close()

def criar_tabela():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="transportes_londres"
    )

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transportes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        period_beginning DATE,
        period_ending DATE,
        reporting_period INT,
        days_in_period INT,
        total DECIMAL(10,2)
    )
    """)

    print("Tabela criada")

    cursor.close()
    conexao.close()

def inserir_dados():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="transportes_londres"
    )

    cursor = conexao.cursor()

    sql = """
    INSERT INTO transportes (
        period_beginning,
        period_ending,
        reporting_period,
        days_in_period,
        total
    ) VALUES (%s, %s, %s, %s, %s)
    """

    dados = []

    for _, row in df.iterrows():
        dados.append((
            row["period_beginning"],
            row["period_ending"],
            int(row["reporting_period"]),
            int(row["days_in_period"]),
            float(row["total_journeys"])
        ))

    cursor.executemany(sql, dados)
    conexao.commit()

    print(f"{cursor.rowcount} registros inseridos")

    cursor.close()
    conexao.close()

def consultar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="transportes_londres"
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM transportes LIMIT 5")

    resultados = cursor.fetchall()

    print("\nDados inseridos:")
    for linha in resultados:
        print(linha)

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    criar_banco()
    criar_tabela()
    inserir_dados()
    consultar()