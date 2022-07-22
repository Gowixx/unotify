from setuptools import setup, find_packages

VERSION = '0.1' 
DESCRIPTION = 'Simple Python Linux/Ubuntu Notify Package'
LONG_DESCRIPTION = 'Simple Python Linux/Ubuntu Notify Package Created in Python'

# Setting up
setup(
        name="unotify",
        version=VERSION,
        author="Gowixx",
        author_email="<ItsGowixx@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
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