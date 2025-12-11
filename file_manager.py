import csv
from typing import List
from pathlib import Path
from expense import Expense

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CSV_FILE = DATA_DIR / "expenses.csv"

HEADERS = ["Date", "Category", "Amount", "Description"]

def save_expenses(expenses: List[Expense], filename: Path = CSV_FILE):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        for e in expenses:
            writer.writerow([e.date, e.category, f"{e.amount:.2f}", e.description])

def load_expenses(filename: Path = CSV_FILE) -> List[Expense]:
    expenses=[]
    if not filename.exists():
        return expenses
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                expenses.append(Expense(
                    amount=float(row.get("Amount",0)),
                    category=row.get("Category","Other"),
                    date=row.get("Date",""),
                    description=row.get("Description","")
                ))
            except:
                continue
    return expenses
