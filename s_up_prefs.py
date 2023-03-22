# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

from bpy.types import AddonPreferences
from bpy.props import BoolProperty
from bpy.utils import register_class, unregister_class
from . import s_up_panel


class SUP_preferences(AddonPreferences):

    bl_idname = __package__

    panel_viewport: BoolProperty(
        name='Show the add-on panel in 3D Viewport',
        default=True,
        update=lambda self, context: self._panel_viewport_update(
            self=self
        )
    )
    outliner_buttons: BoolProperty(
        name='Show the add-on buttons in Outliner',
        default=True,
        update=lambda self, context: self._outliner_buttons_update(
            self=self
        )
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, property='panel_viewport')
        layout.prop(self, property='outliner_buttons')

    @staticmethod
    def _panel_viewport_update(self):
        if self.panel_viewport:
            s_up_panel.register_panel()
        else:
            s_up_panel.unregister_panel()

    @staticmethod
    def _outliner_buttons_update(self):
        if self.outliner_buttons:
            s_up_panel.register_buttons()
        else:
            s_up_panel.unregister_buttons()


def register():
    register_class(SUP_preferences)


def unregister():
    unregister_class(SUP_preferences)
