# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

import bpy
from bpy.types import Panel, OUTLINER_HT_header
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


def register_panel():
    register_class(SUP_PT_main_panel)

def register_buttons():
    OUTLINER_HT_header.prepend(SUP_PT_main_panel.draw_button)

def register():
    if bpy.context.preferences.addons[__package__].preferences.panel_viewport:
        register_panel()
    if bpy.context.preferences.addons[__package__].preferences.outliner_buttons:
        register_buttons()

def unregister_panel():
    if hasattr(bpy.types, 'SUP_PT_main_panel'):
        unregister_class(SUP_PT_main_panel)

def unregister_buttons():
    if hasattr(OUTLINER_HT_header.draw, '_draw_funcs') and \
            SUP_PT_main_panel.draw_button in OUTLINER_HT_header.draw._draw_funcs:
        OUTLINER_HT_header.remove(SUP_PT_main_panel.draw_button)

def unregister():
    unregister_buttons()
    unregister_panel()
