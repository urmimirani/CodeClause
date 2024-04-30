import tkinter as tk
from tkinter import messagebox

# Currency conversion rates (example rates)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.83,
    "GBP": 0.72,
    "JPY": 109.24,
    "INR": 75.23
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            messagebox.showerror("Error", "Currency not supported")
        else:
            converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
            result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Create Tkinter window
window = tk.Tk()
window.title("Currency Converter")

# Labels
amount_label = tk.Label(window, text="Amount:")
amount_label.pack()

# Entry for amount
amount_entry = tk.Entry(window)
amount_entry.pack()

# From currency dropdown
from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.pack()

from_currency_var = tk.StringVar(window)
from_currency_var.set("USD")  # Default value

from_currency_menu = tk.OptionMenu(window, from_currency_var, *exchange_rates.keys())
from_currency_menu.pack()

# To currency dropdown
to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.pack()

to_currency_var = tk.StringVar(window)
to_currency_var.set("EUR")  # Default value

to_currency_menu = tk.OptionMenu(window, to_currency_var, *exchange_rates.keys())
to_currency_menu.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
