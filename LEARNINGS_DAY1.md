# Python Learning Journal — Day 1

**Date:** February 16, 2026
**Project:** Product Sourcing Calculator

---

## What is Python?

Python is a programming language — a way of giving precise instructions to a computer. Unlike Excel where you click and type into cells, Python lets you write a script: a sequence of steps the computer follows from top to bottom.

A few things that make Python beginner-friendly:

- It reads almost like English (`if`, `while`, `print`, `input`)
- You don't need to configure much to get started — just write and run
- It's used everywhere: data analysis, automation, web apps, finance tools

Today we used Python to build a real business tool from scratch — a product sourcing calculator that handles currency conversion, shipping methods, multi-product sessions, and saves a history log.

---

## Concepts Learned Today

### 1. Variables
A variable is a named container that stores a value. You make one up — the name is entirely your choice.

```python
product_name = "Wireless Earbuds"
quantity = 200
unit_price = 12.50
```

Python doesn't care what you call it (`product_name`, `p`, `banana`) — it just uses whatever name you pick consistently. The only names you *can't* use are Python's reserved words like `if`, `for`, `print`, `input`.

---

### 2. Data Types
Not all values are the same kind. Python has different types, and the type matters for maths.

| Type | What it is | Example |
|------|-----------|---------|
| `str` | Text (string) | `"Wireless Earbuds"` |
| `int` | Whole number | `200` |
| `float` | Decimal number | `12.50` |

You convert between them using `int()`, `float()`, `str()`.

```python
quantity = int(input("Quantity: "))   # converts typed text → whole number
price    = float(input("Price: "))    # converts typed text → decimal number
```

---

### 3. input() and print()
`input()` pauses the program and waits for the user to type something. Whatever they type comes back as text.

`print()` displays something on screen.

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

---

### 4. f-strings
An f-string lets you mix variables directly into text. Put an `f` before the quote, then wrap variables in `{}`.

```python
product = "Earbuds"
total = 2650.98
print(f"Total cost for {product}: ${total:.2f}")
# Output: Total cost for Earbuds: $2650.98
```

`:.2f` means "show exactly 2 decimal places."

---

### 5. While Loops + Input Validation
A `while` loop keeps repeating until a condition is no longer true. We used this to prevent the program crashing if someone types `3.3` as a quantity.

```python
while True:                              # loop forever...
    user_input = input("Quantity: ")
    if user_input.isdigit():             # ...until input is valid
        quantity = int(user_input)
        break                            # exit the loop
    else:
        print("Please enter a whole number")
```

`break` is the escape hatch — it exits the loop immediately.

---

### 6. try / except
Some conversions crash if the input is unexpected. `try/except` lets you *attempt* something and handle the failure gracefully instead of crashing.

```python
try:
    price = float(user_input)     # attempt this...
except ValueError:
    print("That's not a number")  # ...if it fails, do this instead
```

---

### 7. Functions
A function is a reusable named block of code. You define it once with `def`, then call it by name whenever you need it — instead of copy-pasting the same logic repeatedly.

```python
def get_whole_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a whole number")

# Call it anywhere, as many times as needed:
quantity = get_whole_number("Quantity: ")
```

`return` sends a value back out of the function to wherever it was called.

---

### 8. Dictionaries
A dictionary stores pairs of **key → value**, like a labelled set of boxes. Useful for bundling related values together.

```python
product = {
    "name":         "Earbuds",
    "quantity":     200,
    "final_budget": 2650.98
}

print(product["name"])          # → Earbuds
print(product["final_budget"])  # → 2650.98
```

---

### 9. Lists
A list stores multiple items in order, inside square brackets `[]`. You can add to it, loop through it, and access items by position.

```python
session_products = []                    # start empty
session_products.append(product_one)    # add first product
session_products.append(product_two)    # add second product

# Loop through all of them:
for p in session_products:
    print(p["name"])
```

---

### 10. File Handling (Writing & CSV)
`open()` creates or opens a file. Using `"w"` overwrites it; `"a"` appends to it (adds without deleting existing content). The `with` block closes the file automatically.

```python
# Write a plain text file:
with open("budget.txt", "w") as file:
    file.write("Total: $2650.98\n")

# Append a row to a CSV (opens in Excel):
import csv
with open("history.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["product", "total"])
    writer.writerow({"product": "Earbuds", "total": 2650.98})
```

---

## Code Written Today

### Version 1 — Basic Calculator
Single product. Fixed 10% shipping and 5% buffer. Saves to a `.txt` file.

```python
print("=" * 45)
print("   PRODUCT SOURCING CALCULATOR")
print("=" * 45)

product_name = input("Product name: ")
quantity     = int(input("Quantity (units): "))
unit_price   = float(input("Unit price ($): "))

base_cost      = quantity * unit_price
shipping_cost  = base_cost * 0.10
unexpected_cost = base_cost * 0.05
final_budget   = base_cost + shipping_cost + unexpected_cost

print(f"  Base Cost    : ${base_cost:.2f}")
print(f"  Shipping 10% : ${shipping_cost:.2f}")
print(f"  Buffer   5%  : ${unexpected_cost:.2f}")
print(f"  FINAL BUDGET : ${final_budget:.2f}")

with open(f"{product_name}_budget.txt", "w") as file:
    file.write(f"FINAL BUDGET: ${final_budget:.2f}\n")
```

---

### Version 2 — Full Sourcing Calculator
Multi-product session. CNY/USD conversion. Choice of shipping method (Sea / Air / Land). Comparison table at end of session. Appends to a running `sourcing_history.csv` log.

Key additions:
- Input validation with `while` + `isdigit()` / `try/except`
- Currency conversion: `price_usd = price_cny * CNY_TO_USD`
- Shipping dictionary: `{"1": ("Sea Freight", 0.08), "2": ("Air Freight", 0.25), ...}`
- Functions for reusable logic (`get_whole_number`, `get_shipping_method`, `calculate_product`, etc.)
- Results stored in dictionaries, collected in a list
- Session summary printed as a formatted comparison table
- History saved with `csv.DictWriter` in append mode

---

## Questions I Still Have

- **How do functions actually work in more depth?**
  Specifically: what happens to variables *inside* a function — can the rest of the program see them? (This is called *scope*.)

- **How do I update the CNY rate automatically?**
  Right now it's a hardcoded number at the top of the file (`CNY_TO_USD = 0.138`). Is there a way to fetch the live rate from the internet each time the program runs, so it's always accurate?

---

## What I Want to Learn Next

- **Connect to real exchange rate APIs** — fetch the live CNY/USD rate automatically on each run, instead of updating it manually in the code
- **Learn how to use Excel/CSV files more deeply** — read the history log back into Python, filter by date or product, summarise past sessions
- **Build a simple menu/GUI for this tool** — move beyond the terminal so the calculator has a proper clickable interface
- **Learn about classes and objects** — the next big Python concept after functions; a way to bundle data and behaviour together (imagine a `Product` class that knows how to calculate its own costs)

---

## Key Takeaways

> Python doesn't care what you name your variables — consistency is what matters.

> A program crashing on bad input is a design flaw, not a user error. Always validate.

> Functions are the first step toward writing code you can actually maintain and reuse.

> The jump from v1 to v2 today — from 30 lines to 150 — wasn't about knowing more Python. It was about breaking the problem into smaller pieces.
```