from bs4 import BeautifulSoup
from requests import get

import sinta
from util.config import get_config
from util.utils import format_output, listify, run_thread, singlify, cast


def department(department_ids, affiliation_id, output_format='dictionary'):
    affiliation_code = sinta.affiliation(affiliation_id)['code']
    result = run_thread(worker, listify(department_ids), affiliation_id=affiliation_id,
                        affiliation_code=affiliation_code)
    result = singlify(result)

    return format_output(result, output_format)


def worker(department_id, worker_result, *args, **kwargs):
    affiliation_id = kwargs['affiliation_id']
    affiliation_code = kwargs['affiliation_code']
    domain = get_config()['domain']
    url = f'{domain}/departments/profile/{affiliation_id}/{affiliation_code}/{department_id}'
    html = get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    name = soup.select('.univ-name > h3')[0].text.strip()
    location = soup.select('.affil-loc')[0].text.strip()
    affiliation_soup = soup.select('.meta-profile > a')[0]
    affiliation = {
        'id': cast(affiliation_soup['href'].split('/')[-1]),
        'name': affiliation_soup.text.strip(),
        'url': affiliation_soup['href']
    }

    result_data = {
        'id': department_id,
        'name': name,
        'location': location,
        'url': url,
        'affiliation': affiliation
    }

    worker_result.append(result_data)
