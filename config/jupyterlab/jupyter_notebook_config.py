# ============================================================
# JupyterLab Configuration — Math's Rock's Suite
# ============================================================

c = get_config()

# Seguridad: token en lugar de contraseña
c.ServerApp.token = "maths-rocks-2026"
c.ServerApp.password = ""

# Acceso desde red local
c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = 8888
c.ServerApp.open_browser = False

# Directorio de trabajo
c.ServerApp.root_dir = "/home/jovyan/work"

# Permitir acceso sin SSL en red local
c.ServerApp.allow_origin = "*"
c.ServerApp.allow_credentials = True

# Interfaz Lab como predeterminada
c.ServerApp.default_url = "/lab"

# Desactivar advertencias de seguridad para uso local
c.ServerApp.disable_check_xsrf = False

# Tamaño máximo de contenido
c.ServerApp.max_body_size = 536870912  # 512 MB

# Extensiones
c.LabApp.check_for_updates_class = "jupyterlab.NeverCheckForUpdate"