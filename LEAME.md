# Math’s Rocks Suite  🧮

Suite matemática modular basada en Docker y potenciada por Jupyter.  
Ofrece entornos aislados para múltiples lenguajes científicos (Python, Julia, R, Octave, GAP y más), permitiendo flujos reproducibles y multilenguaje para investigación, educación y experimentación.

---

## 🚀 Vision

Crear un entorno unificado, reproducible y extensible donde herramientas matemáticas de distintos ecosistemas puedan convivir y usarse de forma integrada mediante Jupyter.

---

## 🧱 Architecture General

Este repositorio inicia con un enfoque backend‑first:

- Entornos modulares basados en Docker  
- Jupyter como punto central de acceso  
- Módulos independientes por lenguaje  
- Volúmenes compartidos para notebooks y datos  
- Separación clara entre configuración, scripts y servicios  

---

## 🧬 Arquitectura Híbrida (Estado Actual) 🧩

Math’s Rocks Suite utiliza un modelo híbrido que combina:

- JupyterLab como interfaz unificada
- Scientific Module (Python) como entorno principal
- Módulos independientes para lenguajes especializados
- Frontends propios (RStudio, Sage Notebook) cuando aportan valor
- Kernels remotos para integración dentro de JupyterLab

### Por qué híbrida?
Este enfoque permite avanzar rápido hoy, mientras se construye una arquitectura totalmente modular para el futuro.

---

## 📦 Estructura del Repositorio (inicial)

```text
maths-rocks-suite/
├── docker/
│   └── base/
│   ├── jupyterlab/
│   ├── sagemath/
│   ├── octave/
│   └── ...
├── config/
│   ├── jupyter/
│   └── jupyterlab/
├── scripts/
├── notebooks/
│   └── examples/
├── data/
├── docs/
└── docker-compose.yml
```

---

## 🧪 Scientific Module (Python + Julia + R) 🐍 🔬 🧬 📊 🧠

El Módulo Científico  es el **núcleo actual** de la suite, ofrece un entorno científico basado en Python, construido sobre la imagen `datascience-notebook`. Incluye cómputo numérico, matemáticas simbólicas, estadística, visualización, modelado probabilístico e integración con JupyterLab.

### 📦 Stack científico incluido

- NumPy
- SciPy
- SymPy
- Pandas
- Matplotlib
- Seaborn
- Scikit‑Learn
- Statsmodels
- Plotly
- Bokeh
- NetworkX
- Numba
- Mpmath
- PyMC
- ipywidgets / ipympl
- jupyterlab-git
- and others

Este módulo actúa como:

- Entorno Python completo
- Hub de JupyterLab
- Base para kernels remotos

En el futuro, este módulo se reducirá a Python puro, mientras Julia y R migran a módulos independientes.

Todas las dependencias se administran a traves del archivo `requirements.txt`.