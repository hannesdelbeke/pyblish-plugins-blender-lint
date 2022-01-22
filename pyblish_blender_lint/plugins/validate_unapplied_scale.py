# data and function from https://github.com/ryanjosephking/meshlint by ryanjosephking 2012
# ported to pyblish plugin by hannesdelbeke 2022

from pyblish_blender_lint.plugins._plugin_factory import create_validator

data = {
    'symbol': 'has_unapplied_scale',
    'label': 'has_unapplied_scale',
    'definition': '',
    'default': True
}


def has_unapplied_scale(scale):
    return 3 != len([c for c in scale if c == 1.0])


def check_scale(obj):
    assert not has_unapplied_scale(obj.scale), 'Object has unapplied scale'


plugin = create_validator(check_scale, data)
