import pyblish.api
import bpy
import bmesh

FAMILIES = ['mesh']


def is_edit_mode():
    return 'EDIT_MESH' == bpy.context.mode


def ensure_edit_mode():
    if not is_edit_mode():
        bpy.ops.object.editmode_toggle()


class ActionEditMode(pyblish.api.Action):
    label = "Set edit mode"
    on = "failedOrWarning"

    # icon = "hand-o-up"  # Icon from Awesome Icon

    def process(self, context, plugin):
        ensure_edit_mode()
        # import maya.cmds as cmds
        # errors = context.data[plugin.label]  # list of strings, ex. ['pCube2.f[0]',...]
        # print(errors)
        # cmds.select(errors)


class CollectSelectedMesh(pyblish.api.Collector):
    """collect selected blender mesh"""

    # pyblish plugin attributes
    # families = ['*']
    hosts = ['blender']
    label = 'collect selected mesh'
    optional = True
    actions = [ActionEditMode]

    def process(self, context):
        obj = bpy.context.active_object

        # ensure_edit_mode()  # a collector that toggles edit mode, dangerous. collector shouldnt change scene
        assert is_edit_mode, "not in edit mode, can't collect"

        blender_mesh = bmesh.from_edit_mesh(obj.data)
        instance = context.create_instance(obj.data.name, icon="cubes",
                                           families=FAMILIES)  # parent=instance_meshes.parent)
        instance.append(blender_mesh)
