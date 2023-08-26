"""
VNEngine is a game engine specially for Visual Novel in python

===== Instruction =====

- set_appearance_mode : system
- set_default_color_theme : blue / dark-blue

- title : VNEngine
- geometry : 400x500
- resizable : False, False

- file format : .vpy

========= END =========
"""

import customtkinter

from packages.color_theme import define_color_theme
from packages.project_command import button_click_event


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")
        define_color_theme()

        self.title("VNEngine")
        self.geometry("400x500")
        self.resizable(False, False)

        # Section-1 ####################################################################################################

        self.title_font = customtkinter.CTkFont(family="Arial", size=25, weight="bold")
        self.title_label = customtkinter.CTkLabel(self, text="VNEngine", height=50, width=400, font=self.title_font,
                                                  text_color=("#5c5b5b", "#dbdbdb"))
        self.title_label.grid(column=0, row=0)

        # Section-2 ####################################################################################################

        self.project_frame = customtkinter.CTkFrame(self, height=1, width=375, fg_color=("#858585", "#a6a6a6"),
                                                    border_width=1, border_color=("#858585", "#a6a6a6"))
        self.project_frame.grid(column=0, row=1)

        self.project_font = customtkinter.CTkFont(family="Arial", size=13, weight="normal")
        self.project_label = customtkinter.CTkLabel(self, text="Projects", height=35, width=50, font=self.project_font,
                                                    text_color=("#858585", "#a6a6a6"))
        self.project_label.grid(column=0, row=1)

        # Section-3 ####################################################################################################

        self.add_font = customtkinter.CTkFont(family="Arial", size=15, weight="normal")
        self.add_button = customtkinter.CTkButton(self, height=25, width=350, fg_color=("#cfcfcf", "#2e2e2e"),
                                                  text="+", border_width=0, text_color=("#858585", "#a6a6a6"),
                                                  font=self.add_font, hover_color=("#bdbdbd", "#363636"),
                                                  command=self.click_event)
        self.add_button.grid(column=0, row=98)

    def click_event(self):
        button_click_event(self)


if __name__ == "__main__":
    root = Window()
    root.mainloop()
