# coding=utf-8
# Code generated by:
# python -m pwiz -e mysql -H 192.168.0.20 -p 3306 -u root -i -P trivest_spider
# Date: September 25, 2017 09:29AM
# Database: trivest_spider
# Peewee version: 2.9.2

from peewee import *
from trivest_data.config.app import config
from playhouse.shortcuts import RetryOperationalError
import codecs

codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

__mysql_config = config['mysql']


class MyRetryDB(RetryOperationalError, MySQLDatabase):
    pass


database = MyRetryDB(__mysql_config['database'],
                     **{'host': __mysql_config['host'], 'password': __mysql_config['password'],
                        'port': int(__mysql_config['port']), 'user': __mysql_config['user'], 'charset': 'utf8'})

database.execute_sql("SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;")


# TODO...新增一个表的对象，就在此处添加一个键值对，指定数据库名称和类的对应关系
def getTableByName(tableName):
    Tables = {
        'similar_src': SimilarSrc,
        'similar_detail': SimilarDetail,
    }
    return Tables[tableName]


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class SimilarSrc(BaseModel):
    plat_name = CharField(null=True)
    plat_url = CharField(null=True)
    search_word = CharField(null=True)
    info = CharField(null=True)
    update_time = DateTimeField(null=True)
    area = CharField(null=True)
    hash_code = CharField(null=True)

    class Meta:
        db_table = 'similar_src'


class SimilarDetail(BaseModel):
    src_id = IntegerField(null=True)
    info = CharField(null=True)
    url = CharField(null=True)
    hash_code = CharField(null=True)
    update_time = DateTimeField(null=True)
    content = TextField(null=True)
    search_word = CharField(null=True)

    over_view_time = CharField(null=True)
    # 第一部分
    global_rank = CharField(null=True)
    country_rank = CharField(null=True)
    category_rank = CharField(null=True)
    # 第二部分
    trf_total_visits = CharField(null=True)
    trf_total_visits_change = CharField(null=True)
    trf_avg_visit_duration = CharField(null=True)
    trf_pages_per_visit = CharField(null=True)
    trf_bounce_rate = CharField(null=True)
    # 第三部分traffic countries
    trf_country_1 = CharField(null=True)
    trf_country_1_value = CharField(null=True)
    trf_country_1_change = CharField(null=True)

    trf_country_2 = CharField(null=True)
    trf_country_2_value = CharField(null=True)
    trf_country_2_change = CharField(null=True)

    trf_country_3 = CharField(null=True)
    trf_country_3_value = CharField(null=True)
    trf_country_3_change = CharField(null=True)

    trf_country_4 = CharField(null=True)
    trf_country_4_value = CharField(null=True)
    trf_country_4_change = CharField(null=True)

    trf_country_5 = CharField(null=True)
    trf_country_5_value = CharField(null=True)
    trf_country_5_change = CharField(null=True)
    # 第三部分 Traffic Sources
    trf_source_direct = CharField(null=True)
    trf_source_referrals = CharField(null=True)
    trf_source_search = CharField(null=True)
    trf_source_social = CharField(null=True)
    trf_source_mail = CharField(null=True)
    trf_source_display = CharField(null=True)
    # 第四部分 Referrals
    ref_of_trf_percent = CharField(null=True)

    ref_top_site_1 = CharField(null=True)
    ref_top_site_1_value = CharField(null=True)
    ref_top_site_1_change = CharField(null=True)

    ref_top_site_2 = CharField(null=True)
    ref_top_site_2_value = CharField(null=True)
    ref_top_site_2_change = CharField(null=True)

    ref_top_site_3 = CharField(null=True)
    ref_top_site_3_value = CharField(null=True)
    ref_top_site_3_change = CharField(null=True)

    ref_top_site_4 = CharField(null=True)
    ref_top_site_4_value = CharField(null=True)
    ref_top_site_4_change = CharField(null=True)

    ref_top_site_5 = CharField(null=True)
    ref_top_site_5_value = CharField(null=True)
    ref_top_site_5_change = CharField(null=True)

    ref_des_site_1 = CharField(null=True)
    ref_des_site_1_value = CharField(null=True)
    ref_des_site_1_change = CharField(null=True)

    ref_des_site_2 = CharField(null=True)
    ref_des_site_2_value = CharField(null=True)
    ref_des_site_2_change = CharField(null=True)

    ref_des_site_3 = CharField(null=True)
    ref_des_site_3_value = CharField(null=True)
    ref_des_site_3_change = CharField(null=True)

    ref_des_site_4 = CharField(null=True)
    ref_des_site_4_value = CharField(null=True)
    ref_des_site_4_change = CharField(null=True)

    ref_des_site_5 = CharField(null=True)
    ref_des_site_5_value = CharField(null=True)
    ref_des_site_5_change = CharField(null=True)
    # 第五部分 Search
    sch_of_trf_percent = CharField(null=True)

    sch_organic_percent = CharField(null=True)
    sch_organic_keyword_out_of = CharField(null=True)

    sch_paid_percent = CharField(null=True)
    sch_paid_keyword_out_of = CharField(null=True)

    sch_organic_keyword_1 = CharField(null=True)
    sch_organic_keyword_1_value = CharField(null=True)
    sch_organic_keyword_1_change = CharField(null=True)

    sch_organic_keyword_2 = CharField(null=True)
    sch_organic_keyword_2_value = CharField(null=True)
    sch_organic_keyword_2_change = CharField(null=True)

    sch_organic_keyword_3 = CharField(null=True)
    sch_organic_keyword_3_value = CharField(null=True)
    sch_organic_keyword_3_change = CharField(null=True)

    sch_organic_keyword_4 = CharField(null=True)
    sch_organic_keyword_4_value = CharField(null=True)
    sch_organic_keyword_4_change = CharField(null=True)

    sch_organic_keyword_5 = CharField(null=True)
    sch_organic_keyword_5_value = CharField(null=True)
    sch_organic_keyword_5_change = CharField(null=True)

    sch_paid_keyword_1 = CharField(null=True)
    sch_paid_keyword_1_value = CharField(null=True)
    sch_paid_keyword_1_change = CharField(null=True)

    sch_paid_keyword_2 = CharField(null=True)
    sch_paid_keyword_2_value = CharField(null=True)
    sch_paid_keyword_2_change = CharField(null=True)

    sch_paid_keyword_3 = CharField(null=True)
    sch_paid_keyword_3_value = CharField(null=True)
    sch_paid_keyword_3_change = CharField(null=True)

    sch_paid_keyword_4 = CharField(null=True)
    sch_paid_keyword_4_value = CharField(null=True)
    sch_paid_keyword_4_change = CharField(null=True)

    sch_paid_keyword_5 = CharField(null=True)
    sch_paid_keyword_5_value = CharField(null=True)
    sch_paid_keyword_5_change = CharField(null=True)
    # 第六部分 Social
    soc_of_trf_percent = CharField(null=True)

    soc_trf_1 = CharField(null=True)
    soc_trf_1_value = CharField(null=True)

    soc_trf_2 = CharField(null=True)
    soc_trf_2_value = CharField(null=True)

    soc_trf_3 = CharField(null=True)
    soc_trf_3_value = CharField(null=True)

    soc_trf_4 = CharField(null=True)
    soc_trf_4_value = CharField(null=True)

    soc_trf_5 = CharField(null=True)
    soc_trf_5_value = CharField(null=True)
    # 第七部分 Display Advertising
    ad_of_trf_percent = CharField(null=True)

    ad_top_publisher_1 = CharField(null=True)
    ad_top_publisher_2 = CharField(null=True)
    ad_top_publisher_3 = CharField(null=True)
    ad_top_publisher_4 = CharField(null=True)
    ad_top_publisher_5 = CharField(null=True)
    # 第八部分 Website Content
    web_sub_domain_1 = CharField(null=True)
    web_sub_domain_1_value = CharField(null=True)

    web_sub_domain_2 = CharField(null=True)
    web_sub_domain_2_value = CharField(null=True)

    web_sub_domain_3 = CharField(null=True)
    web_sub_domain_3_value = CharField(null=True)

    web_sub_domain_4 = CharField(null=True)
    web_sub_domain_4_value = CharField(null=True)

    web_sub_domain_5 = CharField(null=True)
    web_sub_domain_5_value = CharField(null=True)

    # 第九部分 Audience Interests
    also_visit_web_1 = CharField(null=True)
    also_visit_web_2 = CharField(null=True)
    also_visit_web_3 = CharField(null=True)
    also_visit_web_4 = CharField(null=True)
    also_visit_web_5 = CharField(null=True)

    class Meta:
        db_table = 'similar_detail'
