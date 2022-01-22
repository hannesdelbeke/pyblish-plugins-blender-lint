# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'nonmanifold',
    'label': 'Nonmanifold Elements',
    'definition': 'Simply, shapes that won\'t hold water. More precisely, nonmanifold edges are those '
                  'that do not have exactly 2 faces attached to them (either more or less). '
                  'Nonmanifold verts are more complicated -- '
                  'you can see their definition in BM_vert_is_manifold() in bmesh_queries.c',
    'default': True
}


def check_nonmanifold_elements(blender_mesh):
    bad = {}
    for elemtype in 'verts', 'edges':
        bad[elemtype] = []
        for elem in getattr(blender_mesh, elemtype):
            if not elem.is_manifold:
                bad[elemtype].append(elem.index)
    # TODO: Exempt mirror-plane verts.
    # Plus: ...anybody wanna tackle Mirrors with an Object Offset?
    return bad


def check_nonmanifold_verts(blender_mesh):
    return check_nonmanifold_elements(blender_mesh)['verts']


def check_nonmanifold_edges(blender_mesh):
    return check_nonmanifold_elements(blender_mesh)['edges']


plugin = create_validator(check_nonmanifold_verts, data, convert_instance_to_bmesh=True)
plugin.label = 'nonmanifold verts'
plugin.families.append('verts')

plugin2 = create_validator(check_nonmanifold_edges, data, convert_instance_to_bmesh=True)
plugin2.label = 'nonmanifold edges'
plugin2.families.append('edges')
