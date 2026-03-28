# Smart Expense Tracker (Command Line Application)

## 📌 Project Description

Smart Expense Tracker is a simple command-line application developed using Python that helps users track their daily expenses efficiently.

The application allows users to:
- Add expenses
- View all stored expenses
- Delete expenses
- Calculate total spending
- View category-wise expense summary

This project is designed to demonstrate basic file handling, data structures, and command-line interface development.

---

## 🎯 Objective

The objective of this project is to help users manage their daily expenses in a structured way and improve financial awareness.

---

## 🛠️ Technologies Used

- Python 3
- JSON (for data storage)
- Command Line Interface (CLI)

---

## 📁 Project Structure

smart-expense-tracker/

main.py → Main program (user interface)

expense_manager.py → Handles all logic (add, delete, calculate)

storage.json → Stores expense data

README.md → Project documentation

requirements.txt → Dependencies (empty for this project)

---

## ⚙️ Installation & Setup

Follow the steps below to run this project on your system.

### Step 1: Install Python

Download Python from:
https://www.python.org/downloads/

Install Python and make sure to check:
"Add Python to PATH"

---

### Step 2: Clone the Repository

Open Command Prompt and run:

git clone https://github.com/YOURUSERNAME/smart-expense-tracker

---

### Step 3: Navigate to Project Folder

cd smart-expense-tracker

---

### Step 4: Run the Program

python main.py

---

## ▶️ How to Use the Application

After running the program, you will see a menu:

Smart Expense Tracker

1 Add Expense  
2 View Expenses  
3 Delete Expense  
4 Total Spending  
5 Category Summary  
6 Exit  

---

### ➤ Option 1: Add Expense

- Enter amount (example: 200)
- Enter category (Food, Travel, etc.)
- Enter note (example: Lunch)

---

### ➤ Option 2: View Expenses

Displays all saved expenses in this format:

Index | Amount | Category | Note

---

### ➤ Option 3: Delete Expense

- Enter the index number shown in "View Expenses"
- The selected expense will be deleted

---

### ➤ Option 4: Total Spending

Shows total money spent

---

### ➤ Option 5: Category Summary

Displays spending grouped by category

Example:
Food : 500  
Travel : 300  

---

### ➤ Option 6: Exit

Closes the program

---

## 💾 Data Storage

All expenses are stored in a file named:

storage.json

This file automatically updates when you add or delete expenses.

---

## 🧪 Example Run

Add expense:

Amount: 100  
Category: Food  
Note: Lunch  

View expense:

0 | 100 | Food | Lunch  

---

## 🚀 How to Upload Project to GitHub

Follow these steps carefully:

### Step 1: Initialize Git

git init

---

### Step 2: Add Files

git add .

---

### Step 3: Commit Changes

git commit -m "Initial Expense Tracker Project"

---

### Step 4: Create Repository on GitHub

Go to:
https://github.com

Click "New Repository"

Repository Name:
smart-expense-tracker

Set it to PUBLIC

Click "Create Repository"

---

### Step 5: Connect Local Project to GitHub

git branch -M main

git remote add origin https://github.com/YOURUSERNAME/smart-expense-tracker.git

---

### Step 6: Push Code

git push -u origin main

---

## 📌 Important Notes

- Do NOT submit links with /tree/main or /blob
- Submit only the root repository URL:

https://github.com/YOURUSERNAME/smart-expense-tracker

---

## 📈 Features Summary

✔ Add expenses  
✔ View expenses  
✔ Delete expenses  
✔ Total spending calculation  
✔ Category-wise summary  
✔ Data stored in JSON file  
✔ Runs in command-line  

---

## 👨‍💻 Author

Your Name

---

## 📚 Conclusion

This project demonstrates how basic programming concepts like file handling, loops, and functions can be used to build a useful real-world application.

It helps users manage finances effectively and serves as a foundation for more advanced financial management systems.
