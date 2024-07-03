from sidecar import Sidecar
from IPython.display import IFrame, display
import os
from urllib.parse import urlparse

class SidecarViewer:
    def __init__(self, viewer):
        self.viewer = viewer
        self.sidecar = Sidecar()
        self.is_visible = False

        if "JUPYTERHUB_SERVICE_PREFIX" in os.environ:
            # We're running in a JupyterHub
            self.use_proxy = True
        else:
            self.use_proxy = False

    def __enter__(self):
        return self.sidecar.__enter__()

    def __exit__(self):
        return self.sidecar.__exit__()

    def get_accessible_viewer_url(self):
        viewer_url = self.viewer.get_viewer_url()
        if not self.use_proxy:
            return viewer_url

        try:
            import jupyter_server_proxy
        except ImportError:
            raise ImportError("The jupyter-server-proxy package (with this PR included: https://github.com/jupyterhub/jupyter-server-proxy/pull/479) must be installed when running on a JupyterHub")

        parts = urlparse(viewer_url)
        base_url = os.environ["JUPYTERHUB_SERVICE_PREFIX"] # Contains trailing slash
        return f"{base_url}proxy/{parts.port}{parts.path}"

    def show(self):
        if not self.is_visible:
            frame = IFrame(self.get_accessible_viewer_url(), width='100%', height='100%')

            self.sidecar.__enter__()
            display(frame)

            self.is_visible = True

    def hide(self):
        if self.is_visible:
            self.sidecar.__exit__()
            self.is_visible = False
