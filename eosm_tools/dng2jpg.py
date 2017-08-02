"""
Convert a dng image series into JPG images using Raw Therapee

Usage: eosm_raw2dng -i=DNG_PATH -o=OUTPUT_PATH [-c=CONFIG_PATH]

Options:
    -i --dng_path=DNG_PATH          Path to the Canon raw video file.
    -o --out_path=OUT_PATH          Path to the output dng file directory.
    -c --config_path=CONFIG_PATH    Raw Therapee pp3 config file path.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)

        raw2dng_return_value = tools.dng2jpg(
            dng_path=arguments['--dng_path'],
            out_path=arguments['--out_path'],
            config_path=arguments['--config_path'])

        sys.exit(raw2dng_return_value)

    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()