# 📝 Django CRUD

Un proyecto desarrollado con **Django** que implementa las operaciones básicas de un sistema CRUD (Crear, Leer, Actualizar y Eliminar registros).

## 📋 Características

- ✅ Crear registros
- 📖 Listar registros
- ✏️ Editar registros existentes
- ❌ Eliminar registros
- 🔍 Validación de formularios
- 🎨 Interfaz con Bootstrap
- 🗄️ Base de datos SQLite (por defecto)
- 🔐 Panel de administración de Django

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Django 5.x
- HTML5
- CSS3
- Bootstrap 5
- SQLite

## 📂 Estructura del proyecto

```
django-crud/
│
├── crud/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── proyecto/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/django-crud.git
```

### 2. Entrar al proyecto

```bash
cd django-crud
```

### 3. Crear un entorno virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

## 📸 Capturas de pantalla

Puedes agregar imágenes del proyecto aquí.

```
docs/
├── inicio.png
├── crear.png
├── editar.png
└── eliminar.png
```

Ejemplo:

```markdown
![Inicio](docs/inicio.png)
```

## ⚙️ Funcionalidades

- Gestión completa de registros.
- Formularios con validaciones.
- Navegación sencilla.
- Diseño responsive.
- Administración desde Django Admin.

## 📁 Base de datos

El proyecto utiliza **SQLite** por defecto, aunque puede configurarse para trabajar con:

- PostgreSQL
- MySQL
- MariaDB
- Oracle

Modificando el archivo:

```
proyecto/settings.py
```

## 🧪 Ejecutar pruebas

```bash
python manage.py test
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas.

1. Haz un Fork.
2. Crea una rama.

```bash
git checkout -b feature/nueva-funcionalidad
```

3. Realiza tus cambios.

4. Haz commit.

```bash
git commit -m "Agrega nueva funcionalidad"
```

5. Envía los cambios.

```bash
git push origin feature/nueva-funcionalidad
```

6. Abre un Pull Request.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

## 👨‍💻 Autor

**Tu Nombre**

GitHub: https://github.com/tu-usuario

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub.
