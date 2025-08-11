import time

def sanitizar(objetivo):
    
    try:
        #################################################################################################################################################################################################################################################################################        
        lista_de_peligro=["SELECT","S E L E C T","D R O P","sElEcT","dRoP","WHERE","DROP","UPDATE","OR","AND","--","/*","*/",";","'","%",'"',"/","UNION","U N I O N", "uNiOn", "JOIN","J O I N","jOiN", "FROM","F R O M","fRoM", "SCRIPT","S C R I P T","sCrIpT", "<", ">", "{", "}"]
        lista_de_emails=["@gmail.com","@hotmail.com","@uni.edu.cu"]
        #posibles_malas_entradas=["@.com","@gmal.com","@gmil.com","@gmail.con","@hotmail.con"]
        lista_de_fracmentos=["mail","hot","edu","uni","@",".com","gmai","@gmail",".cu"]
        #################################################################################################################################################################################################################################################################################
        
        
        
        
        
        
        
        """              CAPA: 1           """
        #####################################################
        
        if type(objetivo)==tuple:
            
            print("CAPA 1")
            
            objetivos=[]
            
            for i in objetivo:
                
                i=sanitizar(i)
                
                objetivos.append(i)
                
            objetivo=tuple(objetivos)
                             
        #####################################################
               
               
               
               
               
               
        """              CAPA: 2           """                
        #####################################################
        
        if type(objetivo)!=tuple and "@" in objetivo and (".com" in objetivo or ".cu" in objetivo):
            
            print("CAPA 2")
            
            for email in lista_de_emails:
                
                if email in objetivo:
                    
                    direccion=email
                    
                    nombre=objetivo.replace(direccion,"")
                    
                    nombre=sanitizar(nombre)
            
                    objetivo=f"'{nombre}'{direccion}"
                    
                    objetivo=objetivo.replace(" ","")
                                        
                    break
                else:
                    continue
       
        #####################################################






     
                         
        """              CAPA: 3           """                 
        #####################################################
        
        if type(objetivo)!=tuple and "@" not in objetivo:
            
            print("CAPA 3")
            
            for peligro in lista_de_peligro:
                
                if peligro in objetivo.upper():
                    
                    objetivo=objetivo.replace(peligro.upper(),"")
                    
                    
                    print("ALERTA POSIBLE ATAQUE")
                    
                    time.sleep(1)
                    
                    print("SE HA LIMPIADO SU ENTRADA POR SEGURIDAD")
        #####################################################                 
                    
        
        
        """CAPA DEL PANICO"""#SALTA SOLO SI SE ENCUENTRA ALGO DE LA LISTA DE PELIGROS
        #########################################################################################################################################################################################################            
        
        if (type(objetivo)!=tuple and "@" in objetivo) and (".com" not in objetivo and ".cu" not in objetivo):
            
            print("CAPA DEL PANICO")
            
            objetivo=sanitizar(objetivo)
            
        ###########################################################################################################################################################################################################              
    
        """COMPROBACIONES ADICIONALES"""
        ###############################################################################
        
        if type(objetivo)!=tuple and "@" in objetivo:
            
            print("CAPA ADICIONAL")
            
            contador=0
            
            for email_valido in lista_de_emails:
                
                if email_valido not in objetivo:
                    
                    contador+=1
                    
            if contador==len(lista_de_emails):
                print("EMIL NO VALIDO")       
                for fracmento in lista_de_fracmentos:
                    if fracmento in objetivo:
                        objetivo=objetivo.replace(fracmento,"")
                objetivo=sanitizar(objetivo)
                
        ###############################################################################
    except Exception as e:
        
        print(f"Error: {e}")
    
    return objetivo