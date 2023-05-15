import setuptools


setuptools.setup(
    name='my_bazar_aiogevent',
    version='0.0.0.1',
    author='Evolt',
    author_email='dorijan.komsic@evolt.dev',
    description='Common code for MyBazaar services',
    long_description='Code that will be used in MyBazaar services is grouped in this repo so that it will not be duplicated',
    long_description_content_type="text/markdown",
    url='https://gitlab.com/evolt/bazaar/services/aiogevent',
    license='Evolt',
    packages=setuptools.find_packages(),
    python_requires=">=3"
)
