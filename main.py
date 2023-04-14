# import logging

# from news.extract import extract_news_items
# from news.process import process_news_items
# from news.save import save_news_items


# def main():
#     try:
#         news_items = extract_news_items()
#         news_items = process_news_items(news_items)
#         save_news_items(news_items)
#     except Exception as e:
#         # log the error message and traceback
#         logging.error(f"An error occurred: {e}", exc_info=True)


# if __name__ == '__main__':
#     # configure logging
#     logging.basicConfig(
#         filename='news_scraper.log',
#         level=logging.ERROR,
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )
#     main()



import logging
from typing import List

from news.extract import extract_news_items
from news.process import process_news_items
from news.save import save_news_items


def main() -> None:
    try:
        news_items: List[dict] = extract_news_items()
        news_items = process_news_items(news_items)
        save_news_items(news_items)
    except Exception as e:
        logging.exception(f"An error occurred: {e}")


if __name__ == '__main__':
    # configure logging
    logging.basicConfig(
        filename='news_scraper.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    main()