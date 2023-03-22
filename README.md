# Select-UP
Blender "S-UP" add-on.

Author: Nikita Akimov interplanety@interplanety.org

<a href="https://b3d.interplanety.org/en/blender-add-on-s-up">Add-on web page</a>

<img src="https://b3d.interplanety.org/wp-content/upload_content/2021/09/preview_00_1200x600-560x280.jpg" title="S - UP">

Current version
-
1.2.1.

Installation
-
User Preferences - Add-ons - Install Add-on from File - select distributive archive

Location
-
"3D View" window - N-Panel - "S-UP" tab or the "Outliner" window - button with "arrow up".

Usage
-
- Select single object from some nested collections
- Each pressing the "Select Level Up" button make the level-up selection for items in collections.

Shortcuts
-
- shift+g - Select Level Up

For Blender versions:
-
2.80, 2.81, 2.82, 2.83, 2.90, 2.91, 2.92, 2.93, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6

Version history:
-
1.3.0.
- Added option not to show panel in the 3D Viewport (functionality works only with hotkeys)
- Added default hotkeys:
  - shift+u - select level up
  - ctrl+shift+u - select level up by parenting

1.2.0.
- Added an option to "select up" by parenting

1.1.0.
- Algorithm change. If there are partially-selected collections - next press fill them to full selected. If there are only full-selected collections - next press select the level-up (parent) collection.
- Added shortcuts to the "Select" menu and to the context "Select Grouped" menu

1.0.0.
- This release
