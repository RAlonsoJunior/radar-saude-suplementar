#==============================================================
# TESTE DE FUMAÇA - DUCKDB
#==============================================================

import duckdb
import pandas as pd

con = duckdb.connect()

df = pd.DataFrame({
    "uf": ["AC", "MG", "RJ", "MG"],
    "qt_beneficiario_ativo": [100, 500, 800, 300],
})

# Consultar dados do dataframe

resultado = con.query("""
    SELECT uf,
              SUM(qt_beneficiario_ativo) AS total_beneficiario
    FROM df
    GROUP BY uf
    ORDER BY uf
""").df()

print(resultado)