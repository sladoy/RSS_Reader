from tkinter import Label, Button, ttk, Toplevel


def error_window():
    frame = Toplevel(takefocus=True)
    frame.focus()
    frame.title('Error Window')
    frame.geometry('250x100')
    label = Label(frame, text="You didn't selected a position from the list")
    label.pack()
    button = Button(frame, text='Ok', command=frame.destroy)
    button.pack()
    frame.mainloop()


def start_error_window():
    frame = Toplevel(takefocus=True)
    frame.focus()
    frame.title('Error Window')
    frame.geometry('250x100')
    label = Label(frame, text="You didn't input valid RSS link")
    label.pack()
    button = Button(frame, text='Ok', command=frame.destroy)
    button.pack()

    frame.mainloop()


def show_more_window(values_to_tree):
    frame = Toplevel(takefocus=True)
    frame.focus()
    frame.title('Show More')

    label = Label(frame, text='More details about picked positions')
    label.pack()

    tree = ttk.Treeview(frame, columns=[1, 2, 3], height=10, show='headings')
    tree.pack(side='left', fill='x')
    tree.heading(1, text='Title')
    tree.heading(2, text='Author')
    tree.heading(3, text='Updated')
    tree.column(1, width=500)
    tree.column(2, width=200)
    tree.column(3, width=300)

    scroll_hor = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
    scroll_hor.pack(side='right', fill='y')

    tree.configure(yscrollcommand=scroll_hor.set)

    for value in values_to_tree:
        tree.insert('', 'end', values=(value[0], value[1], value[2]))

    button = Button(frame, text='Ok', command=frame.destroy)
    button.pack(side='top', padx=10, ipadx=10, pady=60, ipady=10)

    frame.mainloop()
