from io import open
from setuptools import setup

setup(
    name='insegel',
    version='0.0.1-alpha',
    url='https://github.com/autophagy/insegel',
    license='MIT',
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    description='Theme for Sphinx',
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
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
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
        'Programming Language :: Python :: 2.7',
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