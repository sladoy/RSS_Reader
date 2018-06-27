from tkinter import Tk, Entry, Label, Button
from Reader import RSS


class MainGUI:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.label = Label(root, text='Wprowadz link RSS')
        self.label.pack()
        self.entry = Entry(root)
        self.entry.pack()
        self.start_button = Button(root, text='Start', command=self.start)
        self.start_button.pack()
        self.show_more_button = Button(root, text='Show more about')
        self.show_more_button.pack()
        self.data_label = Label(root)
        self.data_label.pack()
        self.url = 0

    def start(self):
        self.url = RSS(self.entry.get())
        positions = self.url.show_titles()
        print(self.url)

        for x, y in positions.items():
            print(x + '\t link: ' + y)


if __name__ == '__main__':
    root = Tk()
    root.bind('<Escape>', quit)
    root.title('RSS Reader')
    root.geometry('400x200')
    MainGUI(root)
    root.mainloop()
