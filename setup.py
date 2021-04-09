from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='myvolumentations',
    version='0.0.1',
    description='A small package for 3d augmentations',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, include_package_data=True)