import tkinter as tk
from tkinter import ttk, messagebox

# Main window
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("900x600")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="HOTEL MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="darkblue",
    fg="white",
    pady=15
)
title.pack(fill="x")

# Customer Details Frame
customer_frame = tk.LabelFrame(
    root,
    text="Customer Details",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)
customer_frame.pack(fill="x", padx=20, pady=10)

# Name
tk.Label(customer_frame, text="Customer Name:").grid(row=0, column=0, padx=10, pady=8)
name_entry = tk.Entry(customer_frame, width=30)
name_entry.grid(row=0, column=1)

# Phone
tk.Label(customer_frame, text="Phone Number:").grid(row=0, column=2, padx=10)
phone_entry = tk.Entry(customer_frame, width=25)
phone_entry.grid(row=0, column=3)

# Room
tk.Label(customer_frame, text="Room Number:").grid(row=1, column=0, padx=10, pady=8)

room_combo = ttk.Combobox(
    customer_frame,
    values=["101", "102", "103", "104", "105"],
    width=27,
    state="readonly"
)
room_combo.grid(row=1, column=1)

# Number of Days
tk.Label(customer_frame, text="Number of Days:").grid(row=1, column=2, padx=10)

days_entry = tk.Entry(customer_frame, width=25)
days_entry.grid(row=1, column=3)

# Room Type
tk.Label(customer_frame, text="Room Type:").grid(row=2, column=0, padx=10, pady=8)

type_combo = ttk.Combobox(
    customer_frame,
    values=["Single", "Double", "Deluxe"],
    width=27,
    state="readonly"
)
type_combo.grid(row=2, column=1)

# Price
tk.Label(customer_frame, text="Price Per Day:").grid(row=2, column=2, padx=10)

price_entry = tk.Entry(customer_frame, width=25)
price_entry.grid(row=2, column=3)


# Functions
def calculate_bill():
    try:
        days = int(days_entry.get())
        price = float(price_entry.get())

        total = days * price

        bill_text.delete("1.0", tk.END)

        bill_text.insert(tk.END, "        HOTEL BILL\n")
        bill_text.insert(tk.END, "-----------------------------\n")
        bill_text.insert(tk.END, f"Customer Name : {name_entry.get()}\n")
        bill_text.insert(tk.END, f"Phone Number  : {phone_entry.get()}\n")
        bill_text.insert(tk.END, f"Room Number   : {room_combo.get()}\n")
        bill_text.insert(tk.END, f"Room Type     : {type_combo.get()}\n")
        bill_text.insert(tk.END, f"Days          : {days}\n")
        bill_text.insert(tk.END, f"Price/Day     : ₹{price}\n")
        bill_text.insert(tk.END, "-----------------------------\n")
        bill_text.insert(tk.END, f"TOTAL BILL    : ₹{total}\n")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid number of days and price."
        )


def clear_data():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    room_combo.set("")
    days_entry.delete(0, tk.END)
    type_combo.set("")
    price_entry.delete(0, tk.END)
    bill_text.delete("1.0", tk.END)


def checkout():
    if name_entry.get() == "":
        messagebox.showwarning("Warning", "Please enter customer details.")
    else:
        messagebox.showinfo(
            "Check Out",
            "Customer checked out successfully!"
        )
        clear_data()


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Calculate Bill",
    command=calculate_bill,
    width=15,
    bg="green",
    fg="white"
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Check Out",
    command=checkout,
    width=15,
    bg="orange"
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_data,
    width=15,
    bg="red",
    fg="white"
).grid(row=0, column=2, padx=10)

tk.Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    width=15,
    bg="black",
    fg="white"
).grid(row=0, column=3, padx=10)


# Bill Area
bill_frame = tk.LabelFrame(
    root,
    text="Bill Details",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)
bill_frame.pack(fill="both", expand=True, padx=20, pady=10)

bill_text = tk.Text(
    bill_frame,
    height=10,
    width=80,
    font=("Arial", 12)
)
bill_text.pack()

# Run application
root.mainloop()