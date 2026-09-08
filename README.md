# Laboratorio: API REST de Gestión de Ventas y Productos

Este repositorio contiene la implementación de una API REST para la gestión de productos y ventas, desarrollada como parte del trabajo práctico de la materia **Seminario de Lenguajes: Python** en la **Universidad Nacional de Lanús (UNLa)**.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.12
* **Framework Web:** FastAPI
* **Base de Datos:** SQLite
* **ORM:** SQLAlchemy
* **Validación de Datos:** Pydantic
* **Análisis y Reportes:** Pandas
* **Generación de PDFs:** Borb

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto de manera local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
cd nombre-del-repo
### 2. Creacion del entorno virtual
  python -m venv .venv
.venv\Scripts\activate
### 3. Instalacion de dependencias
  ip install --upgrade pip
  pip install -r requirements.txt
### 4. Ejecucion del servidor FasApi
  uvicorn main:app --reload