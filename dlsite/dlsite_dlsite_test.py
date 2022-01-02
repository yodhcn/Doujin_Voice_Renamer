import unittest
from dlsite import Dlsite


class TestDlsite(unittest.TestCase):
    def test_parse_rjcode(self):
        string_1 = '***RJ169027***'
        rjcode_1 = Dlsite.parse_rjcode(string_1)
        self.assertEqual(rjcode_1, 'RJ169027')

        string_2 = '***RJ16902789***'
        rjcode_2 = Dlsite.parse_rjcode(string_2)
        self.assertEqual(rjcode_2, None)

        string_3 = '***rj169027***'
        rjcode_3 = Dlsite.parse_rjcode(string_3)
        self.assertEqual(rjcode_3, 'RJ169027')

    def test_parse_url_params(self):
        url = 'https://www.dlsite.com/maniax/fsr' \
              '/=/keyword_work_name' \
              '/%22%E5%9C%B0%E7%8D%84%E7%B4%9A%E3%82%AA%E3%83%8A%E3%83%8B%E' \
              '3%83%BC%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%22+SRI0000011759' \
              '/order/title_d' \
              '/from/work.titles' \
              '/?locale=zh_CN'
        params = Dlsite.parse_url_params(url)
        str_keyword_work_name = params.get('keyword_work_name', '')
        str_order = params.get('order', '')
        str_from = params.get('from', '')

        self.assertEqual(len(params), 3)
        self.assertEqual(str_keyword_work_name, '"地獄級オナニーサポート"+SRI0000011759')
        self.assertEqual(str_order, 'title_d')
        self.assertEqual(str_from, 'work.titles')


if __name__ == '__main__':
    unittest.main()
