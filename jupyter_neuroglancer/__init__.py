from sidecar import Sidecar
from IPython.display import IFrame, display

class SidecarViewer:
    def __init__(self, viewer):
        self.viewer = viewer
        self.sidecar = Sidecar()
        self.is_visible = False

    def __enter__(self):
        return self.sidecar.__enter__()

    def __exit__(self):
        return self.sidecar.__exit__()

    def show(self):
        if not self.is_visible:
            frame = IFrame(self.viewer.get_viewer_url(), width='100%', height='100%')

            self.sidecar.__enter__()
            display(frame)

            self.is_visible = True

    def hide(self):
        if self.is_visible:
            self.sidecar.__exit__()
            self.is_visible = False
