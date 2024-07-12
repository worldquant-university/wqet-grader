
try:
    from setuptools import setup
    from setuptools import find_packages
    from setuptools.command.install import install as _install
    from setuptools.command.sdist import sdist as _sdist
except ImportError:
    from distutils.core import setup
    from distutils.core import find_packages
    from distutils.command.install import install as _install
    from distutils.command.sdist import sdist as _sdist

class install(_install):
    def run(self):
        _install.run(self)

setup(
    name="wqet_grader",
    version="0.2.2",
    description='Grading for WQET',
    url='https://github.com/worldquant/wqet-grader',
    cmdclass={'install': install},
    include_package_data=True,
    install_requires=[
        'pandas>=1.3.3',
        'requests>=2.26.0',
        'category-encoders>=2.2.2',
        'scikit-learn>=1.0',
        'matplotlib>=3.7'
    ],
    packages=find_packages()
)
