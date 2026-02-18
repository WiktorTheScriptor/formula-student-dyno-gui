import tkinter as tk

# TODO: reorder parameters in alphabetical order and split long lines


class RemoteGUI(tk.Tk):

    # window config:
    TITLE = "Remote Vehicle Control"
    DEFAULT_GEOMETRY = "1200x800"
    MIN_SIZE = (800, 500)

    def __init__(self) -> None:
        super().__init__()
        self.setupWindow()
        self.createElements()
        self.setupLayout()

    def setupWindow(self):
        self.title(self.TITLE)
        self.geometry(self.DEFAULT_GEOMETRY)
        self.minsize(*self.MIN_SIZE)

    def createElements(self):
        self.mainFrame = tk.Frame(self)  # for outer padding

        self.stopButton = tk.Button(self.mainFrame, bg="#ff0000", activebackground="#d00000", text='STOP', bd=5)

        self.leftFrame = tk.Frame(self.mainFrame, bg="#E8E8E8", relief='solid', bd=2)
        self.rightFrame = tk.Frame(self.mainFrame, bg="#E8E8E8", relief='solid', bd=2)

    def setupLayout(self):
        OUTER_PADDING = 10
        INNER_PADDING = 3

        self.mainFrame.pack(padx=OUTER_PADDING, pady=OUTER_PADDING, fill='both', expand=True)

        # grid configure
        self.mainFrame.columnconfigure((0, 1), weight=1)
        self.mainFrame.rowconfigure(0, weight=8)  # change for stop button height
        self.mainFrame.rowconfigure(1, weight=1)

        # placing elements in grid
        self.stopButton.grid(row=1, column=0, columnspan=2, sticky='nesw', padx=INNER_PADDING, pady=INNER_PADDING)  # can add dynamic padding using more grid rows/colums around, with weights

        self.leftFrame.grid(row=0, column=0, sticky='nesw', padx=INNER_PADDING, pady=INNER_PADDING)
        self.rightFrame.grid(row=0, column=1, sticky='nesw', padx=INNER_PADDING, pady=INNER_PADDING)
