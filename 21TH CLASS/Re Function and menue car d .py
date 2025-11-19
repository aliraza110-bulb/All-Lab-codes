import re

def search_function():
    text = input("Enter text: ")
    pattern = input("Enter pattern to search: ")
    result = re.search(pattern, text)
    if result:
        print(f"✅ Pattern found at index {result.start()} to {result.end()}")
    else:
        print("❌ Pattern not found.")

def match_function():
    text = input("Enter text: ")
    pattern = input("Enter pattern to match (only at start): ")
    result = re.match(pattern, text)
    if result:
        print(f"✅ Pattern matches at the beginning: {result.group()}")
    else:
        print("❌ Pattern does not match at the start.")

def findall_function():
    text = input("Enter text: ")
    pattern = input("Enter pattern to find all matches: ")
    result = re.findall(pattern, text)
    if result:
        print(f"✅ All matches found: {result}")
    else:
        print("❌ No matches found.")

def sub_function():
    text = input("Enter text: ")
    pattern = input("Enter pattern to replace: ")
    replacement = input("Enter replacement text: ")
    result = re.sub(pattern, replacement, text)
    print(f"✅ Updated text: {result}")

def split_function():
    text = input("Enter text: ")
    pattern = input("Enter pattern to split text: ")
    result = re.split(pattern, text)
    print(f"✅ Text split into: {result}")

def main():
    while True:
        print("\n" + "="*50)
        print("🧠 REGEX (re) MODULE MENU")
        print("="*50)
        print("1. re.search() - Find first match")
        print("2. re.match()  - Match only at start")
        print("3. re.findall() - Find all matches")
        print("4. re.sub() - Replace text")
        print("5. re.split() - Split text")
        print("6. Exit")
        print("="*50)

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            search_function()
        elif choice == '2':
            match_function()
        elif choice == '3':
            findall_function()
        elif choice == '4':
            sub_function()
        elif choice == '5':
            split_function()
        elif choice == '6':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1–6.")

main()
