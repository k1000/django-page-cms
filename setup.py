# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pages
package_name = 'django-page-cms'

def local_open(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

import os
templates_dirs = []
for directory in os.walk('pages/templates'):
    templates_dirs.append(directory[0][6:]+'/*.*')

url_schema = 'http://pypi.python.org/packages/source/d/%s/%s-%s.tar.gz'
download_url = url_schema % (package_name, package_name, pages.__version__)

setup(
    name=package_name,
    test_suite='example.test_runner.run_tests',
    version=pages.__version__,
    description=pages.__doc__,
    author=pages.__author__,
    author_email=pages.__contact__,
    url=pages.__homepage__,
    license=pages.__license__,
    long_description=local_open('README.rst').read(),
    download_url=download_url,
    requires=(
        'BeautifulSoup',
        'Django',
        'html5lib (>=0.10)',
        'tagging (>0.2.1)', # please use the trunk version of tagging
        'django_mptt (>0.2.1)', # please use the trunk version of django mptt
        'authority', # known as django-authority
    ),
    packages=find_packages(exclude=['example', 'example.*']),
    # very important for the binary distribution to include the templates.
    package_data={'pages': templates_dirs},
    #include_package_data=True, # include package data under svn source control
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
