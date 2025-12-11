from expense import Expense
from file_manager import load_expenses, append_expense, save_expenses
from reports import category_summary, monthly_report, save_text_report
from utils import parse_date, validate_category, format_currency
from datetime import datetime

class Menu:
    def __init__(self):
        self.expenses = load_expenses()

    def clear_screen(self):
        print("\n"*2)

    def pause(self):
        input("\nPress Enter to continue...")

    def show_main(self):
        self.clear_screen()
        print("==========================================")
        print("     PERSONAL FINANCE MANAGER")
        print("==========================================\n")
        print("MAIN MENU:")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category-wise Summary")
        print("4. Generate Monthly Report")
        print("5. Search Expenses")
        print("6. Backup Data")
        print("7. Exit")

    def add_expense(self):
        print("\nADD NEW EXPENSE:")
        try:
            amount=float(input("Enter amount: ").strip())
        except:
            print("Invalid amount.")
            return
        cat=validate_category(input("Enter category: ").strip())
        date=input("Enter date (YYYY-MM-DD): ").strip()
        if not parse_date(date):
            print("Invalid date.")
            return
        desc=input("Enter description: ").strip()
        e=Expense(amount,cat,date,desc)
        from file_manager import append_expense
        append_expense(e)
        self.expenses.append(e)
        print("Expense added!")

    def view_all(self):
        print("\nALL EXPENSES:")
        for e in self.expenses:
            print(e)

    def view_summary(self):
        print("\nCATEGORY SUMMARY:")
        summary=category_summary(self.expenses)
        for c,a in summary.items():
            print(f"{c}: {format_currency(a)}")

    def generate_monthly_report(self):
        print("\nMONTHLY REPORT:")
        year=int(input("Year (YYYY): "))
        month=int(input("Month (1-12): "))
        entries=monthly_report(self.expenses,year,month)
        lines=[f"Report {year}-{month:02d}"]+[str(e) for e in entries]
        save_text_report(f"report_{year}_{month}",lines)

    def search_expenses(self):
        q=input("Search keyword: ").lower()
        results=[e for e in self.expenses if q in e.category.lower() or q in e.description.lower() or q in e.date]
        for r in results:
            print(r)

    def backup_data(self):
        from shutil import copy2
        src="data/expenses.csv"
        if not os.path.exists(src):
            print("No data.")
            return
        backup=f"data/backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        copy2(src,backup)
        print("Backup created:",backup)

    def run(self):
        while True:
            self.show_main()
            ch=input("Enter choice: ")
            if ch=="1": self.add_expense(); self.pause()
            elif ch=="2": self.view_all(); self.pause()
            elif ch=="3": self.view_summary(); self.pause()
            elif ch=="4": self.generate_monthly_report(); self.pause()
            elif ch=="5": self.search_expenses(); self.pause()
            elif ch=="6": self.backup_data(); self.pause()
            elif ch=="7": save_expenses(self.expenses); break
