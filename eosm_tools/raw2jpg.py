"""
Convert a Canon raw video into a series into JPG images using Raw Therapee

Usage: eosm_raw2dng -i=RAW_PATH -o=OUTPUT_PATH [-c=CONFIG_PATH]

Options:
    -i --raw_path=RAW_PATH          Path to the Canon raw video file.
    -o --out_path=OUT_PATH          Path to the output dng file directory.
    -c --config_path=CONFIG_PATH    Raw Therapee pp3 config file path.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)

        raw2dng_return_value = tools.raw2jpg(
            raw_path=arguments['--raw_path'],
            out_path=arguments['--out_path'],
            config_path=arguments['--config_path'])

        sys.exit(raw2dng_return_value)

    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()