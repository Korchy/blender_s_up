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
            if self._collection_partially_selected(collection=collection):
                partially_selected_collections.append(collection)
        # get full-selected collections
        selected_collections = []
        for collection in bpy.data.collections:
            if self._collection_selected(collection=collection, check_nested=True):
                selected_collections.append(collection)
        # Select-UP
        if partially_selected_collections:
            # if there are partially-selected collections - fill them to all-selected
            for collection in partially_selected_collections:
                self._select_collection(collection=collection, select_nested=True)
        elif selected_collections:
            # if there are full-selected collections - select their parent collection
            collections_to_select = []
            for collection in selected_collections:
                parent_collection = self._parent_collection(collection)
                if parent_collection and parent_collection not in collections_to_select \
                        and parent_collection not in selected_collections:
                    collections_to_select.append(parent_collection)
            for collection in collections_to_select:
                self._select_collection(collection=collection, select_nested=True)
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
        items_to_select = collection.all_objects if select_nested else collection.objects
        for item in items_to_select:
            item.select_set(True)

    @staticmethod
    def _collection_selected(collection, check_nested=False):
        # True if collection selected (all items in collection are selected)
        items = collection.all_objects if check_nested else collection.objects
        return bool(collection.all_objects) and bool(items) and all([item.select_get() for item in items])

    @staticmethod
    def _collection_partially_selected(collection):
        # True if collection partially selected
        # have any items
        # and (
        # any selected item and any not selected
        # or
        # amy items on collection level and all of them selected and any not selected item in nested collections
        # )
        return bool(collection.all_objects)\
               and (
                   any([item.select_get() for item in collection.objects]) and any([not item.select_get() for item in collection.objects])
                   or
                   bool(collection.objects) and all([item.select_get() for item in collection.objects]) and any([not item.select_get() for item in collection.all_objects])
               )

    @staticmethod
    def _parent_collection(collection):
        # returns parent collection for collection
        parent = None
        for check_collection in bpy.data.collections:
            if collection in check_collection.children[:]:
                parent = check_collection
        return parent


class SUP_OT_select_level_up_parent(Operator):
    bl_idname = 's_up.select_level_up_parent'
    bl_label = 'Select Level Up by Parenting'
    bl_description = 'Select objects up 1 level by parenting'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # get partially-selected collections
        parents = [obj.parent for obj in context.selected_objects if obj.parent]
        for parent in parents:
            parent.select_set(True)
            self.select_all_children(
                objects=parents,
                nested=True
            )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False

    @classmethod
    def select_all_children(cls, objects, nested=False):
        # select all children of all objects from list
        if not isinstance(objects, (list, tuple)):
            objects = [objects]
        for obj in objects:
            if obj and hasattr(obj, 'children') and obj.children:
                for child in obj.children:
                    child.select_set(True)
                    if hasattr(child, 'children') and child.children:
                        cls.select_all_children(
                            objects=child,
                            nested=nested
                        )


def register():
    register_class(SUP_OT_select_level_up)
    register_class(SUP_OT_select_level_up_parent)


def unregister():
    unregister_class(SUP_OT_select_level_up_parent)
    unregister_class(SUP_OT_select_level_up)
