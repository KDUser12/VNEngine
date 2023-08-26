import customtkinter


# Function to define the color theme based on the appearance mode
def define_color_theme():
    # Get the current appearance mode from customtkinter
    appearance_mode = customtkinter.get_appearance_mode()

    # Check the appearance mode and set the color theme accordingly
    if appearance_mode == "Light":
        customtkinter.set_default_color_theme("blue")
    elif appearance_mode == "dark":
        customtkinter.set_default_color_theme("dark-blue")
    else:
        return -101

    return 0
