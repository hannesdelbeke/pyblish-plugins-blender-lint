import pyblish.api
import bmesh

FAMILIES = ['mesh']


def create_validator(func, data, convert_instance_to_bmesh=False, **kwargs):
    class ValidationPlugin(pyblish.api.Validator):
        label = data.get('label', None)
        __doc__ = data.get('definition', 'missing documentation')
        optional = False
        hosts = ["blender"]
        families = FAMILIES
        # actions = [ActionSelect]
        _func = [func]  # we can't store func directly or it will pass self when running self.func()

        def process(self, instance, context):
            meshes = instance[:]
            for mesh in meshes:
                print("test ==============")
                try:

                    if convert_instance_to_bmesh:
                        bmesh_instance = bmesh.from_edit_mesh(mesh.data)
                        mesh = bmesh_instance

                    func = self._func[0]
                    errors = func(mesh, **kwargs)
                except Exception as ex:
                    print("start ==============")
                    print(ex)
                    print("end ==============")
                    errors = [mesh]

                context.data[self.label] = errors  # save failed results for reuse later
                assert not errors, 'check failed on:' + str(errors)
    # print("test ==============")
    # print(func)
    # print(dir(func))
    # print(func.__name__)
    ValidationPlugin.__name__ = 'validate_' + func.__name__

    return ValidationPlugin
