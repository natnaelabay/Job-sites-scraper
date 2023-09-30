import scrapy
import dateparser


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    # start_urls = ["https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=software%2Bengineering%2C%2BWeb%2Bdevelopment%2C%2Bfrontend%2C%2Bbackend&location=remote&geoId=&start=75"]
    api_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=software%2Bengineering%2C%2BWeb%2Bdevelopment%2C%2Bfrontend%2C%2Bbackend&location=remote&geoId=&start="

    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(
            url=first_url,
            callback=self.parse_job,
            meta={"first_job_on_page": first_job_on_page},
        )

    def parse_job(self, response):
        first_job_on_page = response.meta["first_job_on_page"]

        jobs = response.css("li")
        no_jobs = len(jobs)

        for job in jobs:
            yield {
                "job_url": job.css(
                    "a.base-card__full-link.absolute.top-0.right-0.bottom-0"
                ).attrib["href"],
                "job_id": job.css("div.job-search-card")
                .attrib["data-entity-urn"]
                .split(":")[-1]
                .strip(),
                "title": job.css("span.sr-only::text").get().strip(),
                "company": job.css(
                    "div.base-search-card__info h4.base-search-card__subtitle a.hidden-nested-link::text"
                )
                .get()
                .strip(),
                "date": dateparser.parse(job.css("time::text").get().strip()).strftime(
                    "%Y-%m-%d"
                ),
                "img": job.css("img").attrib["data-delayed-url"].strip(),
                "source": "Linkedin",
                "location": job.css("span.job-search-card__location::text")
                .get()
                .strip(),
            }
        if no_jobs >= 50:
            print("50============== done")
        elif no_jobs > 0:
            first_job_on_page = int(first_job_on_page) + 25
            first_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=first_url, callback=self.parse_job, meta={"first_job_on_page" : first_job_on_page})
