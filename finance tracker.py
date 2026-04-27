import matplotlib.pyplot as plt

# Data storage
expenses = {}
total_spent = 0
savings_goal = 0

# Function to add expense
def add_expense(amount, category)
    global total_spent
    total_spent += amount
    
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    
    print(f"✅ Added ₹{amount} to {category}")

# Function to set savings goal
def set_goal(goal):
    global savings_goal
    savings_goal = goal
    print(f"🎯 Savings goal set to ₹{goal}")

# Function to show summary
def show_summary():
    print("\n📊 Expense Summary:")
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount}")
    
    print(f"\nTotal Spent: ₹{total_spent}")
    
    if savings_goal > 0:
        saved = savings_goal - total_spent
        print(f"Savings Goal: ₹{savings_goal}")
        print(f"Remaining to Save: ₹{saved}")

# Function to show chart
def show_chart():
    if not expenses:
        print("No data to show.")
        return
    
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    
    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

# Chatbot loop
def chatbot():
    print("🤖 Personal Finance Chatbot Started!")
    print("Type 'help' to see commands.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if "add" in user_input:
            try:
                parts = user_input.split()
                amount = int(parts[1])
                category = parts[2]
                add_expense(amount, category)
            except:
                print("❌ Format: add 500 food")
        
        elif "goal" in user_input:
            try:
                goal = int(user_input.split()[1])
                set_goal(goal)
            except:
                print("❌ Format: goal 5000")
        
        elif "summary" in user_input:
            show_summary()
        
        elif "chart" in user_input:
            show_chart()
        
        elif "help" in user_input:
            print("""
Commands:
- add <amount> <category>  (add 500 food)
- goal <amount>           (goal 5000)
- summary
- chart
- exit
            """)
        
        elif "exit" in user_input:
            print("👋 Goodbye!")
            break
        
        else:
            print("❓ I didn't understand. Type 'help'.")

# Run chatbot
chatbot()