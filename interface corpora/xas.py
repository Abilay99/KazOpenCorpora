import tkinter as tk
import tkinter.ttk as ttk
  
  
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
  
  
root = tk.Tk()
table = Table(root, headings=('aaa', 'bbb', 'ccc'), rows=((123, 456, 789), ('abc', 'def', 'ghk')))
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()