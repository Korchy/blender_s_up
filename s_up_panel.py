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
        layout.operator('s_up.select_level_up', text='Select Level Up', icon='FILE_PARENT')
        layout.operator('s_up.select_level_up_parent', text='Select Level Up by Parenting', icon='EMPTY_SINGLE_ARROW')

    def draw_button(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator('s_up.select_level_up', text='', icon='FILE_PARENT')
        row.operator('s_up.select_level_up_parent', text='', icon='EMPTY_SINGLE_ARROW')


def register():
    register_class(SUP_PT_main_panel)
    bpy.types.OUTLINER_HT_header.prepend(SUP_PT_main_panel.draw_button)


def unregister():
    bpy.types.OUTLINER_HT_header.remove(SUP_PT_main_panel.draw_button)
    unregister_class(SUP_PT_main_panel)
