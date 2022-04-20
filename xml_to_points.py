import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
file_name = sys.argv[1].replace('.xml', '.txt')
f=open(file_name, "w")
for node in root.iter('node'):
    ident = node.attrib['id']
    lat = node.attrib['lat']
    lon = node.attrib['lon']
    f.write("{} {} {}\n".format(ident,lat,lon))
f.close()