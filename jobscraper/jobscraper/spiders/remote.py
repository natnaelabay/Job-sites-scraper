import scrapy
import dateparser
import json


class RemoteSpider(scrapy.Spider):
    name = "remote"
    allowed_domains = ["remote.co"]
    current_page = 1
    number_of_pages = 1
    urls = [
        "https://remote.co/remote-jobs/developer/page/",
        "https://remote.co/remote-jobs/design/page/",
        "https://remote.co/remote-jobs/it/"
    ]
    api_url = urls[2]

    def start_requests(self):
        yield scrapy.Request(
            url=self.api_url + str(self.current_page) + "/",
            callback=self.parse_job,
        )

    def parse_job(self, response):
        if self.number_of_pages == 1:
            self.number_of_pages += (
                len(response.css("nav div.pagination.number-pagination > a")) - 1
            )

        jobs = response.css("div.card-body.p-0 > a")

        for job in jobs:
            yield {
                "job_url" : "https://remote.co/" + job.attrib["href"],
                "job_id": "-",
                "title": job.css(".font-weight-bold.larger::text").get().replace("\n", "").replace("&nbsp", ""),
                "company": job.css(".m-0.text-secondary::text").get().strip().replace("\n", "").replace("  ", "").replace("|", ""),
                "date": dateparser.parse(job.css("date::text").get().strip()).strftime(
                    "%Y-%m-%d"
                ),
                "img": job.css("div.row.no-gutters.align-items-center img")
                .attrib["data-lazy-src"]
                .strip(),
                "source": "Remote.co",
                "tags": json.dumps(
                    [c.get().replace("&nbsp", "") for c in job.css("span.badge.badge-success small::text")]
                ),
                "location": "Remote"
            }
        if self.current_page < self.number_of_pages:
            self.current_page += 1
            yield scrapy.Request(
                url=self.api_url + str(self.current_page) + "/",
                callback=self.parse_job,
            )