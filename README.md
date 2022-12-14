# fuseki cleaner

## How to start fuseki

1. `./gradlew build`
2. `./gradlew startFuseki`
3. `./gradlew pattern4:owlLoad`

note: change `pattern4` to pattern of interest

## Pull (& fix syntax errors in) ttl file from fuseki

```
curl --header "Accept: text/turtle; charset=utf-8" http://localhost:3030/oml-tutorial/data > data.ttl
```

NOTE: the aforementioned command yields an invalid ttl syntax that contains entries that look like the following...

```
<http://opencaesar.io/tutorial/vocabulary/mission> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Ontology> <http://opencaesar.io/tutorial/vocabulary/mission> .
```

The expected syntax is a series of RDF triples ending with a `.`. Therefore, the final entry in each line should be removed, s.a.,

```
<http://opencaesar.io/tutorial/vocabulary/mission> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Ontology> .
```

## Usage

```
$ ./fuseki_cleaner.py
usage: fuseki_cleaner.py [-h] [-i INPUT] [-o [OUTPUT]]

Convert quadruples to triples.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of TTL to be cleaned
  -o [OUTPUT], --output [OUTPUT]
                        Filename of output TTL
```

For example,

```bash
$ ./fuseki_cleaner.py -i data.ttl -o new_data.ttl
```
