import webbrowser
from tkinter import Tk, Entry, Label, Button, ttk
from show_more_window import ShowMore
from Reader import RSS

'''
Wiecej informacji o danej pozycji, kiedy byla ostatnio aktualizowana, etc

RSS: https://www.reddit.com/r/python/.rss
'''


class MainGUI:
    def __init__(self, root):
        self.root = root

        self.label = Label(root, text='Wprowadz link RSS')
        self.label.pack()

        self.entry = Entry(root)
        self.entry.pack()

        self.start_button = Button(root, text='Start', command=self.start)
        self.start_button.pack()

        self.open_in_browser_button = Button(root, text='Open', command=self.open_in_browser)
        self.open_in_browser_button.pack()

        self.show_more_button = Button(root, text='Show more', command=self.show_more)
        self.show_more_button.pack()

        self.tree = ttk.Treeview(self.root, columns=[1, 2], height=10, show='headings')
        self.tree.pack(side='left', fill='x')
        self.tree.heading(1, text='Title')
        self.tree.heading(2, text='Link')
        self.tree.column(1, width=500)
        self.tree.column(2, width=500)

        self.scroll_hor = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.scroll_hor.pack(side='right', fill='y')

        self.tree.configure(yscrollcommand=self.scroll_hor.set)
        self.url = 0
        self.value_list = []

    @staticmethod
    def error_window():
        frame = Tk()
        frame.bind('<Escape>', frame.destroy)
        label = Label(frame, text="You didn't selected a position from the list")
        label.pack()
        button = Button(frame, text='Ok', command=frame.destroy)
        button.pack()

        frame.mainloop()

    def show_more(self):
        pass
    def start(self):

        self.url = RSS(self.entry.get())
        positions = self.url.show_title_and_link()
        for x, y in positions.items():
            self.value_list.append([x, y])

        for value in self.value_list:
            self.tree.insert('', 'end', values=(value[0], value[1]))

    def open_in_browser(self):
        table = []

        values = self.tree.selection()
        for value in values:
            table.append(self.tree.item(value)['values'][1])

        for element in table:
            webbrowser.open_new_tab(element)


if __name__ == '__main__':
    root = Tk()
    root.bind('<Escape>', quit)
    root.title('RSS Reader')
    MainGUI(root)
    root.mainloop()
