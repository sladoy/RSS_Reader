import webbrowser
from tkinter import Tk, Entry, Label, Button, ttk, TclError
from Reader import RSS
from windows import error_window, show_more_window, start_error_window

'''
RSS: https://www.reddit.com/r/python/.rss
'''


class MainGUI:
    '''Creating main window'''
    def __init__(self, root):
        self.root = root

        self.label = Label(root, text='Wprowadz link RSS')
        self.label.pack()

        self.entry = Entry(root)
        self.entry.pack()

        self.start_button = Button(root, text='Start', command=self.start)
        self.start_button.pack(side='top')

        self.open_in_browser_button = Button(root, text='Open', command=self.open_in_browser)
        self.open_in_browser_button.pack(side='top')

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

    def show_more(self):
        '''Function will put values from selected positions intro tree from show_more_window'''
        picked_values = []
        values_to_tree = []

        all_values = RSS(self.entry.get())
        all_values = all_values.show_more_details()

        try:
            if len(all_values) == 0:
                error_window()
        except TclError:
            return
        else:
            picked_id_values = self.get_selection_values()

            for values in picked_id_values:
                picked_values.append(self.tree.item(values)['values'][0])

            for x in all_values:
                if x[0] in picked_values:
                    values_to_tree.append([x[0], x[1], x[2]])

            show_more_window(values_to_tree)

    def start(self):
        '''Reading values from RSS link and putting them to a tree'''
        self.url = RSS(self.entry.get())
        positions = self.url.show_title_and_link()
        try:
            if len(positions) == 0:
                start_error_window()
        except TclError:
            return
        else:
            for x, y in positions.items():
                self.value_list.append([x, y])

            for value in self.value_list:
                self.tree.insert('', 'end', values=(value[0], value[1]))

    def open_in_browser(self):
        '''Opening selected positions in web browser'''
        table = []
        values = self.get_selection_values()
        try:
            if len(values) == 0:
                error_window()
        except NameError:
            return
        else:
            for value in values:
                table.append(self.tree.item(value)['values'][1])

            for element in table:
                webbrowser.open_new_tab(element)

    def get_selection_values(self):
        values = self.tree.selection()
        return values


if __name__ == '__main__':
    root = Tk()
    root.title('RSS Reader')
    MainGUI(root)
    root.mainloop()
