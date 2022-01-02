import unittest
from dlsite import Scraper, Locale


class TestScraper(unittest.TestCase):
    def test_scrape_metadata(self):
        scrape = Scraper(rjcode="RJ169027", locale=Locale.zh_cn)
        metadata = scrape.scrape_metadata()

        self.assertEqual(metadata['rjcode'], 'RJ169027')
        self.assertEqual(metadata['work_name'], '意地悪なロリ娘に完全支配される音声 地獄級射精禁止オナニーサポート3 ペニス虐めレベルMAX!!!')
        self.assertEqual(metadata['maker_id'], 'RG18195')
        self.assertEqual(metadata['maker_name'], 'B-bishop')
        self.assertEqual(metadata['release_date'], '2016-01-29')
        self.assertEqual(metadata['series_id'], 'SRI0000011759')
        self.assertEqual(metadata['series_name'], '地獄級オナニーサポート')
        self.assertEqual(metadata['age_category'], 'ADL')

        tags = metadata['tags']
        self.assertEqual(len(tags), 6)
        self.assertEqual('萝莉' in tags, True)
        self.assertEqual('足交' in tags, True)
        self.assertEqual('萝莉' in tags, True)
        self.assertEqual('自慰' in tags, True)
        self.assertEqual('言语侵犯' in tags, True)
        self.assertEqual('焦躁' in tags, True)
        self.assertEqual('无表情' in tags, True)

        cvs = metadata['cvs']
        self.assertEqual(len(cvs), 1)
        self.assertEqual('餅よもぎ' in cvs, True)


if __name__ == '__main__':
    unittest.main()
