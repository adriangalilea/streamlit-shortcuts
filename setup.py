from setuptools import setup, find_packages
import os


def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    try:
        with open(version_file, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("VERSION file not found. Please create or update it.")


setup(
    name="streamlit-shortcuts",
    version=get_version(),
    author="Adrian Galilea Delgado",
    author_email="adriangalilea@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/adriangalilea/streamlit-shortcuts",
    license="MIT",
    extras_require={
        "test": ["pytest", "black", "flake8"],
        "dev": ["pre-commit", "black", "flake8"],
    },
    extras_require_test=["pytest", "black", "flake8"],
    description="Streamlit keyboard shortcuts for your buttons.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "streamlit>=1.45.0",
    ],
    entry_points={
        "console_scripts": [
            "run-checks=streamlit_shortcuts.scripts:run_checks",
        ],
    },
)
