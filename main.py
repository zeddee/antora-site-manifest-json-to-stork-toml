import pprint
import xml.etree.ElementTree as ET

# https://www.tutorialspoint.com/xml-parsing-in-python

pp = pprint.PrettyPrinter(width=41, compact=True).pprint

DATA = "_data/sitemap.xml"
SCHEMA = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


class Elem:
    def __init__(
            self,
            tag: dict,
            attributes: dict,
            text: str,
            ) -> dict:

        self.tag = tag
        self.attributes = attributes
        self.text = text

    def to_dict(self):
        return {
            "tag": self.tag,
            "attributes": self.attributes,
            "text": self.text,
        }


def getXMLtree(filename: str) -> ET.ElementTree:
    tree = ET.ElementTree(file=filename)
    return tree


def getXMLroot(tree: ET.ElementTree) -> ET.Element:
    root = tree.getroot()
    return root


def traverselXML(parent: ET.ElementTree):
    treeIter = parent.iter()
    elemList = list()
    for elem in treeIter:
        elemList.append(Elem(
            elem.tag,
            elem.attrib,
            elem.text,
        ).to_dict())
    return elemList


if __name__ == "__main__":
    print(SCHEMA)
    tree = getXMLtree(DATA)
    pp(traverselXML(tree))
