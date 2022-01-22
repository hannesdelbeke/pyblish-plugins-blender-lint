# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022
import re

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'label': 'is_bad_name',
    'definition': 'check if the name is alright',
    'symbol': '',
    'default': True
}


def is_bad_name(name):
    default_names = [
        'BezierCircle',
        'BezierCurve',
        'Circle',
        'Cone',
        'Cube',
        'CurvePath',
        'Cylinder',
        'Grid',
        'Icosphere',
        'Mball',
        'Monkey',
        'NurbsCircle',
        'NurbsCurve',
        'NurbsPath',
        'Plane',
        'Sphere',
        'Surface',
        'SurfCircle',
        'SurfCurve',
        'SurfCylinder',
        'SurfPatch',
        'SurfSphere',
        'SurfTorus',
        'Text',
        'Torus',
    ]
    pat = '(%s)\.?\d*$' % '|'.join(default_names)
    assert not re.match(pat, name), '%s is a bad name' % name


def is_bad_name_helper(blender_mesh):
    return is_bad_name(blender_mesh.name)


plugin = create_validator(is_bad_name_helper, data)
plugin.families.append('name')
