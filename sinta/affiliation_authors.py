from bs4 import BeautifulSoup
from requests import get
from pprint import pprint
from util.config import get_config
from util.utils import format_output, cast, listify, run_thread, compact_list, singlify


def affiliation_authors(affiliation_id):
    affiliation_id = singlify(affiliation_id)
    domain = get_config()['domain']
    url = f'{domain}/affiliations/authors/{affiliation_id}'
    html = BeautifulSoup(get(url).content, 'html.parser')
    n_pages = html.select('.pagination-text')[0].text.split(' ')[3]

    result = parse(html)


def parse(html):
    rows = html.select('.au-item')
    result = []

    for row in rows:
        profile_picture = row.select('img')[0]['src']
        profile = row.select('.profile-name > a')[0]
        profile_url = profile['href']
        profile_name = profile.text
        profile_id = row.select('.profile-id')[0].text.split(':')[1].strip()

        department = row.select('.profile-dept > a')[0]
        department_url = department['href']
        department_name = department.text.strip()

        h_index_row = row.select('.profile-hindex > .profile-id')
        h_index_numbers = [cast(h_index_row[i].text.split(':')[1].strip()) for i in (0, 1)]
        h_index = dict(zip(('scopus', 'scholar'), h_index_numbers))

        result.append({
            'profile_picture': profile_picture,
            'id': profile_id,
            'url': profile_url,
            'name': profile_name,
            'department': {
                'url': department_url,
                'name': department_name
            },
            'h_index': h_index
        })

        pprint(result)

        break


if __name__ == '__main__':
    affiliation_authors(404)
