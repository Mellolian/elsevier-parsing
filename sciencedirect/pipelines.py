# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class SciencedirectPipeline(object):

    def open_spider(self, spider):
        hostname = '127.0.0.1'
        username = 'mellolian'
        password = 'Fljufk93'  # your password
        database = 'RSC'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        print('connected')

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


    def process_item(self, item, spider):
        # print(item['doi'])
        self.cur.execute('SELECT 1 FROM articles WHERE doi = %s;', (item['doi'],))
        # print(item['doi'])
        doi_exists = self.cur.fetchone() is not None
        if not doi_exists:
            self.cur.execute("INSERT INTO articles (doi, name, authors, journal, year, volume, issue, pages) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                             (item['doi'], item['name'], item['authors'], item['journal'], item['year'], item['volume'],
                              item['issue'], item['pages']))
            self.connection.commit()
            print('commited')
        else:
            print('doi exists')
        return item
