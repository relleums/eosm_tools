from distutils.core import setup

setup(
    name='eosm_tools',
    version='0.0.0',
    description='Tools for the raw video workflow with a Canon EOS M',
    url='https://github.com/relleums/eosm_tools.git',
    author='Sebastian Achim Mueller',
    author_email='sebmuell@phys.ethz.ch',
    license='MIT',
    packages=[
        'eosm_tools',
    ],
    package_data={'eosm_tools': ['resources/*']},
    install_requires=[
        'docopt',
    ],
    entry_points={'console_scripts': [
        'corsika = eosm_tools.main:main',
    ]},
    zip_safe=False,
)
