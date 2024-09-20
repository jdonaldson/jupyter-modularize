import os

from IPython.core.magic import register_cell_magic
from IPython.display import display, Javascript

@register_cell_magic
def modularize(line, cell):
    # Execute the cell
    get_ipython().run_cell(cell)

    # Get the module name from the line argument
    module_name = line.strip()
    if not module_name:
        raise ValueError("Please provide a module name")

    # Create the module file
    file_name = f"{module_name}.py"
    with open(file_name, 'w') as f:
        f.write(cell)

    print(f"Cell exported as module: {file_name}")

    # Add the current directory to sys.path if it's not already there
    display(Javascript("""
    var code = `
    import sys
    import os
    current_dir = os.getcwd()
    if current_dir not in sys.path:
        sys.path.append(current_dir)
    `;
    IPython.notebook.kernel.execute(code);
    """))

# Load the extension
def load_ipython_extension(ipython):
    ipython.register_magic_function(modularize, 'cell')
    print("Cell modularize magic loaded. Use %%modularize module_name to export a cell as a module.")
