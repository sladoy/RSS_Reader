from tkinter import Tk, Entry, Label, Button, StringVar
from Reader import RSS


class MainGUI:
    def __init__(self, root):
        self.root = root
        self.V = StringVar()
        self.label = Label(root, text='Wprowadz link RSS')
        self.label.pack()
        self.entry = Entry(root)
        self.entry.pack()
        self.start_button = Button(root, text='Start', command=self.start)
        self.start_button.pack()
        self.show_more_button = Button(root, text='Show more about')
        self.show_more_button.pack()
        self.data_label = Label(root, textvariable=self.V)
        self.data_label.pack()
        self.url = 0

    def start(self):
        #Uzyć Tree View do wpisywania wartosci
        value_list = ''' '''
        self.url = RSS(self.entry.get())
        positions = self.url.show_titles()

        for x, y in positions.items():
            value_list += x + '\t link: ' + y + '\n'

        self.V.set(value_list)


if __name__ == '__main__':
    root = Tk()
    root.bind('<Escape>', quit)
    root.title('RSS Reader')
    MainGUI(root)
    root.mainloop()
