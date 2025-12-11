from typing import List, Dict
from collections import defaultdict
from expense import Expense
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

def category_summary(expenses: List[Expense]):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount
    return dict(summary)

def monthly_report(expenses: List[Expense], year, month):
    result=[]
    for e in expenses:
        try:
            dt=datetime.strptime(e.date,"%Y-%m-%d")
            if dt.year==year and dt.month==month:
                result.append(e)
        except:
            continue
    return result

def save_text_report(title, lines, filename=None):
    if not filename:
        safe=title.replace(" ","_").lower()
        filename=REPORTS_DIR / f"{safe}.txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write("
".join(lines))
    return filename
