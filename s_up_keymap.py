# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

import bpy
from bpy.types import Menu
from bpy.utils import register_class, unregister_class
import functools


class SUP_MT_ex_menu(Menu):
    bl_label = 'Select Grouped'
    bl_idname = 'S_UP_MT_context_ex_menu'

    def draw(self, context):
        # for context menu
        layout = self.layout
        layout.operator_enum('object.select_grouped', 'type')
        layout.operator('s_up.select_level_up')
        layout.operator('s_up.select_level_up_parent')

    def extend_menu(self, context):
        # for 'select' menu
        self.layout.operator('s_up.select_level_up', text='Select Level Up')
        self.layout.operator('s_up.select_level_up_parent', text='Select Level Up by Parenting')


class SUP_KeyMap:

    _keymaps = []

    @classmethod
    def register(cls, context):
        # context menu
        # deactivate old
        bpy.app.timers.register(functools.partial(cls._remove_old_keymap, context), first_interval=0.5)
        # add new (old + new)
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
            # hotkeys
            keymap_item = keymap.keymap_items.new('s_up.select_level_up', 'U', 'PRESS', shift=True)
            cls._keymaps.append((keymap, keymap_item))
            keymap_item = keymap.keymap_items.new('s_up.select_level_up_parent', 'U', 'PRESS', shift=True, ctrl=True)
            cls._keymaps.append((keymap, keymap_item))
            # menu
            keymap_item = keymap.keymap_items.new('wm.call_menu', 'G', 'PRESS', shift=True)
            keymap_item.properties.name = SUP_MT_ex_menu.bl_idname
            cls._keymaps.append((keymap, keymap_item))
        # 'select' menu
        bpy.types.VIEW3D_MT_select_object.append(SUP_MT_ex_menu.extend_menu)

    @classmethod
    def unregister(cls):
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()

    @classmethod
    def _remove_old_keymap(cls, context):
        if 'object.select_grouped' in context.window_manager.keyconfigs.default.keymaps['Object Mode'].keymap_items:
            context.window_manager.keyconfigs.default.keymaps['Object Mode'].keymap_items['object.select_grouped'].active = False
            return None
        else:
            return 0.5


def register():
    register_class(SUP_MT_ex_menu)
    SUP_KeyMap.register(context=bpy.context)


def unregister():
    SUP_KeyMap.unregister()
    unregister_class(SUP_MT_ex_menu)
