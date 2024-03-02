import argparse
from metadata import MetaData
from vsmeta import make_vsmeta_file
from nfo import make_nfo_file

metadata = MetaData()
f_vsmeta_name = ''
f_nfo_name = ''

if __name__ == '__main__':
    paser = argparse.ArgumentParser()
    paser.add_argument('--vsmeta', help='designate vsmeta file name to create a vsmeta file')
    paser.add_argument('--nfo', help='designate nfo file name to create a nfo file')
    paser.add_argument('--title', help='movie name')
    paser.add_argument('--subtitle', help='movie subtitle')
    paser.add_argument('--year', help='movie public year, format: yyyy')
    paser.add_argument('--public', help='movie public date, formate: yyyy-mm-dd')
    paser.add_argument('--tags', help='movie tags, split by ",", tag1,tag2,tag3...')
    paser.add_argument('--artist', help='movie artist')
    paser.add_argument('--director', help='movie director')
    paser.add_argument('--describe', help='movie describe')
    paser.add_argument('--bgimage', help='movie background image path, only useful for vsmeta file')

    args = paser.parse_args()

    if args.vsmeta:
        f_vsmeta_name = args.vsmeta
    if args.nfo:
        f_nfo_name = args.nfo
    if args.title:
        metadata.title = args.title
    if args.subtitle:
        metadata.sub_title = args.subtitle
    if args.year:
        metadata.year = args.year
    if args.public:
        metadata.public_time = args.public
    if args.tags:
        metadata.tag_list = args.tags.split(',')
    if args.artist:
        metadata.artist = args.artist
    if args.director:
        metadata.director = args.director
    if args.describe:
        metadata.describe = args.describe
    if args.bgimage:
        metadata.back_ground_path = args.bgimage

    if f_vsmeta_name or f_nfo_name:
        print('metadata:')
        print('\tf_vsmeta_name: %s' % f_vsmeta_name)
        print('\tf_nfo_name: %s' % f_nfo_name)
        print('\ttitle: %s' % metadata.title)
        print('\tsubtitle: %s' % metadata.sub_title)
        print('\tyear: %s' % metadata.year)
        print('\tpublic_time: %s' % metadata.public_time)
        print('\ttag_list: %s' % metadata.tag_list)
        print('\tartist: %s' % metadata.artist)
        print('\tdirector: %s' % metadata.director)
        print('\tdescribe: %s' % metadata.describe)
        print('\tbgimage: %s' % metadata.back_ground_path)
        print('')

        if f_vsmeta_name:
            make_vsmeta_file(f_vsmeta_name, metadata)
            print('create %s' % f_vsmeta_name)

        if f_nfo_name:
            make_nfo_file(f_nfo_name, metadata)
            print('create %s' % f_nfo_name)
