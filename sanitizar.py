def sanitizar(objetivo):
    try:
        
        lista_de_peligro=["SELECT","WHERE","DROP","UPDATE","OR","AND","--","/*","*/",";","'",'"',"/",".","UNION", "JOIN", "FROM", "SCRIPT", "<", ">", "{", "}"]
        
        if type(objetivo)==tuple:
            objetivos=[]
            for i in objetivo:
                i=sanitizar(i)
                objetivos.append(i)
                
                objetivo=tuple(objetivos)
                
                
        for i in lista_de_peligro:
            if type(objetivo)!=tuple:
                if i in objetivo.upper() and "@gmail.com" not in objetivo and "@hotmail.com" not in objetivo and "@uni.edu.cu" not in objetivo:
                    objetivo=objetivo.replace(i.upper(),"")
    except Exception as e:
        print(f"Error: {e}")
    return objetivo
