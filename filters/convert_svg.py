from panflute import *
import subprocess

def convert_image(elem, doc):
    if type(elem) == Image:
        if 'svg' in elem.url:
            try:
                 #print(elem.url)
                 with open(f'{elem.url}.pdf', 'w') as f:
                 	subprocess.run(['rsvg-convert', '-f', 'pdf', elem.url], stdout=f)
                 elem.url += '.pdf'
            except IOError as e:
                 print(e)

def main(doc=None):
    return run_filter(convert_image, doc=doc)

if __name__ == "__main__":
    main()
