# Athletics Big Data

## Summary
1. [Installing Python Dependencies](#installing-python-dependencies)
    - [Using pip](#using-pip)
2. [How Python Virtual Environments Work](#how-python-virtual-environments-work)
    - [Creating a Virtual Environment](#creating-a-virtual-environment)
    - [Activating the Virtual Environment](#activating-the-virtual-environment)
    - [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
3. [Running the Project with Bash Script](#running-the-project-with-bash-script)

## Installing Python Dependencies

There are several ways to install Python dependencies, but the most common ones are using `pip` or package managers like Poetry.

### Using pip

`pip` is the default package manager for Python. To install the dependencies for your project using `pip`, you can do the following:

```bash
pip install .
```

Where `setup.py` is a file listing all the dependencies for your project, for example:

```
package1
package2>=1.0.0
```

## How Python Virtual Environments Work

A virtual environment is a tool that isolates a Python environment, allowing you to have different sets of installed packages for different projects. This helps avoid conflicts between packages and package versions.

### Creating a Virtual Environment

To create a virtual environment, you can use Python's `venv` module. Open a terminal or command prompt and navigate to the directory of your project. Then execute the following:

```bash
python -m venv venv
```

This will create a virtual environment named `venv` in your project directory.

### Activating the Virtual Environment

After creating the virtual environment, you need to activate it. This adjusts the environment so that Python and installed packages are isolated from the global system.

On Windows:

```bash
venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

You'll know you're in the virtual environment when the environment name appears at the beginning of your command prompt.

### Deactivating the Virtual Environment

To deactivate the virtual environment and return to the global system environment, simply type:

```bash
deactivate
```

This will restore the command prompt to the state before the virtual environment was activated.

# Running the Project with Bash Script

You can use a bash script run.sh to execute your project:

```bash
bash install.sh && bash view.sh
```