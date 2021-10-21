from io import open
from setuptools import setup
from insegel import __version__

setup(
    name='insegel',
    version=__version__,
    url='https://github.com/autophagy/insegel',
    license='MIT',
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    description='Clean, minimalist Sphinx theme for deploying on ReadTheDocs',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['insegel'],
    package_data={'insegel': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/img/*.*'
    ]},
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'insegel = insegel',
        ]
    },
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
