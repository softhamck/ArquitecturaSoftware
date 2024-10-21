# Proyecto de Registro de Usuarios con Arquitectura en Capas y Patrones de Diseño

## Descripción del Proyecto

Este proyecto es una aplicación sencilla que permite registrar y mostrar usuarios en una base de datos. Se utiliza una arquitectura de software en capas, implementando varios patrones de diseño (creacionales, estructurales y de comportamiento) para demostrar cómo estos patrones resuelven problemas comunes en el desarrollo de software. Los usuarios registrados pueden ser de dos tipos: **Administrador** y **Regular**.

### Características:
- Registro de usuarios con diferentes roles.
- Notificación cuando un usuario es creado correctamente.
- Base de datos SQLite para almacenar la información de los usuarios.
- Implementación de varios patrones de diseño.
  
## Arquitectura

El proyecto sigue una arquitectura de **capas**, que organiza el código en diferentes niveles de responsabilidad:

1. **Capa de Presentación**: Muestra la interfaz de usuario y el punto de entrada de la aplicación (`main.py`).
2. **Capa de Lógica de Negocio**: Gestiona la creación de usuarios y la lógica relacionada (`user_service.py`).
3. **Capa de Acceso a Datos**: Se encarga de la conexión y manejo de la base de datos (`database.py`).
4. **Capa de Patrones de Diseño**: Implementa los patrones de diseño utilizados en la aplicación (`factory.py`, `observer.py`, `adapter.py`).

## Patrones de Diseño Implementados

1. **Patrones Creacionales**:
   - **Factory Method**: Para la creación de usuarios (`UserFactory`).
   - **Singleton**: Puede ser implementado en el manejo de conexiones a la base de datos si se desea una única instancia.
   
2. **Patrones de Comportamiento**:
   - **Observer**: Notifica cuando un nuevo usuario es creado exitosamente (`UserObserver`).
   - **Strategy**: Podría implementarse en futuros cambios para manejar diferentes estrategias de almacenamiento o autenticación.

3. **Patrones Estructurales**:
   - **Adapter**: Permite la integración de diferentes bases de datos (ej. MySQL o SQLite) a través de una interfaz común (`DataBaseAdapter`, `MySQLAdapter`).

## Requisitos

Para ejecutar este proyecto necesitas:

- Python 3.8 o superior
- Paquete `sqlite3` (ya incluido en Python por defecto)

### Instalación de Dependencias

Instala las dependencias necesarias con el siguiente comando:

```bash
pip install -r requirements.txt
```

##  Ejecución del Proyecto

1. Clona este repositorio o descárgalo en tu máquina local.

2. Navega hasta la raíz del proyecto y crea un entorno virtual con el siguiente comando:

```bash
python -m venv venv
```
3. Crear entorno virtual

```bash
venv\Scripts\activate
```

4. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

5. Ejecuta el archivo principal:

```bash
python myApp/presentation/main.py
```

Esto creará la base de datos si aún no existe, registrará algunos usuarios y mostrará los usuarios almacenados.


Este proyecto es parte de un ejercicio académico para la implementación de arquitectura en capas y patrones de diseño en software.