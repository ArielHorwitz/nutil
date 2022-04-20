import setuptools

with open(file='README.md', mode='r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='nutil',
    version='0.0.7',
    description='Common utilities for personal projects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.9',
    install_requires=[
        'numpy==1.22.3',
    ],
    packages=setuptools.find_packages(
        include=['nutil']
    ),
)
