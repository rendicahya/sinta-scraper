from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from requests import get

from util.config import get_config
from util.utils import format_output, cast


def affil(author_ids, output_format='dictionary', pretty_print=None, xml_library='dicttoxml', max_workers=None):
    if type(author_ids) is not list and type(author_ids) is not tuple:
        author_ids = [author_ids]

    worker_result = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for author_id in author_ids:
            executor.submit(worker, author_id, worker_result)

    if len(worker_result) == 1:
        worker_result = worker_result[0]

    return format_output(worker_result, output_format, pretty_print, xml_library)


def worker(author_id, worker_result):
    domain = get_config()['domain']
    url = f'{domain}/affiliations/profile/{author_id}'
    html = get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    name = soup.select('h3 > a')[0].text.strip()
    profile = soup.select('.meta-profile')[0]
    abbrev = profile.select('.affil-abbrev')[0].text.strip()
    location = profile.select('.affil-loc')[0].text.strip()

    row1 = soup.select('.affil-profile-card > div')
    authors, depts, journals = [cast(row1[i].select('.stat-num')[0].text.strip().replace('.', '')) for i in range(3)]

    row2 = soup.select('.stat-profile .pr-num')
    overall, _3_year, productivity, productivity_3_year = [
        cast(row2[i].text.strip().replace('.', '')) for i in range(4)]

    print(name)
    print(abbrev)
    print(location)
    print(authors)
    print(depts)
    print(journals)
    print(overall)

    if __name__ == '__main__':
        affil(404)
