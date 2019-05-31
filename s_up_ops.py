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
        # get partially-selected collections
        partially_selected_collections = []
        for collection in bpy.data.collections:
            if __class__._collection_partially_selected(collection=collection, check_nested=False):
                partially_selected_collections.append(collection)
        print('partially_selected_collections', partially_selected_collections)
        # get full-selected collections
        selected_collections = []
        for collection in bpy.data.collections:
            if __class__._collection_selected(collection=collection, check_nested=False):
                selected_collections.append(collection)
        print('selected_collections', selected_collections)
        # Select-UP
        if partially_selected_collections:
            # if there are partially-selected collections - fill them to all-selected
            for collection in partially_selected_collections:
                __class__._select_collection(collection=collection)
        elif selected_collections:
            # if there are full-selected collections - select their parent collection
            collections_to_select = []
            for collection in selected_collections:
                parent_collection = __class__._parent_collection(collection)
                if parent_collection and parent_collection not in collections_to_select:
                    collections_to_select.append(parent_collection)
            for collection in collections_to_select:
                __class__._select_collection(collection=collection)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False

    @staticmethod
    def _select_collection(collection, select_nested=False):
        # select collection (select all items in collection)
        items_to_select = collection.objects if select_nested else collection.all_objects
        for item in items_to_select:
            item.select_set(True)

    @staticmethod
    def _collection_selected(collection, check_nested=False):
        # True if collection selected (all items in collection are selected)
        items = collection.all_objects if check_nested else collection.objects
        return bool(items) and all([item.select_get() for item in items])

    @staticmethod
    def _collection_partially_selected(collection, check_nested=False):
        # True if collection selected (all items in collection are selected)
        items = collection.all_objects if check_nested else collection.objects
        return bool(items) and any([item.select_get() for item in items]) and any([not item.select_get() for item in items])

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
