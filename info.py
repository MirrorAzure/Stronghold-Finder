import gettext
import tkinter as tk

from locale import getlocale

def show_info_window():
    
    if getlocale()[0] == "Russian_Russia":
        lang = "ru"
    else:
        lang = "en"
    
    ti = gettext.translation('main', localedir='locale', languages=[lang])
    ti.install()
    _i = ti.gettext
    
    text1 = _i('''Welcome to \"Stronghold Finder\"!

This is a simple offline program that will help you find a stronghold in Minecraft.

The search for a stronghold is based on the triangulation method. Thanks to it, you will spend much less time and resources than when using the classic method.''')

    text2 = _i('''How to use the program:

1. Enter the game and take your eyes of ender;

2. Take a position with a good view;

3. Use eye of ender and point your cursor on flying eye (it\'s better to aim to the center);

4. Without moving your character or camera, press F3,
write X and Z coordinates, and also your horizontal rotation (first number in \"Facing\" row) in coresponding fields of the program;

5. Take another position (preferably at a distance of 400-500 blocks from the first) and do steps 2-4 again;

6. Press the \"Calculate\" button.

7. All done! You\\'re awesome!''')


    text3 = _i('''If you made everything right, the program should display estimated coordinates of stronghold.
Because of the error, actual coordinates of stronghold may differ by 100-200 blocks.
However, even with an error, finding stronghold wiil be much easier.

I made this program at the request of my friend. Hello, Zavergan, if you\'re reading this.
I took on the project to get some practice in building the user interface and internationalizing the app.

Good luck to you and all the best!''')
    
    
    root = tk.Tk()
    root.title(_i("Info"))
    
    root.configure(bg="#52504f")
    #root.resizable(False, False)
    
    main_frame = tk.Frame(root, bg="#52504f")
    
    first_text_frame = tk.Frame(main_frame, bg="#52504f")
    
    second_text_frame = tk.Frame(main_frame, bg="#52504f")
    
    third_text_frame = tk.Frame(main_frame, bg="#52504f")
    
    main_frame.pack()
    
    first_text_frame.pack()
    second_text_frame.pack()
    third_text_frame.pack()
    
    tk.Label(first_text_frame, text=text1, bg="#52504f", fg="#dfdfdf", font=('Arial', 11), justify="center").pack(anchor="w", pady=10)
    tk.Label(second_text_frame, text=text2, bg="#52504f", fg="#dfdfdf", font=('Arial', 14), justify="left").pack(anchor="w", pady=20)
    tk.Label(third_text_frame, text=text3, bg="#52504f", fg="#dfdfdf", font=('Arial', 11), justify="center").pack(anchor="w", pady=10)
    
    root.mainloop()


def main():
    show_info_window()

if __name__ == "__main__":
    main()