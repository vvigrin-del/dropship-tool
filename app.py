from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    """Главная страница: показывает последние сохранённые тренды"""
    try:
        with open("weekly-trends.json", "r", encoding="utf-8") as f:
            trends = json.load(f)
        return jsonify(trends)
    except FileNotFoundError:
        return jsonify({"error": "Тренды ещё не обновлены"}), 404


@app.route("/health")
def health():
    """Простая проверка что сервер работает"""
    return {"status": "ok"}


if __name__ == "__main__":
    # для локального запуска
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
