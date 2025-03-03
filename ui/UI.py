import tkinter
from ctypes import windll

class UI:
    def __init__(self, service):
        self.service = service
        self.default_font = "TkDefaultFont"
        self.fontsize = 14

    def run(self):
        root = tkinter.Tk()
        windll.shcore.SetProcessDpiAwareness(1)  # better look on windows
        query_string = tkinter.StringVar()

        result_label = tkinter.Label(root, text="", font=(self.default_font, self.fontsize))

        def submit_callback():
            query = query_string.get()
            self.submit_query(query, result_label)

        # Add widgets here
        root.geometry("480x400")
        root.title("ConvexHullClassificationModel")
        desc_label = tkinter.Label(root, text="\n\n      Enter a point to check if it's in the data convex hull",
                                   font=(self.default_font, self.fontsize))
        desc_label2 = tkinter.Label(root, text="        Separate coordonates with a space\n\n\n",
                                    font=(self.default_font, self.fontsize))
        desc_label.grid(row=0)
        desc_label2.grid(row=1)

        submit_button = tkinter.Button(root, text="Submit", command=submit_callback, font=(self.default_font, self.fontsize))
        submit_button.grid(row=6)

        query_widget = tkinter.Entry(root, textvariable=query_string, font=(self.default_font, self.fontsize))
        query_widget.grid(row=4)

        label_space = tkinter.Label(root, text="\n")
        label_space.grid(row=5)

        result_label.grid(row=7)

        # No more adding widgets beyond this point
        root.mainloop()

    def submit_query(self, query_submitted, result_label):
        try:
            if self.service.run_query(query_submitted):
                result_label.config(text="\n\nPoint is INSIDE data convex hull")
            else:
                result_label.config(text="\n\nPoint is OUTSIDE data convex hull")
        except ValueError as e:
            result_label.config(text="\n\nInvalid input. Coordonates must be integers\nand the point dimension must\n"
                                     "coincide with points in data sample")