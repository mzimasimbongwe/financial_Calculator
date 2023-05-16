import math
from tkinter import *

def calculate_investment():
    deposit = float(deposit_entry.get())
    rate = float(rate_entry.get()) / 100
    years = float(years_entry.get())
    interest = interest_var.get()

    if interest == "Simple":
        total = deposit * (1 + rate * years)
    elif interest == "Compound":
        total = deposit * math.pow((1 + rate), years)
    else:
        result_label.config(text="Invalid input. Please select Simple or Compound.")
        return

    result_label.config(text=f"Your total investment after {years} years is: R{total:.2f}")

    # Clear input text boxes
    deposit_entry.delete(0, END)
    rate_entry.delete(0, END)
    years_entry.delete(0, END)

def calculate_bond():
    house_value = float(house_value_entry.get())
    interest = float(interest_entry.get()) / 100 / 12
    months = int(months_entry.get())

    repayment = (interest * house_value) / (1 - math.pow((1 + interest), -months))

    result_label.config(text=f"Your monthly bond repayment is: R{repayment:.2f}")

    # Clear input text boxes
    house_value_entry.delete(0, END)
    interest_entry.delete(0, END)
    months_entry.delete(0, END)

def exit_program():
    root.destroy()

root = Tk()
root.geometry("500x600")
root.title("Financial Calculator")

# Investment section
investment_frame = Frame(root)
investment_frame.pack(pady=20)

deposit_label = Label(investment_frame, text="Deposit:")
deposit_label.grid(row=0, column=0)
deposit_entry = Entry(investment_frame)
deposit_entry.grid(row=0, column=1)

rate_label = Label(investment_frame, text="Interest Rate (%):")
rate_label.grid(row=1, column=0)
rate_entry = Entry(investment_frame)
rate_entry.grid(row=1, column=1)

years_label = Label(investment_frame, text="Years:")
years_label.grid(row=2, column=0)
years_entry = Entry(investment_frame)
years_entry.grid(row=2, column=1)

interest_label = Label(investment_frame, text="Interest Type:")
interest_label.grid(row=3, column=0)
interest_var = StringVar()
interest_dropdown = OptionMenu(investment_frame, interest_var, "Simple", "Compound")
interest_dropdown.grid(row=3, column=1)

investment_button = Button(investment_frame, text="Calculate", command=calculate_investment)
investment_button.grid(row=4, columnspan=2)

# Bond section
bond_frame = Frame(root)
bond_frame.pack(pady=20)

house_value_label = Label(bond_frame, text="House Value:")
house_value_label.grid(row=0, column=0)
house_value_entry = Entry(bond_frame)
house_value_entry.grid(row=0, column=1)

interest_label = Label(bond_frame, text="Interest Rate (%):")
interest_label.grid(row=1, column=0)
interest_entry = Entry(bond_frame)
interest_entry.grid(row=1, column=1)

months_label = Label(bond_frame, text="Months:")
months_label.grid(row=2, column=0)
months_entry = Entry(bond_frame)
months_entry.grid(row=2, column=1)

bond_button = Button(bond_frame, text="Calculate", command=calculate_bond)
bond_button.grid(row=3, columnspan=2)

# Result label
result_label = Label(root, text="")
result_label.pack(pady=20)

exit_button = Button(root, text="Exit", command=exit_program, font="arial 15")
exit_button.pack(pady=20)

root.mainloop()
