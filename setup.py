import os
import setuptools

_APP_PATH = os.path.dirname(__file__)
_RESOURCES_PATH = os.path.join(_APP_PATH, 'omsaalert', 'resources')

with open(os.path.join(_RESOURCES_PATH, 'README.rst')) as f:
    _LONG_DESCRIPTION = f.read()

with open(os.path.join(_RESOURCES_PATH, 'requirements.txt')) as f:
    _REQUIREMENTS = [s.strip() for s in f if s.strip() != '']

with open(os.path.join(_RESOURCES_PATH, 'version.txt')) as f:
    _VERSION = f.read().strip()

setuptools.setup(
    name='omsa-alert',
    version=_VERSION,
    description="Scan OMSA's omreport tool's output for issues",
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    classifiers=[],
    keywords='omsa omreport',
    author='Dustin Oprea',
    author_email='myselfasunder@gmail.com',
    url='https://github.com/dsoprea/omsa_alert',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'omsaalert': [
            'resources/README.rst',
            'resources/requirements.txt',
        ],
    },
    install_requires=_REQUIREMENTS,
    scripts=[
        'omsaalert/resources/scripts/oa_check',
    ],
)
