from setuptools import setup, find_packages

setup(
    name='streamlit-shortcuts',
    version='0.1.1',
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
