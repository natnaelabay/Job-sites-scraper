# Job Scrapy

Job Scrapy is an open-source project that allows you to scrape job listings from various sources. This README provides instructions on how to set up the project, create a virtual environment, install necessary packages, and start the scraping process.

## Prerequisites

- Python 3.x installed on your system.
- [Scrapy](https://scrapy.org/) installed (for web scraping).
- [Django](https://www.djangoproject.com/) installed (for the API).

## Getting Started

Follow these steps to set up and run the Job Scraper project:

### 1. Clone the Repository

```bash
git clone https://github.com/natnaelabay/Job-sites-scraper.git
```

### 2. Create a Virtual Environment
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
```
### 3. Activate the Virtual Environment
```bash
# On Windows
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Configure Scrapy
Navigate to the `jobscraper` directory (where _run.py is located) and adjust the Scrapy settings as needed.

### 6. Run Scrapy to Start Scraping

```bash
# inside jobscraper
python _run.py
```

### 7. Set Up the API (Django)
For the stats to work you need to download [en_core_web_sm](https://spacy.io/models) from spaCy
```bash
# Inside the api directory
python manage.py migrate && python manage.py runserver
```
The Django API will be accessible at http://localhost:8000/.


### Contributing
Contributions are welcome! Please read the [Contributing Guidelines](https://gist.github.com/briandk/3d2e8b3ec8daf5a27a62) installed (for the API) for details on how to contribute to this project.
