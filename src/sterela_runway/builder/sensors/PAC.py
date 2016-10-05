from morse.builder.sensors import VideoCamera
from morse.builder.blenderobjects import Cube

class PAC(VideoCamera):

    def __init__(self, name=None):
        VideoCamera.__init__(self, name)
        mesh = Cube("PAC_mesh")
        mesh.scale = (.65, 0.1, .1)
        mesh.translate(z=-0.1)
        mesh.color(.5, .5, .5)
        mesh._bpy_object.game.physics_type = 'NO_COLLISION'
        self.append(mesh)

