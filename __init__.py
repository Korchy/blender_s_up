# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

from .addon import Addon
from . import s_up_panel
from . import s_up_ops
from . import s_up_keymap


bl_info = {
    'name': 'Select-UP',
    'category': 'Object',
    'author': 'Nikita Akimov',
    'version': (1, 1, 0),
    'blender': (2, 80, 0),
    'location': 'N-Panel, Outliner window',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-select-up/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-select-up/',
    'description': 'Select objects up by collections levels'
}


def register():
    if not Addon.dev_mode():
        s_up_ops.register()
        s_up_panel.register()
        s_up_keymap.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        s_up_keymap.unregister()
        s_up_panel.unregister()
        s_up_ops.unregister()


if __name__ == "__main__":
    register()
