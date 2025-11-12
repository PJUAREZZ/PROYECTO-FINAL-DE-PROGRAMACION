# IMPORTANTE!!
# Instalación de dependencias del proyecto
# Para instalar todas las dependencias necesarias, desde la terminal, ejecuta el siguiente comando en la raíz del proyecto:
#
#     pip install -r requirements.txt
#
# Este comando instalará automáticamente todas las librerías listadas en el archivo
# requirements.txt, incluyendo FastAPI, Uvicorn (para ejecutar el servidor) y otras
# dependencias requeridas por la aplicación.

# Por ultimo ejecuta el comando uvicorn main:app --reload para levantar el servidor de la api

#  Importamos todas las librerias que utilizaremos
from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel  
from datetime import datetime


# La variable DB_NAME almacena el nombre del archivo de la base de datos SQLite
# "negocio.db" es el archivo donde se guardan todas las tablas y registros del proyecto

DB_NAME = "negocio.db"

# Esta funcion inicializa la conxion a la base de datos de SQLite y crea las tablas necesarias para el proyecto (productos, pedidos, pedido_detalle)
def init_db():
    """Inicializa la base de datos y crea la tabla si no existe"""
    conn = sqlite3.connect(DB_NAME) # Conexion a la base de datos
    cursor = conn.cursor() # El cursor prepara la conexión (conn) para poder enviar consultas y recibir resultados desde SQLite.

    # creacion Tabla PRODUCTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            imagen TEXT,
            categoria TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )
    """)
    
    # creacion Tabla PEDIDOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            pedido_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_cliente TEXT NOT NULL,
            direccion TEXT NOT NULL,
            total REAL NOT NULL,
            fecha_pedido TEXT NOT NULL
        )
    """)
    
    # creacion Tabla PEDIDO_DETALLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedido_detalle (
            detalle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
            FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
        )
    """)

    conn.commit() # Se guardan los cambios 
    conn.close() # importante cerrar la conexion de la base de datos
    print("Base de datos inicializada")


def get_db_connection():
    """Obtiene una conexión a la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# instancia de FastApi
app = FastAPI()

# ejecutamos la funcion que prepara la base de datos
init_db()

# Creamos un objeto Productos con sus respectivos atributos, utilizando el BaseModel de FastApi
class Productos(BaseModel): 
    nombre: str
    descripcion: str
    precio: int 
    imagen: str
    categoria: str



# Enpoint Raiz
@app.get("/")
def root(): 
    return {
        "mensaje" : "Esta es la api de nuestra pagina"
    }

# Enpoint que utiliza una operacion POST para agregar productos 
@app.post("/productos" , status_code=201)
def agregar_productos(producto: Productos): 
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" INSERT INTO productos (nombre, descripcion, precio, imagen, categoria, fecha_creacion) 
    VALUES(?, ?, ?, ?, ?, ?)""" , 
    (producto.nombre,
     producto.descripcion, 
     producto.precio, 
     producto.imagen, 
     producto.categoria,
     datetime.now().isoformat() # operador que obtiene la fecha en la que se realiza el put
    )) # ejecuta codigo SQL, inserta los valores de los atributos para que sean agregados a las tablas
    
    producto_id = cursor.lastrowid # obtiene el id del ultimo objeto agregado
    conn.commit()
    conn.close()
    return {
        "mensaje": "Producto creado exitosamente",
        "producto_id": producto_id
    } # mostramos mensaje de exito 
    
    

# Enpoint que uitliza una operacion GET para obtener los datos de los productos
@app.get("/productos", status_code=200)
def mostrar_productos(): 
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM productos """) # Consulta SQL 
    productos = [dict(row) for row in cursor.fetchall()] # Convierte los resultados de la consulta en un diccionario
    conn.close()
    return productos


# Enpoint que utiliza una operacion GET para obtener los datos de un producto en especifico segun su id
@app.get("/productos/{producto_id}", status_code=200)
def mostrar_producto_individual(producto_id : int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM productos WHERE producto_id = ? """, (producto_id,)) # Consulta de SQL 
    productoIndividual = cursor.fetchone()
    conn.close()  
    if productoIndividual is None: 
        raise HTTPException(status_code=404, detail={"No se encontro el producto"}) # Manejo de errores
    return dict(productoIndividual)