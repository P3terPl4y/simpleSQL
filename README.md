
---

# **Documentación de simpleSQL**  
### *Framework minimalista para SQLite3 en Python*  
**Versión**: v0.1-beta · **Autor**: [P3terPl4y](https://github.com/P3terPl4ay) · **Licencia**: MIT  

---

## **📌 1. Introducción**  
**simpleSQL** nace para eliminar la complejidad de SQLite3, ofreciendo métodos intuitivos en español que abstraen operaciones CRUD. Ideal para:  
- Prototipos rápidos.  
- Proyectos pequeños que valoran simplicidad.  
- Devs hispanohablantes.  

**Filosofía clave**:  
```python  
# Menos esto:  
cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (1, "Pedro"))  

# Más esto:  
db.InsertarDatos("usuarios", 1, "Pedro")  
```  

---

## **🔧 2. Instalación**  
### Requisitos:  
- Python 3.6+.  
- SQLite3 (incluido en Python).  

### Opciones:  
1. **Clonar repositorio**:  
   ```bash  
   git clone https://github.com/P3terPl4y/simpleSQL.git  
   cd simpleSQL  
   ```  
2. **Instalar manualmente**:  
   Copia el archivo `simpleSQL.py` a tu proyecto.  

---

## **🚀 3. Uso básico**  
### **Inicialización**  
```python  
from simpleSQL import InitDataBase  

# Crear/conectar a una base de datos  
db = InitDataBase("mi_db.db")  
```  

### **Métodos principales**  
| Método               | Parámetros                  | Ejemplo                          |  
|-----------------------|-----------------------------|----------------------------------|  
| `CrearTabla()`        | `nombre_tabla, [columnas]`  | `db.CrearTabla("usuarios", ["id INTEGER", "nombre TEXT"])` |  
| `InsertarDatos()`     | `tabla, *valores`           | `db.InsertarDatos("usuarios", 1, "Ana")` |  
| `ConsultarDatos()`    | `tabla, condicion(opcional)` | `db.ConsultarDatos("usuarios", "id = 1")` |  
| `EliminarTabla()`     | `nombre_tabla`              | `db.EliminarTabla("logs_old")` |  

---

## **⚙️ 4. Métodos avanzados**  
### **Transacciones**  
```python  
# Ejecutar múltiples operaciones atómicas  
with db:  
    db.InsertarDatos("ventas", 100, "Producto A")  
    db.InsertarDatos("inventario", -1, "Producto A")  
```  

### **Backup automático**  
```python  
db.GuardarBackup("backup_20250608.db")  
```  

---

## **📜 5. Filosofía y convenciones**  
- **Nombres en español**: Todos los métodos usan español para ser accesibles.  
- **Sin magia oculta**: El código es fácil de leer y modificar.  
- **Crédito**: Si usas simpleSQL, menciona al autor:  
  ```markdown  
  Desarrollado con [simpleSQL](https://github.com/P3terPl4y/simpleSQL) por @P3terPl4y.  
  ```  

---

## **⚠️ 6. Limitaciones**  
- **No es un ORM**: No soporta relaciones complejas o migraciones.  
- **Seguridad**: Usa parámetros internos para evitar SQL injection, pero valida tus inputs.  

---

## **🌍 7. Contribuir**  
¿Quieres mejorar simpleSQL?  
1. Haz fork del repo.  
2. Añade tests para nuevos métodos.  
3. Envía un PR con cambios claros.  

**Roadmap**:  
- [ ] Soporte para transacciones anidadas.  
- [ ] Documentación en inglés.  

---

## **📬 8. Contacto**  
- **Issues en GitHub**: Reporta bugs [aquí](https://github.com/P3terPl4y).  

---  
*"Código simple, vida simple." — P3terPl4y, 2025*  

```

### 📌 **Notas adicionales**:  
1. **Formato**: Usa este archivo como `DOCUMENTACION.md` en la raíz de tu repo.  
2. **Estilo**: Mantén la consistencia con ejemplos en español y código resaltado.  
3. **Personalización**: Añade un logo ASCII si quieres darle identidad.  

¿Necesitas ajustar algo o añadir más detalles? 😊 
