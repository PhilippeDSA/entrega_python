# Mi Proyecto Blog Django

Este proyecto es una aplicación web del tipo blog, desarrollada con Django que tiene lo siguiente:

- Uso de herencia de plantillas HTML para evitar duplicación de código.(muy util la verdad jaja)
- Tres modelos en la base de datos: `Autor`, `Categoria` y `Articulo`.
- Formularios para crear registros en cada uno de estos modelos.
- Formulario para buscar artículos en la base de datos.
- Uso del patrón MVT (Modelo-Vista-Template) característico de Django.

---

## La Estructura del proyecto

- `mi_proyecto/`: Carpeta raíz del proyecto Django.
- `blog/`: Aplicación donde están definidos los modelos, vistas, urls y formularios.
- `templates/`: Contiene las plantillas HTML.
  - `base.html`: Es la plantilla base con estructura común.
  - `crear_autor.html`, `crear_categoria.html`, `crear_articulo.html`: Son los formularios para crear datos.
  - `buscar_articulo.html`: Es el formulario destinado para búsqueda.
- `manage.py`: Es un script para manejar el proyecto (migraciones, servidor, etc.).
- `db.sqlite3`: Es la Base de datos SQLite del proyecto.

---

## Requisitos previos para el correcto uso

- Python 3.x instalado.
- Django instalado (`pip install django`).
- (Opcional) Entorno virtual para aislar dependencias.

---

Fue un placer hacer este trabajo, hubo contratiempos pero supimos sobrellevarlos. 
Saludos Cordiales.