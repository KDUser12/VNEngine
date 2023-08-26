import customtkinter

from .build import build_project


def button_click_event(self):
    dialog_name = customtkinter.CTkInputDialog(text="Enter the name of your project:", title="New Project",
                                               button_hover_color=("#bdbdbd", "#363636"),
                                               button_fg_color=("#cfcfcf", "#2e2e2e"),
                                               button_text_color=("#737373", "#c4c4c4"),
                                               entry_fg_color=("#c4c4c4", "#303030"),
                                               entry_border_color=("#c4c4c4", "#303030"))

    project_name = dialog_name.get_input()
    min_char = 2
    max_char = 18
    project_name_char = int(len(project_name))

    if min_char > project_name_char > max_char:
        return -201
    else:
        self.title_label.grid_forget()
        self.project_frame.grid_forget()
        self.project_label.grid_forget()
        self.add_button.grid_forget()

        build_project(self)
