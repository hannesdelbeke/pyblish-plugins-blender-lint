# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'tris',
    'label': 'Tris',
    'definition': 'A face with 3 edges. '
                  'Often bad for modeling because it stops edge loops and does not deform well around bent areas. '
                  'A mesh might look good until you animate, so beware!',
    'default': True
}


def check_tris(blender_mesh):
    face_indices = []
    for f in blender_mesh.faces:
        if 3 == len(f.verts):
            face_indices.append(f.index)
    return face_indices


plugin = create_validator(check_tris, data, convert_instance_to_bmesh=True)
plugin.families.append('faces')
