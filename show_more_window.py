from tkinter import ttk, Tk


class ShowMore:
    def __init__(self):
        self.frame = Tk()
        self.tree = ttk.Treeview(self.frame, columns=[1, 2], height=10, show='headings')
        self.tree.pack(side='left', fill='x')
        self.tree.heading(1, text='Title')
        self.tree.heading(2, text='Link')
        self.tree.column(1, width=500)
        self.tree.column(2, width=500)

        self.scroll_hor = ttk.Scrollbar(self.frame, orient='vertical', command=self.tree.yview)
        self.scroll_hor.pack(side='right', fill='y')

        self.tree.configure(yscrollcommand=self.scroll_hor.set)

        self.frame.mainloop()


f = ShowMore()