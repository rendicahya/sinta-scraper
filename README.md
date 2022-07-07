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

## Function Details

- ### `author()`

Retrieves an author's information by Sinta ID. For example:

```
author_id = 6082456
author = sinta.author(author_id)

print(author)
```

The output format is the Python dictionary. The structure is given in the following sample output.

```
{
    "id": 6082456,
    "name": "RANDY CAHYA WIHANDIKA",
    "url": "https://sinta3.kemdikbud.go.id/authors/profile/6082456",
    "affiliation": {
        "id": 404,
        "name": "Universitas Brawijaya",
        "url": "https://sinta3.kemdikbud.go.id/affiliations/profile/404"
    },
    "department": "S1 - Teknik Informatika",
    "subjects": [
        "Image Processing",
        "Computer Vision"
    ],
    "score": {
        "overall": 449,
        "3_years": 122,
        "affiliation": 0,
        "affiliation_3_years": 0
    },
    "articles": {
        "scopus": 14,
        "scholar": 103,
        "wos": 0
    },
    "citations": {
        "scopus": 52,
        "scholar": 266,
        "wos": 0
    },
    "cited_docs": {
        "scopus": 9,
        "scholar": 0,
        "wos": 0
    },
    "h-index": {
        "scopus": 4,
        "scholar": 9,
        "wos": ""
    },
    "i10-index": {
        "scopus": 1,
        "scholar": 9,
        "wos": ""
    },
    "g-index": {
        "scopus": 1,
        "scholar": 1,
        "wos": ""
    }
}

```

Multiple authors can also be retrieved at once:

```
author_ids = 5975467, 6019743
authors = sinta.author(author_ids)
```

## Other Output Formats

Other formats can be used by specifying the `output_format` argument:

```
author = sinta.author(id, output_format='json')
```

Avalable output formats:

- `'dictionary'` (default)
- `'json'`
- `'json-pretty'`
- `'xml'`
- `'xml-pretty'`

Please note that the output is not wrapped in a root element. For example:

```
author = sinta.author(id, output_format='xml', xml_library='dict2xml')
```

Output:

```
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
