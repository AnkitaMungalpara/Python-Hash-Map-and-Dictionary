# Inventory System - Advanced Python Hash Maps and Dictionaries

This Python module provides a set of functions to manage an inventory system. It allows for creating, updating, and querying inventory data using dictionary-based data structures.

## Functions

### `create_inventory()`
Creates and returns an initial inventory structure.

### `update_inventory(inventory, category, item_name, update_info)`
Updates item information in the inventory.

### `merge_inventories(inv1, inv2)`
Merges two inventory systems without losing any data.

### `get_items_in_category(inventory, category)`
Retrieves all items in a specified category.

### `find_most_expensive_item(inventory)`
Finds and returns the most expensive item in the inventory.

### `check_item_in_stock(inventory, item_name)`
Checks if an item is in stock and returns its details if available.

### `view_categories(inventory)`
Views available categories in the inventory.

### `view_all_items(inventory)`
Views all items in the inventory.

### `view_category_item_pairs(inventory)`
Views category-item pairs in the inventory.

### `copy_inventory(inventory, deep=True)`
Copies the entire inventory structure. Uses deep copy if deep=True, else uses shallow copy.

## Usage

To use this module, import it into your Python script:

### 1. Import the Inventory System Module

```python
import inventory_system as inv_sys
```

### 2. Create a New Inventory

To create a new inventory, use the `create_inventory()` function:

```python
inventory = inv_sys.create_inventory()
```

### 3. Update an Item in the Inventory

You can update an item in the inventory by specifying the category, item name, and details (e.g., quantity):

```python
inv_sys.update_inventory(inventory, 'Electronics', 'Laptop', {'quantity': 10})
```

### 4. Find the Most Expensive Item

To find and print the most expensive item in the inventory, use the `find_most_expensive_item()` function:

```python
most_expensive = inv_sys.find_most_expensive_item(inventory)
print(f"The most expensive item is: {most_expensive['name']}")
```

## Note

This module uses dictionary operations extensively. Make sure you're familiar with Python dictionaries and their methods for optimal usage.
