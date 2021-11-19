# EXPERIMENTAL linkmk schema rendering of Domestic Animal Diversity Information System (DAD-IS)

This is an experimental rendering of an induced schema from

https://www.fao.org/dad-is/

## How it was built

 1. TSVs downloaded from https://www.fao.org/dad-is/dataexport/en/
 2. tsvs2linkml was used to generate a base schema
 3. linkml-model-enrichment was used to auto-annotate schema elements with ontologies
 4. linkml was used to generate this site
    - json-schema
    - markdown docs
    - etc



