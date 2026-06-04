# Web Scraper

A Python web scraper built with BeautifulSoup that extracts data from multiple sites, including job listings from the Real Python fake jobs site and quotes from quotes.toscrape.com, with support for keyword, author, and tag filtering via a CLI.

## Local Setup

### Prerequisites
- Python 3.10+

### Installation
1. Clone the repository:
```bash
git clone https://github.com/MihsterRobot/web-scraper.git
cd web-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage
```bash
python -m web_scraper.main
```

Follow the prompts to select a scraper and optionally filter results.
