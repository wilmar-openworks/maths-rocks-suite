# docker/sagemath/Dockerfile
FROM sagemath/sagemath:latest

# Install Jupyter kernel for SageMath
RUN sage -pip install --no-cache-dir jupyterlab

# Register SageMath kernel for JupyterLab
RUN sage -python -m sage.repl.ipython_kernel.install --name "sage" --display-name "SageMath" --user

# RUN sage -n jupyter --generate-config --user

# Placeholder for future enhancements RUN echo "SageMath module ready."
RUN echo "SageMath module ready."
