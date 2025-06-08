#simpleSQL

class InitDataBase:
    def __init__(self,name):
        import sqlite3
        self.name=name
        self.conexion = sqlite3.connect(self.name)
        self.cursor = self.conexion.cursor()
        
        
        
    def CrearTabla(self, name, *campos):
        name=name
        campos=',\n '.join(campos)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY AUTOINCREMENT,{campos})")
        
        
    
    def InsertarDatos(self, name, campos, *valores):
        placeholders = ', '.join(['?'] * len(valores))
        self.cursor.execute(f"INSERT INTO {name} {campos} VALUES ({placeholders})", valores)
        self.conexion.commit()

    def EliminarTabla(self, name):
         self.cursor.execute(f"DROP TABLE IF EXISTS {name}")
   
        
    def ConsultarDatos(self,name):
        self.cursor.execute(f"SELECT * FROM {name}")
        resultados = self.cursor.fetchall()
        for fila in resultados:
            print(fila) 
            
         
         
    def Cerrar(self):
        self.conexion.close()
