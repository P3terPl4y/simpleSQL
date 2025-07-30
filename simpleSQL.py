##################################
"""         SimpleSQL         """
##################################
from sanitizar import sanitizar



class IniciarBD:
    def __init__(self,name):
        try:
            import sqlite3
            self.name=sanitizar(name)
            self.conexion = sqlite3.connect(self.name)
            self.cursor = self.conexion.cursor()
            with open("BD_Rejistro.txt","w") as f:
                f.write(self.name)
        except Exception as e:
            print(f"Error: {e}")
        print(f"Exito al Conectar con {name}")
        
        
        
    def CrearTabla(self, name, *campos):
        try:
            name=sanitizar(name)
            campos=sanitizar(campos)
            campos=",".join(campos)
            
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY AUTOINCREMENT,{campos})")
            print_campos="  ".join(campos.split())
            print(print_campos)
        except Exception as e:
            print(f"Error: {e}")
        print(f"Exito al crear la tabla {name}")
        
    
    def InsertarDatos(self, name, campos, *valores):
        try:
            
            name=sanitizar(name)
            campos=sanitizar(campos)
            valores=sanitizar(valores)
            
            
            
            placeholders = ', '.join(['?'] * len(valores))
            self.cursor.execute(f"INSERT INTO {name} ({campos}) VALUES ({placeholders})", valores)
            self.conexion.commit()
        except Exception as e:
            print(f"Error: {e}")                
        print(f"Exito al insertar los datos")


    def EliminarTabla(self, name):
        try:
            name=sanitizar(name)
            self.cursor.execute(f"DROP TABLE IF EXISTS {name}")
        except Exception as e:
            print(f"Error: {e}")
        print(f"Exito al eliminar la tabla {name}")
      
        
    def ConsultarDatos(self,name):
        try:
            name=sanitizar(name)                              
                                             
            self.cursor.execute(f"SELECT * FROM {name}")
            filas=[]
            resultados = self.cursor.fetchall()
            for fila in resultados:
                filas.append(fila)
                print(fila)
        except Exception as e:
            print(f"Error: {e}")
            
        return filas
         
         
    def Actualizar(self, name,dato,condicion):
        
        name=sanitizar(name)
        dato=sanitizar(dato)
        condicion=sanitizar(condicion)
        
        try:
            self.cursor.execute(f"UPDATE {name} SET {dato} WHERE {condicion} ")
            self.cursor.commit()
        except Exception as e:
           print(f"Error: {e}")
        print("Exito al actualizar")
           
           
    def Cerrar(self):
        try:            
            self.conexion.close()
        except Exception as e:
            print(f"Error: {e}")
        print("Conexion cerrada con exito")
        
db=IniciarBD("user")
db.CrearTabla("users","user TEXT NOT NULL")
db.InsertarDatos("users","user","Elvin@hotmail.com")
db.ConsultarDatos("users")
db.Cerrar()
