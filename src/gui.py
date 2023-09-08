from tkinter import *

# Initial settings window (3x2)
def run_startup_prompt() -> list:
    window = Tk()
    window.title("App Setup")
    window.iconbitmap(r"H:\Code\Github\Basketball-Stat-Tracking-Aid\basketball_icon.ico")
    radiobutton_option = StringVar()
    checkbutton_state = BooleanVar()
    
    radio_container = Frame(window)
    radio_gui = Radiobutton(
        master = radio_container,
        text = "Graphical User Interface",
        variable = radiobutton_option,
        value = "gui"
    )
    radio_cmd = Radiobutton(
        master = radio_container,
        text = "Command Line Interface",
        variable = radiobutton_option,
        value = "cmd"
    )
    radio_description = Label(
        master = window,
        text = "Whether to run\nthe application in command\nline or graphical interface mode"
    )
    
    checkbutton_integrity = Checkbutton(
        master = window,
        text = "Check Saved Data Integrity",
        variable = checkbutton_state,
        onvalue = True,
        offvalue = False
    )
    checkbutton_description = Label(
        master = window,
        text = "Whether to verify\nthe file integrity of\nthe saved data (only makes \nlight checks to save time)"
    )
    
    button_continue = Button(
        master = window,
        text="Continue",
        command=window.destroy
    )
    
    radio_gui.select()
    radio_gui.pack()
    radio_cmd.pack()
    radio_container.grid(row=1, column=1)
    radio_description.grid(row=1, column=2)
    checkbutton_integrity.grid(row=2, column=1)
    checkbutton_description.grid(row=2, column=2)
    button_continue.grid(row=3, column=1)

    window.mainloop()
    
    return [radiobutton_option.get(), checkbutton_state.get()]

print(run_startup_prompt())
