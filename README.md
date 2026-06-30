# CRM Django - Gestión de clientes

Aplicación web CRM desarrollada con Django para administrar registros de clientes, permitir el acceso de usuarios regulares a un portal de cliente y ofrecer un flujo básico de creación, edición, visualización y eliminación de registros.

## 🚀 Características principales

- Registro e inicio de sesión de usuarios.
- Panel de administración para gestionar clientes.
- Portal específico para usuarios clientes.
- CRUD completo de registros de clientes.
- Diseño responsive con Bootstrap y crispy-forms.
- Soporte para MySQL cuando está disponible, con fallback automático a SQLite.

## 🧰 Tecnologías utilizadas

- Python 3.11+
- Django 5.0
- SQLite / MySQL
- Bootstrap 5 (a través de crispy-bootstrap5)
- Django Crispy Forms
- Django Import Export
- Django Filters

## 📁 Estructura del proyecto

```text
.
├── requirements.txt
├── dcrm/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── dcrm/                 # configuración principal del proyecto
│   └── website/              # app principal del CRM
│       ├── forms.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
```

## ⚙️ Requisitos previos

- Python 3.11 o superior
- pip
- MySQL (opcional, si deseas usarla como base de datos principal)

## 🔧 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

2. Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Entra al directorio del proyecto Django:

```bash
cd dcrm
```

5. Ejecuta las migraciones:

```bash
python manage.py migrate
```

6. Crea un superusuario para acceder al panel administrativo:

```bash
python manage.py createsuperuser
```

7. Inicia el servidor:

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000
```

## 🗄️ Configuración de la base de datos

El proyecto está configurado para usar MySQL si el servicio está disponible en `localhost:3306`, con estos valores por defecto:

- Base de datos: `clientes`
- Usuario: `root`
- Contraseña: vacía
- Puerto: `3306`

Si no encuentra MySQL disponible, el sistema utiliza automáticamente SQLite mediante `db.sqlite3`.

> Si deseas cambiar la configuración, edita el archivo [dcrm/dcrm/settings.py](dcrm/dcrm/settings.py).

## 👤 Uso básico

- Accede a `/register/` para crear una nueva cuenta.
- Un usuario normal entra al portal de cliente en `/client_home/`.
- Un administrador puede gestionar registros desde la interfaz principal.
- Las rutas principales incluyen:
  - `/` → home
  - `/add_record/` → agregar cliente
  - `/update/<id>/` → editar cliente
  - `/record/<id>/` → ver detalle del cliente
  - `/delete/<id>/` → eliminar cliente

## 🧪 Pruebas

Para ejecutar la suite de pruebas:

```bash
python manage.py test
```

## 📌 Notas importantes

- El proyecto usa un flujo simple de autenticación basado en usuarios de Django.
- Los administradores tienen acceso a operaciones de gestión, mientras que los usuarios normales solo visualizan el portal cliente.
- Puedes adaptar el sistema para agregar más campos o flujos de negocio según la necesidad.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si quieres mejorar el proyecto:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad.
3. Realiza tus cambios.
4. Abre un pull request.
