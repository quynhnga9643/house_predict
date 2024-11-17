import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pickle
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')  # format USD

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 350
CONTAINER_PADX = 60

file = ""

window = tk.Tk()
window.title("House Predict")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.resizable(width=False, height=False)
window.eval('tk::PlaceWindow . center')

str_ft = tk.StringVar()
str_m = tk.StringVar()


def choose_file():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=[("SAV files", "*.sav")])
    if file:
        file_label.config(text=file.split("/")[-1])


def on_ok(event=None):
    global file
    try:
        number = float(number_ft_entry.get())
        if not file:
            messagebox.showerror("Error!", "Vui lòng chọn file model.")
            return
        result_label.config(text="Loading...")
        window.update()
        loaded_model = pickle.load(open(file, 'rb'))
        result = loaded_model.predict(pd.DataFrame([
            {"sqft_living": number}
        ]))
        result_label.config(text=f"Kết quả dự đoán:  {locale.currency(result[0], grouping=True)} USD")
    except ValueError:
        messagebox.showerror("Error!", "Vui lòng nhập diện tích nhà.")


def on_change_ft(event=None):
    try:
        str_m.set(round(float(str_ft.get()) * 0.092903, 2))
    except ValueError:
        str_m.set('')


def on_change_m(event=None):
    try:
        str_ft.set(round(float(str_m.get()) / 0.092903, 2))
    except ValueError:
        str_ft.set('')


# === Empty
empt_frame = tk.Frame(window)
empt_frame.pack(pady=20)
# ===

# === File
file_frame = tk.Frame(window)
file_frame.pack(pady=2, fill=tk.X, padx=CONTAINER_PADX)

file_button = tk.Button(file_frame, text="Chọn file model [.sav]", command=choose_file)
file_button.pack(side=tk.LEFT)

# space_file = tk.Label(file_frame, text="", width=0)
# space_file.pack(side=tk.LEFT, expand=True)

file_label = tk.Label(file_frame, text="Chưa chọn file")
file_label.pack(side=tk.LEFT)
# === End File


# === Input sqft_living
input_frame = tk.Frame(window)
input_frame.pack(pady=1, fill=tk.X, padx=CONTAINER_PADX)

entry_label = tk.Label(input_frame, text="Diện tích nhà:")
entry_label.pack(side=tk.LEFT, padx=5)

space_input = tk.Label(input_frame, text="", width=0)
space_input.pack(side=tk.LEFT, expand=True)

# input ft
number_ft_entry = tk.Entry(input_frame, width=11, textvariable=str_ft)
number_ft_entry.pack(side=tk.LEFT, pady=10)
number_ft_entry.bind("<Return>", on_ok)
# number_ft_entry.bind("<KeyRelease>", lambda x: str_m.set(round(float(str_ft.get()) * 0.092903, 2))) # ft to m2
number_ft_entry.bind("<KeyRelease>", on_change_ft)  # ft to m2
unit_label = tk.Label(input_frame, text="ft")
unit_label.pack(side=tk.LEFT)

#
split_label = tk.Label(input_frame, text="~")
split_label.pack(side=tk.LEFT)

# input m2
number_m_entry = tk.Entry(input_frame, width=11, textvariable=str_m)
number_m_entry.pack(side=tk.LEFT, pady=10)
number_m_entry.bind("<Return>", on_ok)
number_m_entry.bind("<KeyRelease>", on_change_m)  # m2 to ft
unit_m_label = tk.Label(input_frame, text="m²")
unit_m_label.pack(side=tk.LEFT)
# === End Input sqft_living

# === Result
result_button = tk.Button(window, text="Xem kết quả", height=2, command=on_ok)
result_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)
# === End Result

window.mainloop()
