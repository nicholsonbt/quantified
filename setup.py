from setuptools import setup, find_packages



NAME = 'Quantified'

VERSION = '0.0.1'

DESCRIPTION = 'A library for working with quantified values.'

PROJECT_URLS = {
    'Source Code': 'https://github.com/nicholsonbt/quantified',
}

LICENSE = 'GPLv3+'

INSTALL_REQUIRES = []

PACKAGES = find_packages()

# Extra non .py, .{so,pyd} files that are installed within the package dir
# hierarchy
PACKAGE_DATA = {}


def setup_package():
    setup(
        name=NAME,
        description=DESCRIPTION,
        project_urls=PROJECT_URLS,
        license=LICENSE,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        zip_safe=False,
    )


if __name__ == '__main__':
    setup_package()