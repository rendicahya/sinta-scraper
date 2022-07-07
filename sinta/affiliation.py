from bs4 import BeautifulSoup
from requests import get

from util.config import get_config
from util.utils import format_output, cast, listify, run_thread, singlify


def affiliation(affiliation_ids, output_format='dictionary'):
    result = run_thread(worker, listify(affiliation_ids))
    result = singlify(result)

    return format_output(result, output_format)


def worker(affiliation_id, worker_result, *args, **kwargs):
    domain = get_config()['domain']
    url = f'{domain}/affiliations/profile/{affiliation_id}'
    html = get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    # profile section
    name = soup.select('.univ-name > h3')[0].text.strip()
    abbrv_name = soup.select('.affil-abbrev')[0].text.strip()
    location = soup.select('.affil-loc')[0].text.strip()
    code = soup.select('.affil-code')[0].text.split(':')[-1].strip()

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
        'code': code,
        'url': url,
        'name': name,
        'abbreviation': abbrv_name,
        'location': location,
        'stats': stat,
        'sinta_score': scores
    }

    worker_result.append(result_data)
