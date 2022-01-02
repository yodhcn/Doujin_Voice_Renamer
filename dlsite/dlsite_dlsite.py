import re
import os
import json
from urllib.parse import unquote
from typing import Final

from dlsite_translation import Translation
from dlsite_locale import Locale


# 读取翻译文件
def _load_translations():
    translations: dict[Locale, Translation] = {}
    for locale in Locale:
        file_path = os.path.join('locales', f'{locale.value}.json')
        file = open(file_path, encoding='UTF-8')
        try:
            translation: Translation = json.load(file)
            translations[locale] = translation
        finally:
            file.close()
    return translations


class Dlsite(object):
    TRANSLATIONS: Final = _load_translations()
    RJCODE_PATTERN: Final = re.compile(r'RJ(\d{6})(?!\d+)')
    RGCODE_PATTERN: Final = re.compile(r'RG(\d{5})(?!\d+)')
    SRICODE_PATTERN: Final = re.compile(r'SRI(\d{10})(?!\d+)')

    # 提取字符串中的 rjcode
    @staticmethod
    def parse_rjcode(string: str):
        string_upper = string.upper()
        match = Dlsite.RJCODE_PATTERN.search(string_upper)
        if match:
            return match.group()
        else:
            return None

    # 根据 rjcode 拼接出同人作品页面的 url
    @staticmethod
    def compile_work_page_url(rjcode: str):
        return f'https://www.dlsite.com/maniax/work/=/product_id/{rjcode}.html'

    # 解析 dlsite 链接中携带的参数 (dlsite 服务端使用 mod_rewrite 优化 SEO)
    @staticmethod
    def parse_url_params(url: str):
        url = unquote(url)
        split_url = url.split(r'/=/', 1)
        params_str = split_url[1] if len(split_url) == 2 else ''
        params_str_1 = re.sub(r'\?.*$', '', params_str, count=1)
        params_str_2 = re.sub(r'(\.html)?/?$', '', params_str_1)   # 去除 url 的 .html/ 后缀
        params_list = params_str_2.split('/')
        params = {}
        for i in range(0, len(params_list), 2):
            params[params_list[i]] = params_list[i + 1] if i + 1 < len(params_list) else ''
        return params
