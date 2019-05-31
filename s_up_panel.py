# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

import bpy
from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class SUP_PT_main_panel(Panel):
    bl_idname = 'SUP_PT_main_panel'
    bl_label = 'S-UP'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'S-UP'

    def draw(self, context):
        layout = self.layout
        layout.operator('s_up.select_level_up', text='Select 1 level up', icon='FILE_PARENT')

    def draw_button(self, context):
        layout = self.layout
        layout.operator('s_up.select_level_up', text='', icon='FILE_PARENT')


def register():
    register_class(SUP_PT_main_panel)
    bpy.types.OUTLINER_HT_header.prepend(SUP_PT_main_panel.draw_button)


def unregister():
    bpy.types.OUTLINER_HT_header.remove(SUP_PT_main_panel.draw_button)
    unregister_class(SUP_PT_main_panel)
