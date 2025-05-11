# **Web Crawler Documentation**

This project involved developing a web crawler designed to extract data from various websites, with a focus on CNN. The crawler systematically navigates through article URLs and collects key information such as titles, publication dates, URLs, and summaries. The goal was to automate data extraction for use in further analysis.

---

## **1. Crawling Process and Logic**

We followed a standard web scraping workflow:

- Defined base CNN URL (`https://www.cnn.com`).
- Initialized a set `all_urls` to avoid duplicate URLs.
- Fetched HTML content of CNN's homepage using `request.get()`.
- Used `BeautifulSoup` to parse HTML content.
- Extracted 50 URls using anchor (`<a>`) tags.
- Used `is_article()` to filter out invalid articles (such as ads).
- Extracted `Title`, `Date`, and `Summary` using relevant tags.
- Stored the data into a list called `article_data`.

---

## **2. Challenges and Resolutions**

### **Challenge 1: Handling Duplicate URLs**
- **Problem:** CNN's homepage contains multiple links to the same article.
- **Solution:** A `set` (`all_urls`) ensures only unique URLs are stored.

### **Challenge 2: Filtering Non-Article Pages**
- **Problem:** The homepage includes links to videos, galleries, and other non-news sections.
- **Solution:** The script applies multiple filtering conditions to exclude unwanted URLs.

### **Challenge 3: Inconsistent Article Structure**
- **Problem:** Some articles may not contain a publication date or summary.
- **Solution:** Articles missing critical details are skipped using checks in `extract_article_details()` to avoid exceptions.

### **Challenge 4: Extracting Date**
- **Problem:** Articles included a combined date and time field, but only the date was needed.
- **Solution:** The `extract_date()` function was used to extract only the date by ignoring the time, retaining the last three tokens (e.g., "January 30, 2025") for consistency.

### **Challenge 5: Topic Categorization**
- **Problem:** Some articles may not be able to be categorized using NLP techniques.
- **Solution:** Reliance on URL-based classification as a fallback helped reduce uncategorized articles.

---
