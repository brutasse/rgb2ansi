from setuptools import setup


with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='rgb2ansi',
    version='1.0.0',
    url='https://github.com/brutasse/rgb2ansi',
    license='BSD',
    author='Bruno Renié',
    description=('Color strings for terminal ouput (ANSI 256 colors) using '
                 'CSS-style ``rgb`` notation.'),
    long_description=long_description,
    py_modules=('rgb2ansi',),
    zip_safe=False,
    include_package_data=True,
    platform='any',
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
    ),
)
