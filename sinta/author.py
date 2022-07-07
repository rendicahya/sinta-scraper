from bs4 import BeautifulSoup
from requests import get

from util.config import get_config
from util.utils import format_output, cast, listify, run_thread, singlify


def author(author_ids, output_format='dictionary'):
    author_ids = listify(author_ids)
    result = run_thread(worker, author_ids)
    result = singlify(result)

    return format_output(result, output_format)


def worker(author_id, worker_result, **kwargs):
    domain = get_config()['domain']
    url = f'{domain}/authors/profile/{author_id}'
    html = get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    name = soup.select('h3 > a')[0].text.strip()
    profile = soup.select('.meta-profile a')
    affil_name = profile[0].text.strip()
    affil_url = profile[0]['href'].strip()
    affil_id = cast(affil_url.split('/')[-1])
    dept = profile[1].text.strip()
    subjects = [subject.text.strip() for subject in soup.select('.subject-list a')]

    scores_soup = soup.select('.stat-profile .pr-num')
    score_names = 'overall', '3_years', 'affiliation', 'affiliation_3_years'
    scores_int = [cast(scores_soup[i].text) for i in range(4)]
    scores = dict(zip(score_names, scores_int))

    stat_names = 'articles', 'citations', 'cited_docs', 'h-index', 'i10-index', 'g-index'
    indexers = 'scopus', 'scholar', 'wos'
    stat_soup = soup.select('.stat-table > tbody > tr')
    stats = {}

    for i, stat_name in enumerate(stat_names):
        s = [cast(stat_soup[i].select('td')[j].text.strip()) for j in range(1, 4)]
        stats[stat_name] = dict(zip(indexers, s))

    result_data = {
                      'id': author_id,
                      'name': name,
                      'url': url,
                      'affiliation': {
                          'id': affil_id,
                          'name': affil_name,
                          'url': affil_url
                      },
                      'department': dept,
                      'subjects': subjects,
                      'score': scores
                  } | stats

    worker_result.append(result_data)
