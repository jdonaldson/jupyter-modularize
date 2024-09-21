from IPython.core.magic import register_cell_magic
from IPython.display import display, Javascript
from IPython.utils.importstring import import_item
from pathlib import Path
import os

@register_cell_magic
def modularize_import(line, cell):
    get_ipython().run_cell(cell)

    # Get the module name from the line argument
    module_name = line.strip()
    if not module_name:
        raise ValueError("Please provide a module name")

    # Create the module file
    Path(".modularize/").mkdir(exist_ok=True)
    file_name = f".modularize/{module_name}.py"
    with open(file_name, 'w') as f:
        f.write(cell)

    print(f"Cell exported as module: {file_name}")

    # Add the current directory to sys.path if it's not already there
    current_dir = os.getcwd()

    code = f"""
import sys
if '{current_dir}' not in sys.path:
    sys.path.append('{current_dir}/.modularize')
import {module_name}
"""
    print(f"Cell imported as module: {module_name}")
    get_ipython().run_cell(code)

@register_cell_magic
def modularize(line, cell):
    get_ipython().run_cell(cell)

    # Get the module name from the line argument
    module_name = line.strip()
    if not module_name:
        raise ValueError("Please provide a module name")

    # Create the module file
    file_name = f".modularize/{module_name}.py"
    Path(".modularize/").mkdir(exist_ok=True)
    with open(file_name, 'w') as f:
        f.write(cell)

    print(f"Cell exported as module: {file_name}")

    # Add the current directory to sys.path if it's not already there
    current_dir = os.getcwd()

    code = f"""
import sys
if '{current_dir}' not in sys.path:
    sys.path.append('{current_dir}')
"""
    get_ipython().run_cell(code)




# Load the extension
def load_ipython_extension(ipython):
    ipython.register_magic_function(modularize, 'cell')
    print("Cell modularize magic loaded. Use %%modularize module_name to export a cell as a module.")


