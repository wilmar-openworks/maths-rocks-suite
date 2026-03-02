FROM quay.io/jupyter/datascience-notebook:latest

# Evita prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Instala paquetes científicos pesados mediante archivo de requerimientos
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir --quiet -r /tmp/requirements.txt

# Register Python kernel (usually automatic, but explicit is safer)
RUN python -m ipykernel install --user --name python3 --display-name "Python 3 (Maths Rocks)"

# Placeholder for future enhancements
RUN echo "Python scientific environment ready."

# Asegura que JupyterLab arranque correctamente
CMD ["start-notebook.sh"]
