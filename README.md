# jupyter-neuroglancer

Simple Jupyter (and jupyter-server-proxy) integration with [neuroglancer](https://github.com/google/neuroglancer).

Pops up a neuroglancer viewer in a split pane in JupyterLab (via [jupyterlab-sidecar](https://github.com/jupyter-widgets/jupyterlab-sidecar))
so you can more easily see real-time live visualizations driven by your python code.

When running on a remote JupyterHub, the viewer is automatically (and securely) proxied through
[jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy/) so users get the exact
same experience on theier local machine as well as a JupyterHub.

## Installation

`jupyter-neuroglancer` is available on [PyPI](https://pypi.org/project/jupyter-neuroglancer/).

```bash
pip install jupyter-neuroglancer
```

## Usage

`jupyter_neuroglancer` provides a `display_in_sidecar` function that accepts a regular `neuroglancer` `Viewer`
object. You don't have to modify your `neuroglancer` code in any way!

```python
import neuroglancer
from jupyter_neuroglancer import SidecarViewer

# Create a neuroglancer Viewer instance. This controls the visualization
viewer = neuroglancer.Viewer()

# Display the neuroglancer in JupyterLab as a sidecar
display_in_sidecar(viewer)
```

## Using on a JupyterHub

When using this on a JupyterHub, you need [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy/)
installed in the image you are using. Since `neuroglancer` uses eventstreams for communication, you need it
to be a version of `jupyter-server-proxy` that has [this PR](https://github.com/jupyterhub/jupyter-server-proxy/pull/479)
included. Until that PR is merged and released, you can install that with:

```bash
pip install --upgrade git+https://github.com/ganisback/jupyter-server-proxy@support-stream
```

Other than that, you do not have to modify your code in any way.