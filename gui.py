import tkinter as tk

# TODO: reorder parameters in alphabetical order and split long lines
# TODO: add dynamic font resizing based on window resize
# may be issue with empty frames being wrong size compared to the set weights
# adjust sizes of elements and how they resize, and padding (maybe change sticky vs set size) (once all elements done)
# maybe add a default font + settings
# maybe make default element classes so attributes aren't repeated for each creation


class RemoteGUI(tk.Tk):

    # window config:
    TITLE = "Remote Vehicle Control"
    DEFAULT_GEOMETRY = "1200x800"
    MIN_SIZE = (800, 500)
    LIGHT_BACKGROUND = "#E8E8E8"
    MID_BACKGROUND = "#D4D4D4"
    DARK_BACKGROUND = "#BEBEBE"

    def __init__(self) -> None:
        super().__init__()
        self.setupWindow()
        self.createElements()
        self.setupLayout()

    def setupWindow(self):
        self.title(self.TITLE)
        self.geometry(self.DEFAULT_GEOMETRY)
        self.minsize(*self.MIN_SIZE)   # * for argument unpacking minsize tuple
        self.configure(bg=self.DARK_BACKGROUND)

    def createElements(self):
        self.mainFrame = tk.Frame(self, bg=self.DARK_BACKGROUND)  # for outer padding

        self.stopButton = tk.Button(self.mainFrame, bg="#ff0000", activebackground="#d00000", text='STOP', font=("Arial", 30, "bold"), bd=5)

        self.leftFrame = tk.Frame(self.mainFrame, bg=self.LIGHT_BACKGROUND, relief='solid', bd=2)
        self.rightFrame = tk.Frame(self.mainFrame, bg=self.LIGHT_BACKGROUND, relief='solid', bd=2)

        # torque controls in left frame:
        self.leftFrameLabel = tk.Label(self.leftFrame, text="Control Panel", font=("Arial", 30, "bold"), bg=self.LIGHT_BACKGROUND)
        self.stepLabel = tk.Label(self.leftFrame, text="Step:", font=("Arial", 18, "bold"), bg=self.LIGHT_BACKGROUND, anchor='s')
        self.stepEntry = tk.Entry(self.leftFrame, bg="#FFFFFF", justify="center", font=("Arial", 20))
        self.stepUpButton = tk.Button(self.leftFrame, text="step up", font=("Arial", 18), bg=self.DARK_BACKGROUND, activebackground=self.MID_BACKGROUND)
        self.TorqueEntry = tk.Entry(self.leftFrame, bg="#FFFFFF", justify="center", font=("Arial", 20))
        self.stepDownButton = tk.Button(self.leftFrame, text="step down", font=("Arial", 18), bg=self.DARK_BACKGROUND, activebackground=self.MID_BACKGROUND)
        self.sendButton = tk.Button(self.leftFrame, text="send", font=("Arial", 20, "bold"), bg=self.DARK_BACKGROUND, activebackground=self.MID_BACKGROUND)

        # dyno info in right frame:
        self.rightFrameLabel = tk.Label(self.rightFrame, text="Monitor Panel", font=("Arial", 30, "bold"), bg=self.LIGHT_BACKGROUND)
        self.dynoTorque = tk.Entry(self.rightFrame, bg="#FFFFFF", justify="center", font=("Arial", 20))

    def setupLayout(self):
        OUTER_PADDING = 10
        INNER_PADDING = 3

        self.mainFrame.pack(padx=OUTER_PADDING, pady=OUTER_PADDING, fill='both', expand=True)

        # main grid configure
        self.mainFrame.columnconfigure((0, 1), weight=1)
        self.mainFrame.rowconfigure(0, weight=8)  # change for stop button height
        self.mainFrame.rowconfigure(1, weight=1)

        # placing elements in main grid
        self.stopButton.grid(row=1, column=0, columnspan=2, sticky='nesw', padx=INNER_PADDING, pady=INNER_PADDING)  # can add dynamic padding using more grid rows/colums around, with weights

        self.leftFrame.grid(row=0, column=0, sticky='nesw', padx=INNER_PADDING, pady=INNER_PADDING)
        self.rightFrame.grid(row=0, column=1, sticky='nesw', padx=INNER_PADDING, pady=INNER_PADDING)

        # left grid configure
        self.leftFrame.columnconfigure((0, 1, 2), weight=1)
        self.leftFrame.rowconfigure(0, weight=1)   # adjust weight for label vs buttons height:
        self.leftFrame.rowconfigure((1, 5), weight=2)
        self.leftFrame.rowconfigure((2, 4), weight=1)
        self.leftFrame.rowconfigure(3, weight=2)

        # place elements in left frame grid
        self.leftFrameLabel.grid(column=0, columnspan=3, row=0, rowspan=2)
        self.stepLabel.grid(row=2, column=0, sticky='nesw')
        self.stepEntry.grid(row=3, column=0, sticky='nesw')
        self.stepUpButton.grid(row=2, column=1, sticky='nesw')
        self.TorqueEntry.grid(row=3, column=1, sticky='nesw')
        self.stepDownButton.grid(row=4, column=1, sticky='nesw')
        self.sendButton.grid(row=3, column=2, sticky='nesw')

        # temporary rightFrame design:
        self.rightFrameLabel.pack()
        self.dynoTorque.pack()
