# Inventory System Features Plan

## Overview

The inventory system is a customizable plug-and-play module designed to provide essential inventory functionalities for games built using Python and Pygame. It is intended to be flexible, visually customizable, and integrable with other game systems, offering a comprehensive solution for inventory management.

---

## Core Features

### 1. **Grid-based Inventory Layout**

- **Description**: Provides a structured grid layout to organize items, configurable by rows and columns.
- **Customization Options**:
  - Define the number of rows and columns.
  - Adjust slot size and spacing for visual alignment.
  - Specify slot types (e.g., general storage, equipment slots, consumables).

---

### 2. **Drag-and-Drop Functionality for Items**

- **Description**: Enables players to move items between inventory slots using drag-and-drop actions.
- **Key Features**:
  - Validation of slot compatibility for item placement.
  - Support for splitting and merging item stacks.
  - Visual feedback, such as highlighting valid or invalid slots during drag-and-drop.

---

### 3. **Comprehensive Item Management**

- **Core Functions**:
  - **Add Item**: Insert an item into the first available slot or a specified slot.
  - **Remove Item**: Remove an item by its unique ID or specific slot index.
  - **Swap Items**: Exchange two items between different slots seamlessly.
- **Item Metadata**:
  - Attributes include Unique ID, Name, Description, Icon Path, and Max Stack Size.

---

### 4. **Customizable User Interface (UI)**

- **Customizable Elements**:
  - Tooltip styles, including font, colors, and alignment.
  - Slot visuals, such as hover effects and empty slot backgrounds.
  - Inventory backgrounds and border designs for personalized themes.

---

### 5. **Persistent Inventory State**

- **Description**: Provides functionality to save and load the inventory state for continuity.
- **Features**:
  - **Save Structure**: Grid-based representation storing item IDs and stack counts in a file (e.g., JSON).
  - **Load Functionality**: Rebuilds the inventory from saved data, mapping items based on their IDs.

---

### 6. **Integration Hooks for Game Systems**

- **Description**: Facilitates communication between the inventory and external game systems.
- **Examples**:
  - Callbacks triggered by item interactions (e.g., using a health potion).
  - Event listeners for changes, such as adding or removing items.

---

### 7. **Keyboard and Mouse Interaction Support**

- **Keyboard**:
  - Navigate through slots using arrow keys.
  - Assign hotkeys for specific inventory actions (e.g., quickly use an item).
- **Mouse**:
  - Right-click context menus for item actions.
  - Drag-and-drop operations for rearranging items.

---

### 8. **Visual Effects and Animations**

- **Description**: Enhances the inventory UI with dynamic visuals and animations.
- **Examples**:
  - Pop-in animations when new items are added.
  - Hover glow effects for interactive slots.
  - Shake animations for invalid actions, such as trying to place an item in a restricted slot.

---

### 9. **Optional Advanced Features**

- **Equipment Slots**:
  - Special slots designated for equippable items like weapons or armor.
  - Automatic item transfer between inventory and equipment slots.
- **Filtering and Sorting**:
  - Filter items by categories such as weapons, consumables, or crafting materials.
  - Sorting options by name, rarity, or item type.
- **Hotbar Integration**:
  - Quick-access hotbar linked to specific inventory slots for streamlined gameplay.

---

## File Structure

```
inventory_system/
|-- inventory.py      # Core inventory logic
|-- item.py           # Item class and related functions
|-- ui.py             # UI handling and rendering
|-- persistence.py    # Save/load functionality
|-- README.md         # Documentation for the module
|-- example.py        # Demo script showcasing the inventory system
```

---

## Roadmap for Development

1. **Core Inventory Logic**
   - Develop the grid-based layout and implement basic item management.
2. **Drag-and-Drop System**
   - Add mechanics for moving and validating item placements.
3. **UI Customization**
   - Create flexible, customizable UI components like slots and tooltips.
4. **Persistence Features**
   - Enable save and load functionalities for inventory states.
5. **Integration Hooks**
   - Implement callbacks and event systems for external integration.
6. **Optional Features**
   - Expand the module with advanced options like filtering, equipment slots, and hotbar systems.

---

## Dependencies

- **Required**:
  - `pygame`: For rendering and input handling.
- **Optional**:
  - `jsonschema`: For validating save file formats.
  - `core`: For utilizing shared utility functions.

