from setuptools import setup

setup(
    name='VideoUploader',
    version='0.1.0',
    py_modules=['videoupload'],
    install_requires=[
        'Click',
        'PyVimeo',
    ],
    entry_points={
        'console_scripts': [
            'videoupload = videoupload:main',
        ],
    },
)