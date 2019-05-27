# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_s_up

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class SUP_OT_select_level_up(Operator):
    bl_idname = 's_up.select_level_up'
    bl_label = 'Select Level Up'
    bl_description = 'Select objects up 1 level by collections'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # select all collections up to 1 level
        collections_level_up = []
        for collection in bpy.data.collections:
            if __class__._collection_selected(collection=collection):
                parent_collection = __class__._parent_collection(collection)
                if parent_collection and parent_collection not in collections_level_up:
                    collections_level_up.append(parent_collection)
        print(collections_level_up)
        print('--')
        for collection in collections_level_up:
            for item in collection.all_objects:
                item.select_set(True)
        # select objects in collections with selected objects
        for item in context.selected_objects:
            for collection in item.users_collection:
                for inner_item in collection.all_objects:
                    inner_item.select_set(True)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False

    @staticmethod
    def _collection_selected(collection):
        # True if all objects in collection are selected
        return all([item.select_get() for item in collection.all_objects])

    @staticmethod
    def _parent_collection(collection):
        # returns parent collection for collection
        parent = None
        for check_collection in bpy.data.collections:
            if collection in check_collection.children[:]:
                parent = check_collection
        return parent


def register():
    register_class(SUP_OT_select_level_up)


def unregister():
    unregister_class(SUP_OT_select_level_up)
