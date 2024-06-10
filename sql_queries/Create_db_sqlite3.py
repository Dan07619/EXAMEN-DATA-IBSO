import sqlite3

# Nombre de la base de datos
db_name = 'database.db'
script = 'C:\Users\nama_\OneDrive\Documentos\GitHub\EXAMEN-DATA-IBSO\sql_queries\DATABASE1.sql'
# Leer el archivo SQL
with open(script, 'r') as file:
    sql_script = file.read()

# Conectar a la base de datos (se creará automáticamente si no existe)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Ejecutar el script SQL
cursor.executescript(sql_script)

# Cerrar la conexión
conn.close()

print(f"Base de datos '{db_name}' creada y script SQL ejecutado con éxito.")
