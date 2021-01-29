import pprint
import json
import toml

# https://www.tutorialspoint.com/xml-parsing-in-python

pp = pprint.PrettyPrinter(width=41, compact=True).pformat

DATA = "_data/site-manifest.json"


class StorkFileItem:
    def __init__(
            self,
            path: str,
            url: str,
            title: str,
            ):
        self.path = path
        self.url = url
        self.title = title

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "url": self.url,
            "title": self.title,
        }


StorkFileList = list[dict]  # type alias


class StorkConfigRaw:
    def __init__(
            self,
            base_directory: str,
            url_prefix: str,
            files: StorkFileList,
            output_filename: str,
            debug=False,  # type: bool
            ):
        self.base_directory = base_directory  # type: str
        self.url_prefix = url_prefix  # type: str
        self.files = files  # type: StorkFileList

        self.output_filename = output_filename  # type: str
        self.debug = debug  # type: bool


class StorkTemplate:
    def toml(c: StorkConfigRaw) -> str:
        assert(
            c.base_directory and
            c.url_prefix and
            c.files and
            c.output_filename and
            isinstance(c.debug, bool)
        )
        return f"""# Generated from {__name__}

[input]
base_directory = \"{c.base_directory}\"
url_prefix = \"{c.url_prefix}\"
files = {c.files}

[output]
filename = \"{c.output_filename}\"
debug = {c.debug}
"""


def parse_sitmanifest(data: dict) -> StorkConfigRaw:
    file_list = []
    for component in data.get("components"):
        for version in component.get("versions"):
            for page in version.get("pages"):
                file_list.append(
                    StorkFileItem(
                        page.get("path"),
                        page.get("url"),
                        page.get("title")
                        ).to_dict()
                )

    return StorkConfigRaw(
        base_directory="build/site",
        url_prefix=data.get("url"),
        files=file_list,
        output_filename="site-manifest.toml"
    )


if __name__ == "__main__":
    stork = StorkConfigRaw(
        "basedir",
        "urlpref",
        "files",
        "outfile",
        # True
        )

    with open(DATA, "r") as f:
        data = json.load(f)
        f.close()

    parsed_manifest = parse_sitmanifest(data)
    output_toml = StorkTemplate.toml(parsed_manifest)

    output = toml.dumps(data)

    with open("output.log", "w") as file:
        file.write(f"{output_toml}")
        file.close()
