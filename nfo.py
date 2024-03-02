import os
from metadata import MetaData
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


def make_nfo_file(filename, metadata):
    movie = ET.Element('movie')

    plot = ET.SubElement(movie, 'plot')
    plot.text = metadata.describe

    outline = ET.SubElement(movie, 'outline')

    lockdata = ET.SubElement(movie, 'lockdata')
    lockdata.text = 'true'

    lockedfields = ET.SubElement(movie, 'lockedfields')
    lockedfields.text = 'Name|OriginalTitle|SortName|Studios|Tags'

    title = ET.SubElement(movie, 'title')
    title.text = metadata.sub_title

    originaltitle = ET.SubElement(movie, 'originaltitle')
    originaltitle.text = metadata.title

    year = ET.SubElement(movie, 'year')
    year.text = metadata.year[:4]

    sorttitle = ET.SubElement(movie, 'sorttitle')
    sorttitle.text = metadata.title

    premiered = ET.SubElement(movie, 'premiered')
    premiered.text = metadata.public_time

    releasedate = ET.SubElement(movie, 'releasedate')
    releasedate.text = metadata.public_time

    studio = ET.SubElement(movie, 'studio')
    studio.text = metadata.director

    for t in metadata.tag_list:
        tag = ET.SubElement(movie, 'tag')
        tag.text = t

    set = ET.SubElement(movie, 'set')
    collection_name = ET.SubElement(set, 'name')
    collection_name.text = metadata.artist

    dom = minidom.parseString(ET.tostring(movie))
    with open(filename, 'wb') as f:
        f.write(dom.toprettyxml(encoding='utf-8'))


