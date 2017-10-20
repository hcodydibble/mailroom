"""Setup module for mailroom package."""

from setuptools import setup

setup(
    name='mailroom',
    description='A package for automating charity donor thank you emails.',
    package_dir={'': 'src'},
    author=['Cody Dibble', 'Gabriel Meringolo'],
    author_email=['hcodydibble@gmail.com', 'gabriel.meringolo@gmail.com'],
    py_modules=['mailroom'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
            'mailroom=mailroom:main'
        ]
    }
)
