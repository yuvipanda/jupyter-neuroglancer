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

## How to use

`jupyter_neuroglancer` provides a `SidecarViewer` class that accepts a regular `neuroglancer` `Viewer`
object. You don't have to modify your `neuroglancer` code in any way!

```python
import neuroglancer
from jupyter_neuroglancer import SidecarViewer

# Create a neuroglancer Viewer instance. This controls the visualization
viewer = neuroglancer.Viewer()

# Create a SidecarViewer that can show / hide the sidecar panel
scv = SidecarViewer(viewer)

# Show the panel
scv.show()

# Hide the panel
scv.hide()
```
