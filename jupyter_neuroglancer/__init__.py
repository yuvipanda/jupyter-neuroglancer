from sidecar import Sidecar
from IPython.display import IFrame, display

class SidecarViewer:
    def __init__(self, viewer):
        self.viewer = viewer
        self.sidecar = Sidecar()

    def __enter__(self):
        return self.sidecar.__enter__()

    def __exit__(self):
        return self.sidecar.__exit__()

    def open(self):
        frame = IFrame(self.viewer.get_viewer_url(), width='100%', height='100%')

        self.sidecar.__enter__()
        display(frame)

    def close(self):
        self.sidecar.__exit__()
