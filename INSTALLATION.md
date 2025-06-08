# Installation

This guide provides detailed instructions for installing the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) for users, scientists, and contributors. We strongly recommend using a virtual environment to manage the project's dependencies in isolation.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python** >= 3.11 ([Download Python](https://www.python.org/downloads/))
- **pip** >= 25 ([Upgrade pip](https://pip.pypa.io/en/stable/installation/))
- **Virtual Environment Tool** ([venv](https://docs.python.org/3/library/venv.html))

## Creating and Activating a Virtual Environment

Using a virtual environment helps avoid conflicts with other Python projects and ensures that the dependencies for the `gfw-api-python-client` are managed separately.

### On macOS and Linux

- Open your terminal and navigate to the directory where you want to create your project.

- Create a new virtual environment named `.venv`:

    ```bash
    python3 -m venv .venv
    ```

- Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

Your terminal prompt should now be prefixed with `(.venv)`, indicating that the virtual environment is active.

### On Windows

- Open Command Prompt or PowerShell and navigate to the directory where you want to create your project.

- Create a new virtual environment named `.venv`:

    ```powershell
    python -m venv .venv
    ```

- Activate the virtual environment:

    ```powershell
    .venv\Scripts\activate
    ```

Your terminal prompt should now be prefixed with `(.venv)`, indicating that the virtual environment is active.

## Installation Methods

Choose one of the following methods to install the `gfw-api-python-client`.

### Installing the Latest Release via pip (Recommended)

This method installs the stable, pre-packaged version of the `gfw-api-python-client` from the [Python Package Index (PyPI)](https://pypi.org/project/gfw-api-python-client/).

```bash
pip install gfw-api-python-client
```

`pip` will automatically download and install the `gfw-api-python-client` and its required dependencies.

### Installing from Source

This method allows you to install the `gfw-api-python-client` directly from the source code, which is useful for contributing to the project or using the latest unreleased changes.

- Clone the repository

    ```bash
    git clone https://github.com/GlobalFishingWatch/gfw-api-python-client.git
    cd gfw-api-python-client
    ```

- Install in **editable mode** with development dependencies:

    ```bash
    make install
    ```

This command performs an editable install (`-e .`) which links the installed package to your local source code. It also installs all the necessary development and documentation dependencies as defined in the [pyproject.toml](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/pyproject.toml) file.

## Updating the Package

### Updating a pip Installation

To upgrade an existing installation to the latest version available on PyPI:

```bash
python -m pip install --upgrade gfw-api-python-client
```

### Updating an Installation from Source

If you installed the `gfw-api-python-client` from source, follow these steps to update:

- Navigate to the cloned repository directory:

    ```bash
    cd gfw-api-python-client
    ```

- Fetch the latest changes from the remote repository:

    ```bash
    git pull origin main
    ```

- Re-install the package in editable mode to apply any changes and update dependencies:

    ```bash
    make install
    ```

## Verifying Your Installation

After installation, you can verify that the `gfw-api-python-client` is correctly installed by running the following Python code in your terminal or a Python interpreter:

```python
import gfwapiclient as gfw
print(gfw.__version__)
```

If the installation was successful, you should see the installed version number, for example:

```
3.0.0
```

You can also try a basic import to ensure the package is accessible:

```python
import gfwapiclient
```

If no errors are raised, the package is likely installed correctly.

## Troubleshooting

If you encounter any issues during installation, please refer to the project's [Issue Tracker](https://github.com/GlobalFishingWatch/gfw-api-python-client/issues) on GitHub to see if the problem has already been reported and if there are any known solutions. If not, feel free to open a new issue with a detailed description of the problem and the steps you took.
