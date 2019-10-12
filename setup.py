import setuptools

setuptools.setup(
    name="nycdb_defacto",
    version="0.1.0",
    url="https://github.com/austensen/nycdb_defacto",

    author="Maxwell Austensen",
    author_email="maxwell.austensen@nyu.edu",

    license='AGPL-3.0-or-later',

    description="plugin for nycdb",

    packages=['nycdb_defacto'],

    package_data={
        'nycdb_defacto': [
            'datasets/*.yml',
            'sql/*.sql',
            'sql/**/*.sql'
        ]
    },

    include_package_data=True,

    python_requires='>=3',

    install_requires=[
        'nycdb==0.1.24'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
