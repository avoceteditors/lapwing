from setuptools import setup, Extension
from os.path import join
from Cython.Build import cythonize

setup(
    name='lapwing',
    version='0.1.1',
    author='Kenneth P. J. Dyer',
    author_email='kenneth@avoceteditors.com',
    url='https://github.com/avoceteditors.com/lapwing',
    install_requires=['lxml'],
    packages=['lapwing'],
    package_data={'lapwing': ['data/*.xsl']},
    ext_modules=cythonize([Extension('*', ['lapwing/*.pyx'])]),
    scripts=[join('scripts', 'lapwing')],
    license='Revised BSD'
)
