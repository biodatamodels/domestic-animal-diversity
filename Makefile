NAME = domestic_animal_diversity
SRC = src/schema/$(NAME).yaml

all: project excel md all-examples
project:
	gen-project -d $(NAME) $(SRC)

# remove this when gen-project fixed
excel:
	gen-excel flmd.yaml -o flmd/excel/flmd.xlsx

md:
	gen-markdown -d docs flmd.yaml

examples/%.ttl: examples/%.tsv $(SRC)
	linkml-convert -s $(SRC) -C Container $< -o $@
examples/%.json: examples/%.tsv $(SRC)
	linkml-convert -s $(SRC) -C Container $< -o $@

all-examples: examples/flmd-example.ttl examples/flmd-example.json

test: all-examples

testdocs:
	mkdocs serve

gh-deploy:
	mkdocs gh-deploy
