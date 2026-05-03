import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

products = {}

def add_product():
    pid = entry_id.get()
    name = entry_name.get()
    qty = entry_qty.get()
    price = entry_price.get()

    if pid and name and qty and price:
        products[pid] = {"Name": name, "Qty": qty, "Price": price}
        messagebox.showinfo("Success", "Product Added Successfully")
        clear_fields()
    else:
        messagebox.showerror("Error", "Please fill all fields")

def view_products():
    text_box.delete("1.0", "end")
    for pid, details in products.items():
        text_box.insert("end", f"ID: {pid} | {details}\n")

def delete_product():
    pid = entry_id.get()
    if pid in products:
        del products[pid]
        messagebox.showinfo("Deleted", "Product Deleted")
        view_products()
    else:
        messagebox.showerror("Error", "Product Not Found")

def clear_fields():
    entry_id.delete(0, 'end')
    entry_name.delete(0, 'end')
    entry_qty.delete(0, 'end')
    entry_price.delete(0, 'end')

# Window
app = tb.Window(themename="superhero")
app.title("Inventory Management System")
app.geometry("500x500")

# Title
tb.Label(app, text="Inventory Management", font=("Arial", 20, "bold")).pack(pady=10)

# Form Frame
frame = tb.Frame(app)
frame.pack(pady=10)

tb.Label(frame, text="Product ID").grid(row=0, column=0, padx=5, pady=5)
entry_id = tb.Entry(frame, bootstyle="info")
entry_id.grid(row=0, column=1)

tb.Label(frame, text="Name").grid(row=1, column=0, padx=5, pady=5)
entry_name = tb.Entry(frame, bootstyle="info")
entry_name.grid(row=1, column=1)

tb.Label(frame, text="Quantity").grid(row=2, column=0, padx=5, pady=5)
entry_qty = tb.Entry(frame, bootstyle="info")
entry_qty.grid(row=2, column=1)

tb.Label(frame, text="Price").grid(row=3, column=0, padx=5, pady=5)
entry_price = tb.Entry(frame, bootstyle="info")
entry_price.grid(row=3, column=1)

# Buttons
btn_frame = tb.Frame(app)
btn_frame.pack(pady=10)

tb.Button(btn_frame, text="Add", bootstyle="success", command=add_product).grid(row=0, column=0, padx=5)
tb.Button(btn_frame, text="View", bootstyle="primary", command=view_products).grid(row=0, column=1, padx=5)
tb.Button(btn_frame, text="Delete", bootstyle="danger", command=delete_product).grid(row=0, column=2, padx=5)
tb.Button(btn_frame, text="Clear", bootstyle="warning", command=clear_fields).grid(row=0, column=3, padx=5)

# Output Box
text_box = tb.Text(app, height=10)
text_box.pack(pady=10, padx=10, fill="both")

app.mainloop()