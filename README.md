![](https://sinta.kemdikbud.go.id/assets/img/sinta_logo.png)

# Sinta Scraper

Retrieves information from [Sinta (Science and Technology Index)](https://sinta.kemdikbud.go.id) via scraping.

## Installation

`pip install sinta-scraper`

Dependencies (installed automatically using the above command): `beautifulsoup4`, `requests`, `dicttoxml`, `dict2xml`,
and `python-string-utils`.

## Importing

`import sinta`

## Available Functions

- [`author()`](#author)
- [`affiliation()`](#affiliation)

## Function Details

- ### `author()`

Retrieves an author's information by Sinta ID. For example:

```python
author_id = 6082456
author = sinta.author(author_id)

print(author)
```

The output format is the Python dictionary. The structure is given in the following sample output.

```python
{'affiliation': {'id': 404,
                 'name': 'Universitas Brawijaya',
                 'url': 'https://sinta.kemdikbud.go.id/affiliations/profile/404'},
 'articles': {'scholar': 103, 'scopus': 14, 'wos': 0},
 'citations': {'scholar': 266, 'scopus': 52, 'wos': 0},
 'cited_docs': {'scholar': 0, 'scopus': 9, 'wos': 0},
 'department': 'S1 - Teknik Informatika',
 'g-index': {'scholar': 1, 'scopus': 1, 'wos': ''},
 'h-index': {'scholar': 9, 'scopus': 4, 'wos': ''},
 'i10-index': {'scholar': 9, 'scopus': 1, 'wos': ''},
 'id': 6082456,
 'name': 'RANDY CAHYA WIHANDIKA',
 'score': {'3_years': 122,
           'affiliation': 0,
           'affiliation_3_years': 0,
           'overall': 451},
 'subjects': ['Image Processing', 'Computer Vision'],
 'url': 'https://sinta.kemdikbud.go.id/authors/profile/6082456'}
```

Multiple authors can also be retrieved at once:

```python
author_ids = 5975467, 6019743
authors = sinta.author(author_ids)
```

- ### `affiliation()`

Retrieves information about an affiliation. For example:

```python
affiliation_id = 404
affiliation_info = sinta.affiliation(affiliation_id)
```

Output:

```python
{'abbreviation': 'UB',
 'articles': {'garuda': 8783, 'scholar': 100142, 'scopus': 9181, 'wos': 1260},
 'authors': 2330,
 'citation_per_researcher': {'garuda': 0.46,
                             'scholar': 462.17,
                             'scopus': 49.15,
                             'wos': 7.96},
 'citations': {'garuda': 428, 'scholar': 431668, 'scopus': 45910, 'wos': 7432},
 'cited_documents': {'garuda': 265,
                     'scholar': 44142,
                     'scopus': 5622,
                     'wos': 778},
 'code': '001019',
 'departments': 177,
 'id': 404,
 'journals': 67,
 'last_update': '2022-06-15 09:00:53',
 'location': 'KOTA MALANG - JAWA TIMUR, ID',
 'name': 'Universitas Brawijaya',
 'sinta_score': {'3_years': 220241,
                 'overall': 568684,
                 'productivity': 277,
                 'productivity_3_years': 107},
 'url': 'https://sinta.kemdikbud.go.id/affiliations/profile/404'}
```

## Other Output Formats

Other formats can be used by specifying the `output_format` argument. For example:

```python
author = sinta.author(id, output_format='json')
```

Avalable output formats:

- `'dict'` (default)
- `'dict-flat'`
- `'json'`
- `'json-pretty'`
- `'xml'`
- `'xml-flat'`

You can also pretty-print a dictionary using `pprint`:

```python
from pprint import pprint

pprint(result_dict)
```
