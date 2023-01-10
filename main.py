import gettext
import info

import tkinter as tk

from re import compile, match
from math import tan, pi
from locale import getlocale


class Line:

    def __init__(self, x=0.0, z=0.0, angle=0.0):
        self.k_coeff = (-1) * tan(angle * (pi / 180))
        self.b_coeff = (-1) * (self.k_coeff * z - x)


class App:
    
    pattern = compile("^-?\d+(\.\d+)?$")
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.root.title(_("Stronghold Finder by MirrorAzure"))
        icon = tk.PhotoImage(file='icon.png')
        self.root.iconphoto(False, icon)
        
        self.root.configure(bg="#52504f")
        self.root.resizable(False, False)
        
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.main_menu.add_command(label=_("Info"), command=info.show_info_window)
        
        self.create_widgets()
        self.place_widgets()
        
    
    @staticmethod
    def is_valid(entry_field: tk.Entry) -> bool:
        return match(App.pattern, entry_field.get())
        
    
    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#52504f")
        
        # first coordinate
        
        self.first_coordinate_frame = tk.Frame(self.main_frame, bg="#52504f")
        
        self.first_coordinate_name_label = tk.Label(self.first_coordinate_frame,
                                                    text=_("First throw"),
                                                    fg="#dfdfdf",
                                                    bg="#52504f",
                                                    font=('Arial', 14, "bold"))
        self.first_entry_field_frame = tk.Frame(self.first_coordinate_frame, bg="#52504f")
        
        
        self.first_x_label = tk.Label(self.first_entry_field_frame,
                                      text="X:",
                                      fg="#dfdfdf",
                                      bg="#52504f",
                                      font=('Arial', 14))
                                      
        self.first_x_entry = tk.Entry(self.first_entry_field_frame,
                                      fg="#dfdfdf",
                                      bg="#52504f",
                                      font=('Arial', 14),
                                      width=9)
        
        
        self.first_z_label = tk.Label(self.first_entry_field_frame,
                                      text="Z:",
                                      fg="#dfdfdf",
                                      bg="#52504f",
                                      font=('Arial', 14))
                                      
        self.first_z_entry = tk.Entry(self.first_entry_field_frame,
                                      fg="#dfdfdf",
                                      bg="#52504f",
                                      font=('Arial', 14),
                                      width=9)
        
        
        self.first_angle_label = tk.Label(self.first_entry_field_frame,
                                          text=_("Angle:"),
                                          fg="#dfdfdf",
                                          bg="#52504f",
                                          font=('Arial', 14))
                                          
        self.first_angle_entry = tk.Entry(self.first_entry_field_frame,
                                          fg="#dfdfdf",
                                          bg="#52504f",
                                          font=('Arial', 14),
                                          width=6)
        
        # second coordinate
        
        self.second_coordinate_frame = tk.Frame(self.main_frame, bg="#52504f")
        
        self.second_coordinate_name_label = tk.Label(self.second_coordinate_frame,
                                                     text=_("Second throw"),
                                                     fg="#dfdfdf",
                                                     bg="#52504f",
                                                     font=('Arial', 14, "bold"))
        self.second_entry_field_frame = tk.Frame(self.second_coordinate_frame, bg="#52504f")
        
        
        self.second_x_label = tk.Label(self.second_entry_field_frame,
                                      text="X:",
                                      fg="#dfdfdf",
                                      bg="#52504f",
                                      font=('Arial', 14))
        self.second_x_entry = tk.Entry(self.second_entry_field_frame,
                                       fg="#dfdfdf",
                                       bg="#52504f",
                                       font=('Arial', 14),
                                       width=9)
        
        
        self.second_z_label = tk.Label(self.second_entry_field_frame,
                                      text="Z:",
                                      fg="#dfdfdf",
                                      bg="#52504f",
                                      font=('Arial', 14))
        self.second_z_entry = tk.Entry(self.second_entry_field_frame,
                                       fg="#dfdfdf",
                                       bg="#52504f",
                                       font=('Arial', 14),
                                       width=9)
        
        
        self.second_angle_label = tk.Label(self.second_entry_field_frame,
                                          text=_("Angle:"),
                                          fg="#dfdfdf",
                                          bg="#52504f",
                                          font=('Arial', 14))
        self.second_angle_entry = tk.Entry(self.second_entry_field_frame,
                                           fg="#dfdfdf",
                                           bg="#52504f",
                                           font=('Arial', 14),
                                           width=6)
        
        
        
        self.show_result_frame = tk.Frame(self.main_frame, bg="#52504f")
        self.calculate_button = tk.Button(self.show_result_frame,
                                          text=_("Calculate"),
                                          fg="#dfdfdf",
                                          bg="#52504f",
                                          font=('Arial', 16, "bold"),
                                          command=self.display_answer)
        self.show_result_label = tk.Label(self.show_result_frame,
                                          text="",
                                          fg="#dfdfdf",
                                          bg="#52504f",
                                          font=('Arial', 16, "bold"))
        
    
    def place_widgets(self):
        self.main_frame.pack(anchor="w", padx=10, pady=10)
        
        self.first_coordinate_frame.pack(anchor="w")
        self.first_coordinate_name_label.pack(anchor="w")
        
        self.first_entry_field_frame.pack(anchor="w")
        
        self.first_x_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.first_x_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.first_z_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.first_z_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.first_angle_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.first_angle_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        
        
        self.second_coordinate_frame.pack(anchor="w")
        self.second_coordinate_name_label.pack(anchor="w")
        
        self.second_entry_field_frame.pack(anchor="w")
        
        self.second_x_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.second_x_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.second_z_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.second_z_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.second_angle_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.second_angle_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        
        
        self.show_result_frame.pack(anchor="w")
        self.calculate_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.show_result_label.pack(side=tk.LEFT, padx=10, pady=10)
        
    def display_answer(self):
        entries_list = [self.first_x_entry,
                       self.first_z_entry,
                       self.first_angle_entry,
                       self.second_x_entry,
                       self.second_z_entry,
                       self.second_angle_entry]
        if all(map(self.is_valid, entries_list)):
            first_line = Line(float(self.first_x_entry.get()),
                              float(self.first_z_entry.get()),
                              float(self.first_angle_entry.get()))
            second_line = Line(float(self.second_x_entry.get()),
                              float(self.second_z_entry.get()),
                              float(self.second_angle_entry.get()))
            if first_line.k_coeff == second_line.k_coeff:
                msg = _("Lines are parallel.\nPlease enter another point.")
            else:
                res = calculate_intersection_point(first_line, second_line)
                msg = _("Estimated stronghold location:\n") + f"X: {res[0]:.2f}   Z: {res[1]:.2f}"
        else:
            msg = _("Error occurred.\nPlease fill all forms correctly.")
        self.show_result_label["text"] = msg
    

    

def calculate_intersection_point(first_line: Line, second_line: Line) -> tuple:
    z_coord = (second_line.b_coeff - first_line.b_coeff) / (first_line.k_coeff - second_line.k_coeff)
    x_coord = first_line.k_coeff * z_coord + first_line.b_coeff
    return (x_coord, z_coord)

def main():
    
    if getlocale()[0] == "Russian_Russia":
        lang = "ru"
    else:
        lang = "en"

    t = gettext.translation('main', localedir='locale', languages=[lang])
    t.install()
    _ = t.gettext
    app = App()
    app.root.mainloop()
    
if __name__ == "__main__":
    main()

