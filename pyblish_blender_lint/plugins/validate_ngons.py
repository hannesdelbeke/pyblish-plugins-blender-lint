# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'ngons',
    'label': 'Ngons',
    'definition': 'A face with >4 edges. Is generally bad in exactly the same ways as Tris',
    'default': True
}


def check_ngons(self):
    face_indices = []
    for f in self.b.faces:
        if 4 < len(f.verts):
            face_indices.append(f.index)
    return face_indices


plugin = create_validator(check_ngons, data)
plugin.families.append('faces')
