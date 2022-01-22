import bmesh
import bpy
import pyblish.api

def enable_anything_select_mode(bmesh_input):
    bmesh_input.select_mode = {'VERT', 'EDGE', 'FACE'}


# def select_indices(elemtype, indices):
#     for i in indices:
#         if 'verts' == elemtype:
#             select_vert(i)
#         elif 'edges' == elemtype:
#             select_edge(i)
#         elif 'faces' == elemtype:
#             select_face(i)
#         else:
#             print("MeshLint says: Huh?? → elemtype of %s." % elemtype)


def select_vert(bmesh_input, index):
    ob = bpy.context.edit_object
    me = ob.data
    bm = bmesh.from_edit_mesh(me)  # todo do we need bmesh_input?
    bm.verts.ensure_lookup_table()  # sav
    bmesh_input.verts[index].select = True


def select_edge(bmesh_input, index):
    ob = bpy.context.edit_object
    me = ob.data
    bm = bmesh.from_edit_mesh(me)  # todo do we need bmesh_input?
    bm.edges.ensure_lookup_table()  # sav
    edge = bmesh_input.edges[index]
    edge.select = True
    for each in edge.verts:
        select_vert(each.index)


def select_face(bmesh_input, index):
    ob = bpy.context.edit_object
    me = ob.data
    bm = bmesh.from_edit_mesh(me)  # todo do we need bmesh_input?
    bm.faces.ensure_lookup_table()  # sav
    face = bmesh_input.faces[index]
    face.select = True
    for each in face.edges:
        select_edge(each.index)

#
# def examine_active_object(self):
#     analyzer = MeshLintAnalyzer()
#     analyzer.enable_anything_select_mode()
#     self.select_none()
#     analysis = analyzer.find_problems()
#     for lint in analysis:
#         for elemtype in ELEM_TYPES:
#             indices = lint[elemtype]
#             analyzer.select_indices(elemtype, indices)
#     return analyzer.found_zero_problems()
#
# def examine_all_selected_meshes(self):
#     self.original_active = bpy.context.active_object
#     self.troubled_meshes = []
#     examinees = [self.original_active] + bpy.context.selected_objects
#     for obj in examinees:
#         if 'MESH' != obj.type:
#             continue
#         activate(obj)
#         good = self.examine_active_object()
#         ensure_not_edit_mode()
#         if not good:
#             self.troubled_meshes.append(obj)
#     priorities = [self.original_active] + self.troubled_meshes
#     for obj in priorities:
#         if obj.select_get:
#             activate(obj)
#             break
#     self.handle_troubled_meshes()
#     bpy.context.area.tag_redraw()
#
# def select_none(self):
#     bpy.ops.mesh.select_all(action='DESELECT')


class ActionFix(pyblish.api.Action):
    label = "Select"
    on = "failedOrWarning"
    icon = "hand-o-up"  # Icon from Awesome Icon

    def process(self, context, plugin):

        # because pyblish doesnt support getting instances from a plugin yet
        # we have to do this manually :(
        # if only we would get the plugin instances when using an action
        data = []
        for result in context.data["results"]:
            if result["error"] and result["plugin"] == plugin:
                instance = result["instance"]
                data.extend(instance)

        func = plugin._func[0]
        for mesh_name in data:
            # we might have mesh, or indices
            func(mesh_name, fix=True)
