"""
Convert a Canon raw video to a dng image collection

Usage: eosm_raw2dng -i=RAW_PATH -o=OUT_DIR

Options:
    -i --raw_path=RAW_PATH          Path to the Canon raw video file.
    -o --out_dir=OUT_DIR            Output directory with dng images.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)
        rc = tools.raw2dng(
            raw_path=arguments['--raw_path'],
            out_dir=arguments['--out_dir'],
        )
        sys.exit(rc)
    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()