from setuptools import setup, find_packages
setup(
    name="PyHighcharts",
    version="2.0",
    package_dir={'': 'src'},
    packages=['pyhighcharts'],
    scripts=["bin/*"],

    install_requires=[],
    package_data={},

    # metadata for upload to PyPI
    author="fin.yeates",
    author_email="",
    description="A python wrapper for the highcharts charting library",
    license="PSF",
    keywords="PyHighcharts",
    url="https://github.com/fidyeates/PyHighcharts/tree/dev",
)