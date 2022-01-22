# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'has_unapplied_scale',
    'label': 'has_unapplied_scale',
    'definition': '',
    'default': True
}


# def check_tris(blender_mesh):
#     # bad = {'faces': []}
#     face_indices = []
#     for f in blender_mesh.faces:
#         if 3 == len(f.verts):
#             # bad['faces'].append(f.index)
#             face_indices.append(f.index)
#     # return bad
#     return face_indices


def has_unapplied_scale(scale):
    return 3 != len([c for c in scale if c == 1.0])


def check_scale(obj):
    assert False
    assert not has_unapplied_scale(obj.scale)


plugin = create_validator(check_scale, data)
