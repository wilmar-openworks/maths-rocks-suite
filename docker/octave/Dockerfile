# Usamos la imagen oficial de Octave (basada en Debian)
FROM gnuoctave/octave:latest

# Cambiamos a root para instalar paquetes
USER root

# 1. Instalamos Python y dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Creamos el entorno virtual e instalamos Jupyter + Kernel
# Usamos un venv para seguir las buenas prácticas actuales de Python
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --quiet \
    octave_kernel \
    jupyter \
    jupyterlab

# 3. Preparamos el directorio de trabajo (coincide con tu docker-compose)
RUN mkdir -p /root/octave/notebooks
RUN mkdir -p /root/octave/data
WORKDIR /root/octave/notebooks

# Exponemos el puerto
EXPOSE 8888

# Comando de inicio
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=maths-rocks-2026", "--notebook-dir=/root/octave/notebooks"]
