import json

FILE = "storage.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(amount, category, note):
    data = load_data()

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    data.append(expense)
    save_data(data)

def view_expenses():
    return load_data()

def delete_expense(index):
    data = load_data()

    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        return True
    return False

def total_expense():
    data = load_data()
    return sum(item["amount"] for item in data)

def category_summary():
    data = load_data()
    summary = {}

    for item in data:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]

    return summary