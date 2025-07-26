# SimpleSQL: Haz SQLite fácil ✨

![SimpleSQL Logo](https://img.shields.io/badge/Hecho%20con-Pydroid%203-blue?logo=android) ![Python Version](https://img.shields.io/badge/Python-3.8+-blue?logo=python)

**SimpleSQL** es una herramienta que creé para hacer más fácil trabajar con bases de datos SQLite, especialmente cuando estás empezando con Python. Lo desarrollé principalmente en mi teléfono Samsung S8 usando Pydroid 3 mientras aprendía a programar.

## 🧒 Mi historia: Programando desde el móvil

"Soy Elvin, tengo 16 años y llevo poco más de un año aprendiendo Python. Como no tenía computadora, desarrollé SimpleSQL en mi teléfono usando Pydroid 3. Es mi primer proyecto 'serio' y aunque no es perfecto, funciona y me ayudó mucho a entender bases de datos."

## ❓ ¿Para qué sirve SimpleSQL?

Cuando empecé con SQLite, me frustraba tener que escribir tanto código repetitivo. SimpleSQL simplifica:

```python
# Sin SimpleSQL
cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", ("Ana",))

# Con SimpleSQL
db.CrearTabla("usuarios", "nombre TEXT")
db.InsertarDatos("usuarios", "nombre", "Ana")
```

## 🛠️ ¿Qué puedes hacer?

| Operación | Ejemplo |
|-----------|---------|
| Crear tabla | `db.CrearTabla("amigos", "nombre TEXT", "edad INT")` |
| Insertar datos | `db.InsertarDatos("amigos", "nombre,edad", "Juan", 15)` |
| Consultar | `db.ConsultarDatos("amigos")` |
| Actualizar | `db.Actualizar("amigos", "edad=16", "nombre='Juan'")` |
| Borrar tabla | `db.EliminarTabla("amigos")` |

## 🔒 Protección básica

Añadí un sistema simple para bloquear intentos de inyección SQL:

```python
# Si alguien intenta esto:
db.ConsultarDatos("usuarios; DROP TABLE usuarios;--")

# SimpleSQL lo convierte en:
db.ConsultarDatos("usuarios DROP TABLE usuarios")
```

## 📦 Cómo usar

1. Descarga `simple_sql.py` y `sanitizar.py`
2. En tu código:

```python
from simple_sql import IniciarBD

# Crea o conecta a una base de datos
db = IniciarBD("mi_base.db")

# Crea una tabla de juegos
db.CrearTabla("juegos", "nombre TEXT", "puntaje INT")

# Añade tu puntaje
db.InsertarDatos("juegos", "nombre,puntaje", "MiJuego", 100)

# Ver todos los puntajes
db.ConsultarDatos("juegos")
```

## 🧪 Pruebas

Incluyo pruebas para asegurarme que todo funciona bien. Para ejecutarlas:

```bash
python -m unittest discover -s tests
```

> Las pruebas las hice con ayuda de DeepSeek-R1, un asistente de IA que me ayudó a crear casos de prueba completos.

## 📱 ¿Por qué móvil?

- No tenía computadora propia
- Pydroid 3 me permitió programar en cualquier lugar
- Quería demostrar que no necesitas equipo caro para crear cosas interesantes

## 💌 ¿Preguntas o sugerencias?

Si tienes dudas o ideas para mejorar SimpleSQL, escríbeme a elvinfelipetorres@gmail.com o abre un issue aquí en GitHub. ¡Estoy aprendiendo y agradezco toda ayuda!

---

**SimpleSQL** - Hecho con 💚 por un estudiante de 16 años en Cuba  
*¿Quién dijo que necesitas una supercomputadora para programar?* 😊
