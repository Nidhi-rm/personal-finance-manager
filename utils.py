from datetime import datetime

VALID_CATEGORIES = ["Food","Transport","Entertainment","Shopping","Other"]

def parse_date(date_str):
    try:
        datetime.strptime(date_str,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def format_currency(amount):
    return f"₹{amount:.2f}"

def validate_category(cat):
    cat = cat.capitalize()
    return cat if cat in VALID_CATEGORIES else "Other"
