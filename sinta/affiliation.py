from bs4 import BeautifulSoup
from requests import get

from util.config import get_config
from util.utils import format_output, cast, listify, run_thread


def affiliation(affiliation_ids, output_format='dictionary', pretty_print=None, xml_library='dicttoxml'):
    affiliation_ids = listify(affiliation_ids)
    worker_result = run_thread(worker, affiliation_ids)

    if len(worker_result) == 1:
        worker_result = worker_result[0]

    return format_output(worker_result, output_format, pretty_print, xml_library)


def worker(affiliation_id, worker_result, **kwargs):
    domain = get_config()['domain']
    url = f'{domain}/affiliations/profile/{affiliation_id}'
    html = get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    # profile section
    name = soup.select('.univ-name > h3')[0].text.strip()
    abbrv_name = soup.select('.affil-abbrev')[0].text.strip()
    location = soup.select('.affil-loc')[0].text.strip()

    # stats section
    stat_profile = soup.select('.affil-profile-card .stat-num')
    stat_names = 'authors', 'departments', 'journals'
    stat_int = [cast(stat_profile[i].text.replace('.', '')) for i in range(3)]
    stat = dict(zip(stat_names, stat_int))

    # sinta score section
    scores = soup.select('.stat-profile .pr-num')
    scores_names = 'overall', '3_years', 'productivity', 'productivity_3_years'
    scores_int = [cast(scores[i].text.replace('.', '')) for i in range(4)]
    scores = dict(zip(scores_names, scores_int))

    result_data = {
        'id': affiliation_id,
        'url': url,
        'name': name,
        'abbreviation': abbrv_name,
        'location': location,
        'stats': stat,
        'sinta_score': scores
    }

    worker_result.append(result_data)


if __name__ == '__main__':
    print(affiliation(404, output_format='json', pretty_print=True))
