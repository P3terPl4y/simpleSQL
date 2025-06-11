class InitDataBase:
    def __init__(self,name):
        try:
            import sqlite3
            self.name=name
            self.conexion = sqlite3.connect(self.name)
            self.cursor = self.conexion.cursor()
            with open("BD_Rejistro.txt","w") as f:
                f.write(self.name)
        except Exception as e:
            print(f"Error: {e}")
        
        
        
    def CrearTabla(self, name, *campos):
        try:
            name=name
            campos=', '.join(campos)
            
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY AUTOINCREMENT,{campos})")
            print_campos="  ".join(campos.split())
            print(print_campos)
        except Exception as e:
            print(f"Error: {e}")
        
        
    
    def InsertarDatos(self, name, campos, *valores):
        try:
            placeholders = ', '.join(['?'] * len(valores))
            self.cursor.execute(f"INSERT INTO {name} {campos} VALUES ({placeholders})", valores)
            self.conexion.commit()
        except Exception as e:
            print(f"Error: {e}")                
        

    def EliminarTabla(self, name):
         try:
             self.cursor.execute(f"DROP TABLE IF EXISTS {name}")
         except Exception as e:
             print(f"Error: {e}")

      
        
    def ConsultarDatos(self,name):
        import time
        try:
            if "=" in name:
                name=name.replace("=", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)
                    
            elif "-" in name:
                name=name.replace("-", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)
            
            elif "." in name:
                name=name.replace(".", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)

            elif "'" in name:
                name=name.replace("'", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)    
               
            elif "WHERE" in name:
                name=name.replace("WHERE", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)
           
            elif ";" in name:
                name=name.replace(";", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)
           
            elif "/" in name:
                name=name.replace("/", "")
                print("No intentes SQLinjection por favor \nEspera unos segundos")
                time.sleep(3)                              
                                             
            self.cursor.execute(f"SELECT * FROM {name}")
            filas=""
            resultados = self.cursor.fetchall()
            for fila in resultados:
                filas+=f"{fila}\n"
            print(filas) 
        except Exception as e:
            print(f"Error: {e}")     
         
         
         
    def Actualizar(self, name,dato):
        try:
            self.cursor.execute(f"UPDATE {name} SET {dato} WHERE 1==1")
        except Exception as e:
           print(f"Error: {e}")
           
           
           
    def Cerrar(self):
        try:            
            self.conexion.close()
        except Exception as e:
            print(f"Error: {e}")