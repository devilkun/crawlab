import os

from constants.spider import FILE_SUFFIX_LANG_MAPPING, LangType, SUFFIX_IGNORE, SpiderType
from db.manager import db_manager


def get_lang_by_stats(stats: dict) -> LangType:
    """
    :param stats: stats is generated by utils.file.get_file_suffix_stats
    :return:
    """
    data = stats.items()
    data = sorted(data, key=lambda item: item[1])
    data = list(filter(lambda item: item[0] not in SUFFIX_IGNORE, data))
    top_suffix = data[-1][0]
    if FILE_SUFFIX_LANG_MAPPING.get(top_suffix) is not None:
        return FILE_SUFFIX_LANG_MAPPING.get(top_suffix)
    return LangType.OTHER


def get_spider_type(path: str) -> SpiderType:
    for file_name in os.listdir(path):
        if file_name == 'scrapy.cfg':
            return SpiderType.SCRAPY


def get_spider_col_fields(col_name):
    items = db_manager.list(col_name, {}, limit=100, sort_key='_id')
    fields = set()
    for item in items:
        for k in item.keys():
            fields.add(k)
    return list(fields)
