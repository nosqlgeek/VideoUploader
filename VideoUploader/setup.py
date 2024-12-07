from setuptools import setup

setup(
    name='VideoUploader',
    version='0.1.0',
    py_modules=['videoupload'],
    install_requires=[
        'Click',
        'PyVimeo',
        'qrcode',
        'pillow',
        'obs-websocket-py',
    ],
    entry_points={
        'console_scripts': [
            'videoupload = videoupload:main',
        ],
    },
)