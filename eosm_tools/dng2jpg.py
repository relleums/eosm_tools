"""
Convert a dng image series into JPG images using Raw Therapee

Usage: eosm_raw2dng -i=DNG_PATH -o=OUT_DIR [-c=CONFIG_PATH]

Options:
    -i --dng_path=DNG_PATH          Path to the Canon raw video file.
    -o --out_dir=OUT_DIR            Directory to the dng output directory.
    -c --config_path=CONFIG_PATH    Raw Therapee pp3 config file path.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)
        rc = tools.dng2jpg(
            dng_path=arguments['--dng_path'],
            out_dir=arguments['--out_dir'],
            config_path=arguments['--config_path']
        )
        sys.exit(rc)
    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()