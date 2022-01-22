# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'three_poles',
    'label': '#-edge Poles',
    'definition': 'A vertex with # edges connected to it. usefull to check for N-Pole, E-pole etc',
    'default': False
}


# todo expose count to plugin settings
def check_poles(blender_mesh, count=6):
    indices = []
    for v in blender_mesh.verts:
        if count == len(v.link_edges):
            indices.append(v.index)
    return indices


plugin = create_validator(check_poles, data)
plugin.families.append('verts')
