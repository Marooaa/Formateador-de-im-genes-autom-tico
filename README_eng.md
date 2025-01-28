# Tutorial to Set Up and Run a Python Script for Image Processing

This tutorial details how to set up the environment to remove image backgrounds and add a white background using Python.

## Prerequisites

1. **Python 3.11**: Download and install Python 3.11 from the [official website](https://www.python.org/). Make sure to check the option "Add Python to PATH" during the installation.
2. **Visual Studio Build Tools**: Install Visual Studio Build Tools to avoid errors related to compiling certain libraries:
   - Go to the download page for [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
   - Download and install the tool.
   - During installation, select the **"Desktop development with C++"** option.

## Environment Setup

1. **Create and Activate a Virtual Environment**: Open a terminal and run the following commands:

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

2. **Update `pip`**: Ensure you have the latest version of `pip`:

```bash
pip install --upgrade pip
```

3. **Install Required Dependencies**: Run the following command to install the necessary libraries:

```bash
pip install pillow numpy rembg
```

## Folder Structure

Organize your files as follows:

```
project-folder/
│
├── input/              # Folder for original images
├── output/             # Folder for processed images
├── script.py           # The script to process images
└── venv/               # Virtual environment
```

Create the `input` and `output` folders manually inside the project directory.

## Using the Script

1. Place the original images in the `input` folder.
2. Run the script from the terminal:

```bash
python script.py
```

3. The processed images will be saved in the `output` folder with a white background.

## Troubleshooting

1. **Compilation Error**: If you encounter errors like "Microsoft Visual C++ 14.0 or greater is required," make sure you have installed Visual Studio Build Tools with the **"Desktop development with C++"** option.
2. **Python Version**: Ensure you are using **Python 3.11**. You can check your version with:

```bash
python --version
```

3. **Additional Libraries**: If any library is missing, install it manually using `pip install library_name`.

And that’s it! Your environment is now set up and ready to process images with Python.
