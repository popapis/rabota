# TODO решите задачу
import json
from pathlib import Path

def task() -> float:
    try:
        file_path = Path(__file__).parent / 'input.json'

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        total = 0.0
        for item in data:
            score = item.get("score", 0.0)
            weight = item.get("weight", 0.0)
            total += score * weight

        return round(total, 3)

    except FileNotFoundError:
        print(f"Файл input.json не найден")
        return 0.0
    except json.JSONDecodeError as e:
        print(f"Ошибка при чтении JSON: {e}")
        return 0.0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0.0


print(task())
