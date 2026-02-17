# Math’s Rocks Suite  🧮

**English**  
A modular mathematical computing suite built with Docker and powered by Jupyter.  
It provides isolated environments for multiple scientific languages (Python, Julia, R, Octave, GAP and more), enabling reproducible, multi‑language workflows for research, education and experimentation.

**Español**  
Suite matemática modular basada en Docker y potenciada por Jupyter.  
Ofrece entornos aislados para múltiples lenguajes científicos (Python, Julia, R, Octave, GAP y más), permitiendo flujos reproducibles y multilenguaje para investigación, educación y experimentación.

---

## 🚀 Vision

**English**  
Create a unified, reproducible and extensible environment where mathematical tools from different ecosystems can coexist and be used seamlessly through Jupyter.

**Español**  
Crear un entorno unificado, reproducible y extensible donde herramientas matemáticas de distintos ecosistemas puedan convivir y usarse de forma integrada mediante Jupyter.

---

## 🧱 Architecture (Base)

**English**  
This repository starts with a backend‑first approach:
- Docker‑based modular environments  
- Jupyter as the central access point  
- Independent language modules  
- Shared volumes for notebooks and data  
- Clean separation between configuration, scripts and services  

**Español**  
Este repositorio inicia con un enfoque backend‑first:
- Entornos modulares basados en Docker  
- Jupyter como punto central de acceso  
- Módulos independientes por lenguaje  
- Volúmenes compartidos para notebooks y datos  
- Separación clara entre configuración, scripts y servicios  

---

## 📦 Repository Structure (initial)

```text
maths-rocks-suite/
├── docker/
│   └── base/
├── config/
│   └── jupyter/
├── scripts/
├── notebooks/
│   └── examples/
├── docs/
└── docker-compose.yml
```

---

# Git Flow Repository

This repository is using git-flow with the following branches:
- main: Production releases
- develop: Development

---

## 🚀 Quick Start
```bash
docker-compose pull
docker-compose up -d
```

Access Jupyter at http://localhost:8888

---

## 🛠 Features (current)

- Modular backend-first architecture
- JupyterLab as unified interface
- Git-flow development model
- Clean separation of services and configuration
- Python scientific stack

---

## 🧪 Scientific Module (Python) 🐍 🔬 🧬 📊 🧠

**English**
The Scientific Module provides a complete Python-based scientific environment built on top of the `datascience-notebook` image. It includes numerical computing, symbolic math, statistics, visualization, probabilistic modeling and JupyterLab integration.

**Español**
El Módulo Científico ofrece un entorno científico basado en Python, construido sobre la imagen `datascience-notebook`. Incluye cómputo numérico, matemáticas simbólicas, estadística, visualización, modelado probabilístico e integración con JupyterLab.

---

### 📦 Included Scientific Stack

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

All dependencies are managed through `requirements.txt`.

---

### 🐳 Docker Integration

The module is built from:

```
docker/jupyterlab/Dockerfile
docker/jupyterlab/requirements.txt
```

It registers a dedicated Python kernel:

```
Python 3 (Maths Rocks)
```

---

### 🔌 docker-compose Service

The Scientific Module is exposed as the main JupyterLab service:

```yaml
jupyterlab:
  build:
    context: ./docker/jupyterlab
  container_name: maths-rocks-jupyterlab
  ports:
    - "8888:8888"
  volumes:
    - jupyter_data:/home/jovyan/work
    - ./notebooks:/home/jovyan/work/notebooks
    - ./data:/home/jovyan/work/data
    - ./config/jupyterlab/jupyter_lab_config.py:/home/jovyan/.jupyter/jupyter_lab_config.py
```

---

### 🚀 Usage

Start the environment:

```bash
docker-compose up -d --build
```

Access JupyterLab at:

```
http://localhost:8888
```

---

### 📁 Directory Structure

```
docker/
  jupyterlab/
    Dockerfile
    requirements.txt
config/
  jupyterlab/
    jupyter_lab_config.py
notebooks/
data/
```

---

### 🧭 Purpose

This module establishes the foundation for future language environments such as Julia, R, Octave and GAP, following the modular architecture of the suite.

---


## 🧪 Planned Modules (coming soon)

- Julia kernel: High-performance dynamic language for technical computing.
- R kernel
- GNU Octave: High-level language for numerical computations.
- GAP
- SageMath: Unified interface for algebra, geometry, and number theory.
- Custom Kernels: Seamless integration within the JupyterLab environment.

---

## 📦 Installation & Requirements

Docker and Docker Compose.
Clone this repository: 

```bash
git clone https://github.com/wilmar-openworks/maths-rocks-suite
```
Then:
```bash
cd maths-rocks-suite
docker-compose up -d
```

---

## 🤝 Contributing

Contributions are welcome! Please follow the logical commit history established in this repo.

> Please follow the commit style and modular structure established in this repository.

---

### 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details 📜.

---

## 📅 Roadmap (short)

- ✅ Add base Docker + Jupyter environment
- 🚧 Add Python scientific stack (Scientific Module)
- ⏳ Add Julia kernel
- ⏳ Add R kernel
- ⏳ Add Octave and GAP
- ⏳ Improve documentation and examples
- ⏳ Add dashboard module

### Status

- ✅ Completed
- 🚧 In progress
- ⏳ Pending
- ❌ Not started

