#==========================================================
# TESTE DE FUMAÇA - SQLSERVER
#==========================================================

import pyodbc


print(pyodbc.drivers())


con = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};" 
    "SERVER=DESKTOP-90FUAVJ;"
    "TRUSTED_CONNECTION=yes;"
)
print("Conexão estabelecida com sucesso!")
print(con.execute("SELECT @@version;").fetchone()[0])