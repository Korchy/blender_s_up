# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

from . import s_up_panel
from . import s_up_ops
from . import s_up_keymap


bl_info = {
    'name': 'Select-UP',
    'category': 'Object',
    'author': 'Nikita Akimov',
    'version': (1, 2, 0),
    'blender': (2, 80, 0),
    'location': 'N-Panel, Outliner window',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-select-up/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-select-up/',
    'description': 'Select objects up by collections levels'
}


def register():
    s_up_ops.register()
    s_up_panel.register()
    s_up_keymap.register()


def unregister():
    s_up_keymap.unregister()
    s_up_panel.unregister()
    s_up_ops.unregister()


if __name__ == "__main__":
    register()
