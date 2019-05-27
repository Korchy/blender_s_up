# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

from . import s_up_panel
from . import s_up_ops


bl_info = {
    'name': 'S-UP',
    'category': 'Object',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 80, 0),
    'location': 'Outliner window',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-s-up',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-s-up',
    'description': 'Select objects up by collections levels'
}


def register():
    s_up_ops.register()
    s_up_panel.register()


def unregister():
    s_up_panel.unregister()
    s_up_ops.unregister()


if __name__ == "__main__":
    register()
