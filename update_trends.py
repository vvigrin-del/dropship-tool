import requests
import json

# URL открытого JSON с трендовыми видео TikTok (пример с Apify)
URL = "https://api.apify.com/v2/datasets/your_dataset_id/items?format=json"

def fetch_trends():
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        # Преобразуем в формат для weekly-trends.json
        trends = {"pets": [], "fitness": []}

        for item in data:
            # Простейшая фильтрация по нишам (пример)
            title = item.get("title", "Unknown")
            views = int(item.get("views", 0))
            likes = int(item.get("likes", 0))
            video_url = item.get("url", "")

            # Пример логики: если в названии есть ключевые слова, относим к нише
            if any(k in title.lower() for k in ["dog", "cat", "pet"]):
                trends["pets"].append({"title": title, "views": views, "likes": likes, "video_url": video_url})
            elif any(k in title.lower() for k in ["yoga", "fitness", "band", "dumbbell"]):
                trends["fitness"].append({"title": title, "views": views, "likes": likes, "video_url": video_url})

        # Ограничим до топ 10 для каждой ниши
        trends["pets"] = sorted(trends["pets"], key=lambda x: x["views"], reverse=True)[:10]
        trends["fitness"] = sorted(trends["fitness"], key=lambda x: x["views"], reverse=True)[:10]

        # Сохраняем в weekly-trends.json
        with open("weekly-trends.json", "w") as f:
            json.dump(trends, f, indent=2)

        print("Weekly trends updated successfully!")

    except Exception as e:
        print("Error fetching trends:", e)

if __name__ == "__main__":
    fetch_trends()
