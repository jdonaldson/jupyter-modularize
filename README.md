# Jupyter Modularize

Jupyter Modularize is a Jupyter Notebook extension that allows you to execute a cell and export it as a Python module. This extension simplifies the process of creating reusable code modules directly from your Jupyter notebooks.

## Features

- Execute a cell and simultaneously export it as a Python module
- Automatically add the current directory to `sys.path` for easy importing
- Simple to use with a custom magic command

## Installation

You can install Jupyter Modularize using pip:

```bash
pip install jupyter_modularize
```

## Usage

1. Load the extension in your Jupyter notebook:

   ```python
   %load_ext jupyter_modularize
   ```

2. Use the `%%modularize` magic command followed by the desired module name:

   ```python
   %%modularize my_module

   def hello(name):
       return f"Hello, {name}!"

   def square(x):
       return x ** 2
   ```

3. The cell will be executed and saved as `my_module.py` in the current directory.

4. You can now import and use the module in your notebook or other Python scripts:

   ```python
   import my_module

   print(my_module.hello("World"))
   print(my_module.square(5))
   ```

 5. (Optional) If you'd like to automatically import the module after you declare it, use the appropriate magic:

   ```python
   %%modularize_import my_module

   def hello(name):
       return f"Hello, {name}!"

   ```

## Requirements

- Python 3.7+
- IPython 7.0.0+
- Jupyter Notebook 6.0.0+

## Development

To set up the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/jdonaldson/jupyter_modularize.git
   cd jupyter_modularize
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

4. To run tests (assuming you're using pytest):
   ```bash
   pytest
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Justin Donaldson (jdonaldson@gmail.com)

## Acknowledgments

- The Jupyter development team for creating and maintaining Jupyter Notebook
- The IPython team for their work on IPython, which this extension builds upon
