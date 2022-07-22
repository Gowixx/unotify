from setuptools import setup, find_packages

VERSION = '1.1'
DESCRIPTION = 'Simple Python Linux/Ubuntu Notify Package'
LONG_DESCRIPTION = '''
# uNotify
> Notification library for Linux/Ubuntu

## Installing w/ PyPi
> `$ pip install unotify`

## Installing w/ Git
> `$ git clone https://github.com/Gowixx/unotify.git` <br />
> `$ cd unotify-main` <br />
> `$ python3 setup.py install`<br />
'''.strip()

# Setting up
setup(
        name="unotify",
        version=VERSION,
        author="Gowixx",
        author_email="<ItsGowixx@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'notify', 'toast', 'notification'],
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: POSIX",
        ]
)