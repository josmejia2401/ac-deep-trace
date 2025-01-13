# Estándar de Desarrollo y Nombramiento en Python

## **1. Estilo de Código: Seguir PEP 8**
Python Enhancement Proposal 8 (PEP 8) es la guía oficial de estilo de código para Python. Algunos puntos clave:

- **Indentación**: Usa 4 espacios por nivel de indentación (no uses tabuladores).
- **Longitud de líneas**: Máximo 79 caracteres por línea.
- **Espacios alrededor de operadores**: Usa espacios alrededor de operadores aritméticos (`a + b`) y después de comas.
- **Cadenas de documentación (docstrings)**: Usa triple comillas (`"""`) para documentar funciones, clases y módulos.
- **Estructura del archivo**: Ordena las importaciones (módulos estándar, módulos de terceros, módulos locales) y agrúpalos.

```python
# Importaciones organizadas
import os
import sys

from third_party_library import module
from my_project.module import function
```

---

## **2. Convenciones de Nombramiento**

### **2.1. Variables y Funciones**
- Usa **snake_case**: palabras separadas por guiones bajos.
  - Ejemplo: `calculate_total`, `user_data`.
- Nombres claros y descriptivos.
  - Malo: `x = 5` (si no es obvio qué representa).
  - Bueno: `total_amount = 5`.

### **2.2. Clases**
- Usa **CamelCase**: palabras con iniciales en mayúsculas, sin guiones bajos.
  - Ejemplo: `UserModel`, `DataProcessor`.

### **2.3. Constantes**
- Usa **UPPER_SNAKE_CASE**: todo en mayúsculas, separado por guiones bajos.
  - Ejemplo: `MAX_RETRIES`, `DEFAULT_TIMEOUT`.

### **2.4. Módulos y Paquetes**
- Usa **snake_case**: nombres cortos y descriptivos.
  - Ejemplo: `data_parser.py`, `image_utils.py`.
- Evita usar caracteres especiales o números al inicio.

### **2.5. Métodos Privados y Variables Internas**
- Prefija con un guion bajo (`_`):
  - Ejemplo: `_calculate_total`.

### **2.6. Métodos y Clases Especiales (dunder)**
- Métodos como `__init__` o `__str__` están reservados. Usa únicamente los que son estándar en Python.

---

## **3. Organización del Proyecto**

### **3.1. Estructura de Carpetas**
Un proyecto típico en Python debería seguir esta estructura:

```
my_project/
│
├── my_project/          # Código fuente del proyecto
│   ├── __init__.py      # Indica que es un paquete
│   ├── main.py          # Punto de entrada del proyecto
│   ├── module1.py       # Módulos individuales
│   ├── module2.py
│   ├── utils/           # Utilidades o funciones auxiliares
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── validators.py
│   └── config/          # Configuración del proyecto
│       ├── __init__.py
│       ├── settings.py
│       └── secrets.py
│
├── tests/               # Pruebas del proyecto
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
│
├── docs/                # Documentación (opcional)
│   ├── README.md
│   └── API.md
│
├── requirements.txt     # Dependencias del proyecto
├── setup.py             # Configuración para empaquetado e instalación
├── .gitignore           # Archivos y carpetas ignorados por Git
├── README.md            # Descripción general del proyecto
└── LICENSE              # Licencia del proyecto
```

### **3.2. Archivo `__init__.py`**
Incluye un archivo vacío llamado `__init__.py` en cada paquete para indicar que es un paquete de Python.

---

## **4. Documentación y Comentarios**

- Usa **docstrings** para documentar funciones, clases y módulos.
- Ejemplo de docstring para una función:

```python
def calculate_total(price, tax):
    """
    Calcula el total a pagar incluyendo impuestos.

    Args:
        price (float): Precio del producto.
        tax (float): Porcentaje del impuesto.

    Returns:
        float: Total a pagar.
    """
    return price * (1 + tax)
```

---

## **5. Buenas Prácticas Generales**

- **Funciones pequeñas**: Mantén funciones y métodos cortos y con una única responsabilidad.
- **Evita hardcoding**: Usa constantes para valores que podrían cambiar en el futuro.
- **Tipado explícito**: Utiliza anotaciones de tipos para mayor claridad.

```python
def greet_user(name: str) -> str:
    return f"Hello, {name}!"
```

- **Linter y Formateador**: Usa herramientas como `flake8`, `black` o `pylint` para garantizar un código limpio.

---

## **6. Reglas de Versionado**
- Utiliza [SemVer](https://semver.org/) para el versionado:
  - **MAJOR.MINOR.PATCH** (1.0.0, 1.1.0, 1.1.1).
  - Incrementa `MAJOR` para cambios incompatibles, `MINOR` para nuevas funcionalidades y `PATCH` para correcciones.
