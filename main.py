import pprint
import xml.etree.ElementTree as ET

# https://www.tutorialspoint.com/xml-parsing-in-python

pp = pprint.PrettyPrinter(width=41, compact=True).pprint

# DATA = "_data/sitemap.xml"
DATA = "_data/test.xml"
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


def parseElement(elem: ET.Element) -> Elem:
    return Elem(
                elem.tag,
                elem.attrib,
                elem.text,
                )


def traverselXML(parent: ET.ElementTree):
    root = parent.getroot()
    elemList = list()
    if len(root) and isinstance(root, ET.ElementTree):
        # apparently we're not parsing children as children?
        children = root.getchildren()
        pp(children)
    else:
        for elem in root.iter():
            elemList.append(parseElement(elem).to_dict())
    return elemList


if __name__ == "__main__":
    tree = getXMLtree(DATA)
    pp(traverselXML(tree))
