# Proyecto Final - Blog en Django

Este es mi proyecto final para el curso, una aplicación web de blog desarrollada con Django. Permite la creación y gestión de artículos, páginas, perfiles de usuario y mensajería interna.

## 🚀 Características principales

- Registro, inicio de sesión y cierre de sesión de usuarios
- Creación, edición y eliminación de artículos
- Buscador de artículos
- Visualización y detalle de artículos
- Creación y visualización de páginas personalizadas (CMS)
- Gestión de perfiles con avatar, bio y fecha de nacimiento
- Envío y recepción de mensajes entre usuarios
- Editor enriquecido con CKEditor para contenido
- Panel de administración de Django para gestión avanzada
- Navegación intuitiva y diseño responsive
- SEO básico y accesibilidad W3C

## 🛠️ Tecnologías utilizadas

- Python 3.13.1
- Django 5.2.1
- SQLite (por defecto)
- HTML5, CSS3, Bootstrap
- CKEditor 5
- Pillow (para manejo de imágenes)
- Django Messages Framework
## 📂 Estructura del proyecto
mi_proyecto/
│
├── blog/ # Aplicación principal
│ ├── templates/blog/ # Plantillas HTML
│ ├── static/ # Archivos estáticos
│ ├── models.py # Modelos de datos
│ ├── views.py # Lógica de vistas
│ ├── urls.py # Rutas internas
│ ├── forms.py # Formularios
│ └── signals.py # Señales para crear perfil automáticamente
│
├── mi_proyecto/ # Configuración del proyecto Django
├── db.sqlite3 # Base de datos local
└── manage.py # Utilidad de línea de comandos de Django

## ✅ Cómo usar este proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/PhilippeDSA/entrega-final-python.git
   cd tu-repo
2. **Crear entorno virtual e instalar dependencias:**
python -m venv env
source env/bin/activate  //Windows env\Scripts\activate
pip install -r requirements.txt
3. **Aplicar migraciones y crear superusuario:**
python manage.py migrate
python manage.py createsuperuser
4. **Correr el servidor:**
python manage.py runserver
5. **Acceder al sitio:**
Abre http://127.0.0.1:8000 en tu navegador.