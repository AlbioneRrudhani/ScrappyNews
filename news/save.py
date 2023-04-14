import json

def save_news_items(news_items):
    with open("news_items.json", "w", encoding="utf-8") as jsonfile:
        json.dump(news_items, jsonfile, ensure_ascii=False, indent=4)