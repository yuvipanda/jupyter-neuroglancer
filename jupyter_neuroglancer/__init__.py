from sidecar import Sidecar
from IPython.display import IFrame, display
import os
from urllib.parse import urlparse


def display_in_sidecar(viewer):
    viewer_url = viewer.get_viewer_url()
    if "JUPYTERHUB_SERVICE_PREFIX" in os.environ:
        # We're running in a JupyterHub
        try:
            import jupyter_server_proxy
        except ImportError:
            raise ImportError(
                "The jupyter-server-proxy package (with this PR included: https://github.com/jupyterhub/jupyter-server-proxy/pull/479) must be installed when running on a JupyterHub"
            )

        parts = urlparse(viewer_url)
        base_url = os.environ["JUPYTERHUB_SERVICE_PREFIX"]  # Contains trailing slash
        iframe_url = f"{base_url}proxy/{parts.port}{parts.path}"
    else:
        iframe_url = viewer_url

    with Sidecar():
        frame = IFrame(iframe_url, width="100%", height="100%")
        display(frame)
