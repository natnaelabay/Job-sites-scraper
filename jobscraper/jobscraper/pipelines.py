# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

# docker run --name postgres-scrap -e POSTGRES_DB=scrap -e POSTGRES_USER=scrap -e POSTGRES_PASSWORD=scrap -d -p 5433:5432 postgres:latest


class JobscraperPipeline:
    def __init__(self):
        hostname = "localhost"
        username = "scrap"
        password = "scrap"  # your password
        database = "scrap"

        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database
        )
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        if item["source"] == "Remote.co":
            self.cur.execute(
                """ insert into jobs_joblisting (job_id,title,company,date,img,source, tags,job_url,job_url,  created_at) values (%s,%s,%s,%s,%s,%s,%s,%s,%s, CURRENT_TIMESTAMP)""",
                (
                    item["job_id"],
                    item["title"],
                    item["company"],
                    item["date"],
                    item["img"],
                    item["source"],
                    item["tags"],
                    item["job_url"],
                    item["location"],
                ),
            )
        else:
            self.cur.execute(
                """ insert into jobs_joblisting (job_id,title,company,date,img,source, location, job_url, created_at) values (%s,%s,%s,%s,%s,%s, %s,%s, CURRENT_TIMESTAMP)""",
                (
                    item["job_id"],
                    item["title"],
                    item["company"],
                    item["date"],
                    item["img"],
                    item["source"],
                    item["location"],
                    item["job_url"],
                ),
            )
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
