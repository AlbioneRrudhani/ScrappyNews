import feedparser
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from datetime import datetime

from utils.config import feeds


def extract_pub_date(entry: feedparser.FeedParserDict) -> str:
    """
    Extracts and formats the publication date of a news item.

    Args:
        entry (feedparser.FeedParserDict): The dictionary containing the news item.

    Returns:
        str: The publication date in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    try:
        pub_date: datetime = datetime(*entry.published_parsed[:6])
        return pub_date.strftime("%Y-%m-%d %H:%M:%S")
    except (KeyError, ValueError):
        # Handle missing or invalid publication date
        return ""


def extract_description(entry: feedparser.FeedParserDict) -> str:
    """
    Extracts the description of a news item and removes HTML tags.

    Args:
        entry (feedparser.FeedParserDict): The dictionary containing the news item.

    Returns:
        str: The description of the news item without HTML tags.
    """
    try:
        soup_desc: BeautifulSoup = BeautifulSoup(entry.description, 'html.parser')
        return soup_desc.get_text(separator=' ')
    except (KeyError, AttributeError):
        # Handle missing or invalid description
        return ""


def extract_content(entry: feedparser.FeedParserDict) -> str:
    """
    Extracts the content of a news item and removes HTML tags.

    Args:
        entry (feedparser.FeedParserDict): The dictionary containing the news item.

    Returns:
        str: The content of the news item without HTML tags.
    """
    try:
        content: str = entry.content[0].value if entry.content else ""
        soup_content: BeautifulSoup = BeautifulSoup(content, 'html.parser')
        for elem in soup_content(["script", "style"]):
            elem.extract()
        return soup_content.get_text(separator=' ')
    except (KeyError, AttributeError):
        # Handle missing or invalid content
        return ""


def extract_news_items() -> List[Dict[str, Any]]:
    """
    Extracts news items from RSS feeds and returns a list of dictionaries.

    Returns:
        List[Dict[str, Any]]: The list of news items as dictionaries.
    """
    news_items: List[Dict[str, Any]] = []
    for feed in feeds:
        feed_url: str = feed["url"]
        source: str = feed["source"]
        feed_data = feedparser.parse(feed_url)
        for entry in feed_data.entries:
            title: str = entry.title
            pub_date_str: str = extract_pub_date(entry)
            description: str = extract_description(entry)
            content: str = extract_content(entry)
            category: str = entry.category if "category" in entry else ""
            news_item: Dict[str, Any] = {
                "Title": title,
                "Description": description,
                "Content": content,
                "Source": source,
                "Category": category,
                "PubDate": pub_date_str
            }
            news_items.append(news_item)

    return news_items