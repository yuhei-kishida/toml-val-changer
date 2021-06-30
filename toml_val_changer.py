import toml
import tkinter as tk
from attrdict import AttrDict
from tkinter import filedialog, messagebox, ttk
from functools import partial
from pathlib import Path

me = Path(__file__)


def load_toml():
    global ST, idi
    with open(Path(dir), "rt", encoding="utf-8") as st:
        ST = toml.load(st)
        idi = AttrDict(ST["individual"])
    combo["values"] = tuple(idi.keys())
    combo.current(0)


def write_toml():
    ST["individual"][combo.get()] = int(entry.get())
    toml.dump(ST, open(dir, mode="w"))
    messagebox.showinfo(me.stem, f"{entry.get()}を書き込みました")


def open_dir():
    global dir
    dir = filedialog.askopenfilename(initialdir=me)
    if dir:
        load_toml()
        entry.insert(0, idi[combo.get()])
        combo.bind("<<ComboboxSelected>>", _set_text)
    else:
        messagebox.showinfo(me.stem, "ファイルが指定されませんでした")
        return


def _set_text(event):
    entry.delete(0, "end")
    entry.insert(0, idi[combo.get()])


def main():
    global entry, combo
    app = tk.Tk()
    app.title(me.stem)
    app.geometry("300x100")
    entry = tk.Entry(app)
    entry.grid(row=1, column=0)
    combo = ttk.Combobox(app, state="readonly")
    combo.grid(row=0, column=0)
    open_dir_button = tk.Button(text="フォルダを開く", command=open_dir)
    open_dir_button.grid(row=0, column=1)
    change_value_botton = tk.Button(text="変更する", command=write_toml)
    change_value_botton.grid(row=1, column=1)
    app.mainloop()


if __name__ == "__main__":
    main()
