"""
Downloads *.RAW video files from the SD card into local work dir.
The local work dir is a timestamp based folder structure as: 
'/year/month/day/HourMinuteSecond/'
Files on SD card are not deleted. Time structure is based on 'mtime' stamp of
*.RAW files on SD card.

Usage: eosm_download -i=CANON_DIR -o=WORK_DIR

Options:
    -i --input_canon_dir=CANON_DIR   Directory on CANON sd card, 'DICM/100CANON'
    -o --out_dir=WORK_DIR            Output working directory.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)
        rc = tools.copy_raw_video_from_sd_card_work_dir(
            sd_card_100CANON_dir=arguments['--input_canon_dir'],
            work_dir=arguments['--out_dir'],
        )
        sys.exit(rc)
    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()