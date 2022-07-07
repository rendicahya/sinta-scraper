![](https://sinta.kemdikbud.go.id/assets/img/sinta_logo.png)

# Sinta Scraper

Retrieves information from [Sinta (Science and Technology Index)](https://sinta.kemdikbud.go.id) via scraping.

## Installation

`pip install sinta-scraper`

Dependencies (installed automatically using the above command): `beautifulsoup4`, `requests`, `dicttoxml`, `dict2xml`, and `python-string-utils`.

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

Other formats can be used by specifying the `output_format` argument:

```python
author = sinta.author(id, output_format='json')
```

Avalable output formats:

- `'dictionary'` (default)
- `'json'`
- `'json-pretty'`
- `'xml'`
- `'xml-pretty'`

You can also pretty-print a dictionary using `pprint`:
```python
from pprint import pprint

pprint(result_dict)
```

Please note that the output is not wrapped in a root element. For example:

```python
author = sinta.author(id, output_format='xml', xml_library='dict2xml')
```

Output:

```xml
<affiliation>
  <id>417</id>
  <name>Institut Teknologi Sepuluh Nopember</name>
  <url>http://sinta.ristekbrin.go.id/affiliations/detail/?id=417&amp;view=overview</url>
</affiliation>
<areas>computer vision</areas>
<areas>image processing</areas>
<areas>information retrieval</areas>
<areas>medical imaging</areas>
<areas>machine learning</areas>
<books>0</books>
<department>Teknik Informatika</department>
<id>5975467</id>
<ipr>2</ipr>
<name>AGUS ZAINAL ARIFIN</name>
<rank>
  <_3_years_affiliation>30</_3_years_affiliation>
  <_3_years_national>1099</_3_years_national>
  <affiliation>32</affiliation>
  <national>723</national>
</rank>
<scholar>
  <citations>1444</citations>
  <documents>294</documents>
  <g-index>31</g-index>
  <h-index>16</h-index>
  <i10-index>36</i10-index>
</scholar>
<scopus>
  <Q1>6</Q1>
  <Q2>12</Q2>
  <Q3>13</Q3>
  <Q4>3</Q4>
  <articles>39</articles>
  <citations>469</citations>
  <conferences>30</conferences>
  <documents>69</documents>
  <g-index>1</g-index>
  <h-index>10</h-index>
  <i10-index>10</i10-index>
  <others>0</others>
  <undefined>35</undefined>
</scopus>
<score>
  <_3_years>3.13</_3_years>
  <_3_years_v2>1377.5</_3_years_v2>
  <overall>48.1</overall>
  <overall_v2>4726.0</overall_v2>
</score>
<sinta>
  <S0>1</S0>
  <S1>8</S1>
  <S2>3</S2>
  <S3>3</S3>
  <S4>7</S4>
  <S5>0</S5>
  <uncategorized>272</uncategorized>
</sinta>
<url>https://sinta.kemdikbud.go.id/authors/detail?id=5975467&amp;view=overview</url>
<wos>
  <citations>None</citations>
  <documents>1</documents>
  <g-index>None</g-index>
  <h-index>None</h-index>
  <i10-index>None</i10-index>
</wos>
```
