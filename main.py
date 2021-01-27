import pprint
import xmltodict

# https://www.tutorialspoint.com/xml-parsing-in-python

pp = pprint.PrettyPrinter(width=41, compact=True).pformat

DATA = "_data/sitemap.xml"
# DATA = "_data/test.xml"
SCHEMA = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


if __name__ == "__main__":
    with open(DATA, "r") as f:
        data = xmltodict.parse(f.read())

        url_list = data.get("urlset").get("url")  # type: list

        output = url_list

        with open("output.log", "w") as file:
            file.write(f"{output}")
