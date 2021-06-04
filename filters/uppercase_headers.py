from panflute import *
import subprocess

def convert_image(elem, doc):
    if isinstance(elem, Header) and elem.level == 2:
        elem.content = [Str(x.text.upper()) if isinstance(x, Str) else x for x in elem.content]

def main(doc=None):
    return run_filter(convert_image, doc=doc)

if __name__ == "__main__":
    main()
