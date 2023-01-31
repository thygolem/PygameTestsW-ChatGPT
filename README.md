# PARA HACER EJECUTABLES DE PYGAME

## Here's how you can use PyInstaller to create an executable:

1. Install PyInstaller: To install PyInstaller, run pip install pyinstaller in your terminal or command prompt.

2. Create the executable: To create the executable, run the following command in your terminal or command prompt, replacing "your_script.py" with the name of your Pygame script:


- pyinstaller -w -F your_script.py

3. Distribute the executable: The executable will be created in the dist folder in the same directory as your script. You can distribute this file to others, who can then run it on their computers without a Python environment.

### Note: Make sure to include all necessary files, such as sound files and fonts, in the same directory as the executable. You may also need to include any required Pygame modules in your script so that they are included in the executable.
