from setuptools import setup, find_packages


setup(
    name='example.uidattrbehavior',
    version='0.1.0',
    description='',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGES.rst').read()),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Plone :: 4.3',
    ],
    keywords='',
    author='Asko Soukka',
    author_email='asko.soukka@iki.fi',
    url='',
    license='EUPL',
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['example'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'plone.app.dexterity',
        'venusianconfiguration',
    ],
    extras_require={'test': [
        'unittest2',
        'plone.app.testing',
        'plone.app.robotframework',
    ]},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
