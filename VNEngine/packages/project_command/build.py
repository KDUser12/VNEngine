import customtkinter


def build_project(self):
    label_font = customtkinter.CTkFont(family="Arial", size=15)
    label = customtkinter.CTkLabel(self, width=400, height=50, text="Creation of the current project", font=label_font)
    label.grid(pady=175)

    progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal")
    progressbar.grid()

    progressbar.set(0)

    progressbar.set(1)
