from setuptools import setup, find_packages
import os

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    if os.path.exists(version_file):
        with open(version_file) as f:
            return f.read().strip()
    return '0.0.0'

setup(
    name='streamlit-shortcuts',
    version=get_version(),
    author='Adrian Galilea Delgado',
    author_email='adriangalilea@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/adriangalilea/streamlit-shortcuts',
    license='MIT',
    description='Streamlit keyboard shortcuts for your buttons.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'streamlit',
    ],
)
