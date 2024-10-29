# inventory_system.py

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    inventory = {}
    inventory['Electronics']= {'Laptop':{'name': 'Laptop', 'price': 1200, 'quantity': 5}}
        
    
    inventory['Groceries']={}
    return inventory


def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    item=inventory[category]
    item_info_dict  = item[item_name]
    inventory[category][item_name] = item_info_dict | update_info
    


def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    
    merged_inventory = inv1.copy()
    for category, items in inv2.items():
        if category not in merged_inventory:
            # if not present category update
            merged_inventory[category]=items
        else:
            for it, it_info in items.items():
                # if in both dict update and update quantity with sum
                if it in merged_inventory[category]:
                    merged_item = merged_inventory[category][it]
                    merged_item['quantity']+=it_info.get('quantity',0)
                else:
                    merged_inventory[category][it]=it_info
    return merged_inventory

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory.get(category,dict())

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    all_items=[]
    for category, items in inventory.items():
        for item_name, item_info in items.items():
            all_items.append(item_info)
    return max(all_items, key=lambda x:x['price'])
    # return max(all_items, key=lambda x:x[1])[0]

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category, vals in inventory.items():
        for it_name, it_info in vals.items():
            if it_info['name'] == item_name:
                return it_info
    return None

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    all_items=[]
    for category, items in inventory.items():
        for k,v in items.items():
            all_items.append(v) 
    return all_items

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    all_items=[]
    for category, items in inventory.items():
        all_items.append((category, items)) 
    return all_items

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    if deep:
        from copy import deepcopy
        return deepcopy(inventory)
    else:
        return dict(inventory)
