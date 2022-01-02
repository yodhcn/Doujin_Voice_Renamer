import requests
import re
from pyquery import PyQuery as pq

from dlsite_dlsite import Dlsite
from dlsite_locale import Locale
from dlsite_work_metadata import WorkMetadata


class Scraper(object):
    def __init__(self, rjcode: str, locale: Locale, proxies=None):
        if not Dlsite.RJCODE_PATTERN.fullmatch(rjcode):
            raise ValueError
        self.__rjcode = rjcode.upper()
        self.__locale = locale
        self.__proxies = proxies

    def __request_work_page(self):
        url = Dlsite.compile_work_page_url(self.__rjcode)
        params = {'locale': self.__locale.value}
        response = requests.get(url, params, proxies=self.__proxies)
        html = response.text
        return html

    def __parse_metadata(self, html: str):
        d = pq(html)
        metadata: WorkMetadata = {
            'rjcode': self.__rjcode,
            'work_name': '',
            'maker_id': '',
            'maker_name': '',
            'release_date': '',
            'series_name': '',
            'series_id': '',
            'age_category': '',
            'tags': [],
            'cvs': []
        }

        # parse work_name
        work_name = d('#work_name').text()
        metadata['work_name'] = work_name

        # parse maker_name
        maker_anchor_element = d('span.maker_name > a')
        maker_name = maker_anchor_element.text()
        metadata['maker_name'] = maker_name

        # parse maker_id
        maker_url = maker_anchor_element.attr('href')
        maker_id = Dlsite.parse_url_params(maker_url).get('maker_id', '')
        if Dlsite.RGCODE_PATTERN.fullmatch(maker_id):
            metadata['maker_id'] = maker_id

        translation = Dlsite.TRANSLATIONS[self.__locale]
        table_rows = d('#work_outline > tr').items()
        for table_row in table_rows:
            table_header: str = table_row.children('th').text()
            table_data = table_row.children('td')
            # parse release_date
            if table_header == translation['RELEASE_DATE']:
                release_url = table_data.children('a').attr('href')
                if release_url is not None:
                    parse_result = Dlsite.parse_url_params(release_url)
                    year = parse_result.get('year', '')
                    mon = parse_result.get('mon', '')
                    day = parse_result.get('day', '')
                    if year and mon and day:
                        release_date = f'{year}-{mon}-{day}'
                        metadata['release_date'] = release_date
            # parse series_id & series_name
            elif table_header == translation['SERIES_NAME']:
                series_anchor_element = table_data.children('a')
                series_name = series_anchor_element.text()
                series_url = series_anchor_element.attr('href')
                metadata['series_name'] = series_name
                keyword_work_name = Dlsite.parse_url_params(series_url).get('keyword_work_name', '')
                split_keyword_work_name = keyword_work_name.split('+')
                if len(split_keyword_work_name) == 2:
                    series_id = split_keyword_work_name[1]
                    if Dlsite.SRICODE_PATTERN.fullmatch(series_id):
                        metadata['series_id'] = series_id
            # parse age_category
            elif table_header == translation['AGE']:
                age_icon_element = table_data.find('span')
                age_icon_name = age_icon_element.attr('class')
                if re.fullmatch(r'icon_(GEN|R15|ADL)', age_icon_name):
                    if age_icon_name == 'icon_GEN':
                        metadata['age_category'] = 'GEN'
                    elif age_icon_name == 'icon_R15':
                        metadata['age_category'] = 'R15'
                    else:
                        metadata['age_category'] = 'ADL'
            # parse tags
            elif table_header == translation['GENRE']:
                genre_anchor_elements = table_data.children('div.main_genre').children('a').items()
                for genre_anchor_element in genre_anchor_elements:
                    genre_name = genre_anchor_element.text()
                    if genre_name:
                        metadata['tags'].append(genre_name)
            # parse cvs
            elif table_header == translation['VOICE_ACTOR']:
                cv_anchor_elements = table_data.children('a').items()
                for cv_anchor_element in cv_anchor_elements:
                    cv_name = cv_anchor_element.text()
                    if cv_name:
                        metadata['cvs'].append(cv_name)
        return metadata

    def scrape_metadata(self):
        html = self.__request_work_page()
        metadata = self.__parse_metadata(html)
        return metadata
