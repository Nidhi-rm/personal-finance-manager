from dataclasses import dataclass

@dataclass
class Expense:
    amount: float
    category: str
    date: str
    description: str

    def __post_init__(self):
        self.amount = float(self.amount)

    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount:.2f} - {self.description}"
