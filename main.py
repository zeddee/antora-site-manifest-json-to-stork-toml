import pprint
import json
import toml

# https://www.tutorialspoint.com/xml-parsing-in-python

pp = pprint.PrettyPrinter(width=41, compact=True).pformat

DATA = "_data/site-manifest.json"


class StorkConfigRaw:
    def __init__(
            self,
            base_directory: str,
            url_prefix: str,
            files: str,
            output_filename: str,
            debug: bool = False,
            ):
        self.base_directory = base_directory
        self.url_prefix = url_prefix
        self.files = files

        self.output_filename = output_filename
        self.debug = debug


class StorkFileListEntry:
    def __init__(
            self,
            path: str,
            url: str,
            title: str,
            ):
        self.path = path,
        self.url = url,
        self.title = title


if __name__ == "__main__":
    stork = StorkConfigRaw("basedir", "urlpref", "files", "outfile")

    with open(DATA, "r") as f:
        data = json.load(f)
        f.close()

    output = toml.dumps(data)

    with open("output.log", "w") as file:
        file.write(f"{output}")
        file.close()
