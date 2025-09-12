import json
from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Dropship Trend Products</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 30px; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background-color: #f4f4f4; }
    a { color: #1a73e8; text-decoration: none; }
    a:hover { text-decoration: underline; }
    h2, h3 { margin-bottom: 10px; }
  </style>
</head>
<body>
  <h2>Трендовые товары для дропшипинга</h2>
  {% for category, items in trends.items() %}
    <h3>{{ category|capitalize }}</h3>
    <table>
      <tr>
        <th>Название</th>
        <th>Просмотры</th>
        <th>Лайки</th>
        <th>Видео</th>
      </tr>
      {% for t in items %}
        <tr>
          <td>{{ t.title }}</td>
          <td>{{ t.views }}</td>
          <td>{{ t.likes }}</td>
          <td><a href="{{ t.video_url }}" target="_blank">Смотреть</a></td>
        </tr>
      {% endfor %}
    </table>
  {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    # Читаем тренды из локального JSON
    with open("weekly-trends.json", "r") as f:
        trends = json.load(f)
    return render_template_string(TEMPLATE, trends=trends)

if __name__ == "__main__":
    app.run(debug=True)
