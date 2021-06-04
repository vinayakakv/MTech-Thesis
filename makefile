FILES = *md
TEMPLATE_DIR = templates
IMAGE_DIR = images
METADATA = metadata.yaml 

FLAGS = -f markdown+smart+inline_notes\
                --metadata-file=$(METADATA)\
                --pdf-engine=xelatex\
                --filter filters/convert_svg.py \
                --filter filters/uppercase_headers.py \
                --filter filters/size.py \
                --filter filters/definitions.py \
                --top-level-division=chapter\
		--filter pandoc-crossref \
		--template=$(TEMPLATE_DIR)/nitk-thesis.tex \
		--resource-path=$(IMAGE_DIR): \
                --bibliography=refs.bib \
                --citeproc \
		-t pdf \
		-s

all: pandoc

pandoc: 
	pandoc $(FILES) $(FLAGS) > build/thesis.pdf

clean:
	rm -r build/*
