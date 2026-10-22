from re import *
from json import *
from logging import *
from collections import *

basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename="processing.log", encoding="utf-8")
p = compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (?P<ip>\d{1,3}(?:\.\d{1,3}){3}) (?P<method>GET|POST|PUT|DELETE|PATCH) (?P<url>\S+) (?P<status>\d{3})")
methods = Counter()
urls = Counter()
errors = 0
total = 0
bad = 0
try:
    with open("access.log", encoding="utf-8") as f:
        for i in f:
            i = i.strip()
            if (not i):
                continue
            m = fullmatch(p, i)
            if (not m):
                bad += 1
                warning("Некорректная строка: %s", i)
                continue
            d = m.groupdict()
            method = d["method"]
            url = d["url"]
            status = int(d["status"])
            methods[method] += 1
            urls[url] += 1
            total += 1
            if (400 <= status < 500):
                errors += 1
            info("Обработан запрос: %s", i)
except OSError as e:
    error("Ошибка чтения файла: %s", e)
    print("Не удалось прочитать access.log:", e)
else:
    most = urls.most_common(1)
    if (most):
        most = most[0][0]
    else:
        most = None
    stats = {
        "requests_by_method": dict(methods),
        "errors_4xx": errors,
        "most_common_url": most,
        "total_requests": total,
        "invalid_lines": bad
    }
    try:
        with open("stats.json", "w", encoding="utf-8") as f:
            dump(stats, f, ensure_ascii=False, indent=4)
        info("Статистика сохранена в stats.json")
        print(dumps(stats, ensure_ascii=False, indent=4))
    except OSError as e:
        error("Ошибка сохранения статистики: %s", e)
        print("Не удалось сохранить stats.json:", e)