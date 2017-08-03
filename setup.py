from distutils.core import setup

setup(
    name='eosm_tools',
    version='0.0.1',
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
        'eosm_raw2dng = eosm_tools.raw2dng:main',
        'eosm_dng2jpg = eosm_tools.dng2jpg:main',
        'eosm_jpg2mp4 = eosm_tools.jpg2mp4:main',
        'eosm_raw2mp4 = eosm_tools.raw2mp4:main',
    ]},
    zip_safe=False,
)
