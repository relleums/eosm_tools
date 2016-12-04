"""
Convert a Canon raw video to a dng image collection

Usage: eosm_raw2dng -i=RAW_PATH -o=OUTPUT_PATH

Options:
    -i --raw_path=RAW_PATH          Path to the Canon raw video file.
    -o --out_path=OUT_PATH    Path to the output dng file directory.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)

        raw2dng_return_value = tools.raw2dng(
            raw_path=arguments['--raw_path'],
            out_path=arguments['--out_path'],
        )

        sys.exit(raw2dng_return_value)

    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()