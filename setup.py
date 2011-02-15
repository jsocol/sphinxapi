from setuptools import setup

setup(
    name='sphinxapi',
    version='0.9.9',
    description='Client for the Sphinx search engine.',
    long_description=open('README.rst').read(),
    author='Sphinx Technologies Inc',
    url='http://github.com/jsocol/sphinxapi',
    license='GPL',
    packages=('sphinxapi',),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
