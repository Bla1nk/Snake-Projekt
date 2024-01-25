# setup.py
from setuptools import setup, find_packages

setup(
    name='snake-game',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pygame',  # Füge hier alle Abhängigkeiten hinzu
    ],
    entry_points={
        'console_scripts': [
            'snake-game = snake.game:main',
        ],
    },
    author='Dein Name',
    author_email='deine@email.com',
    description='Ein einfaches Snake-Spiel in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dein-username/snake-game',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
