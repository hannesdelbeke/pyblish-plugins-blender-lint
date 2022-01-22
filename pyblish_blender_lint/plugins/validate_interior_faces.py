# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'interior_faces',
    'label': 'Interior Faces',
    'definition': 'This confuses people. It is very specific: A face whose edges ALL have >2 faces attached. '
                  'The simplest way to see this is to Ctrl+r a Default Cube and hit \'f\'',
    'default': True
}


def check_interior_faces(blender_mesh):  # translated from editmesh_select.c
    face_indices = []
    for f in blender_mesh.faces:
        if not any(3 > len(e.link_faces) for e in f.edges):
            face_indices.append(f.index)
    return face_indices


plugin = create_validator(check_interior_faces, data)
plugin.families.append('faces')
