from enum import Enum, auto


class AutoName(Enum):
    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values):
        return name


# 枚举类 - dlsite 支持的语言
class Locale(AutoName):
    en_us = auto()
    ja_jp = auto()
    ko_kr = auto()
    zh_cn = auto()
    zh_tw = auto()
