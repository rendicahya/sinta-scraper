from pprint import pprint

from bs4 import BeautifulSoup
from requests import get

from util.config import get_config
from util.utils import format_output, cast, run_thread, singlify


def affiliation_authors(affiliation_id, output_format='dict'):
    affiliation_id = singlify(affiliation_id)
    domain = get_config()['domain']
    url = f'{domain}/affiliations/authors/{affiliation_id}'
    html = BeautifulSoup(get(url).content, 'html.parser')
    n_pages = cast(html.select('.pagination-text')[0].text.split(' ')[3])
    result = parse(html)
    thread_result = run_thread(worker, list(range(2, n_pages + 1)), affiliation_id=affiliation_id)

    result.extend(thread_result)

    return format_output(result, output_format)


def worker(page, result, **kwargs):
    affiliation_id = kwargs['affiliation_id']
    domain = get_config()['domain']
    url = f'{domain}/affiliations/authors/{affiliation_id}?page={page}'
    html = BeautifulSoup(get(url).content, 'html.parser')
    data = parse(html)

    result.extend(data)


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

        score_names = 'sinta_3_years', 'sinta', 'affil_3_years', 'affil'
        score_numbers = [cast(row.select('.stat-num')[i].text.replace('.', '')) for i in range(4)]
        scores = dict(zip(score_names, score_numbers))

        result.append({
            'profile_picture': profile_picture,
            'id': profile_id,
            'url': profile_url,
            'name': profile_name,
            'department': {
                'url': department_url,
                'name': department_name
            },
            'h_index': h_index,
            'scores': scores
        })

    return result


if __name__ == '__main__':
    data = affiliation_authors(404)

    pprint(data)
