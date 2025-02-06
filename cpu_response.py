from customtkinter import *

title_font = ("Helvetica", 18, "bold")
small_font = ("Helvetica", 11)
small_font_color = ["#2B2B2B", "#E5E5E5"]
basic_font = ("Helvetica", 16)

class DisplayFrame(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = CTkLabel(self, text="Welcome to Adventure Text Game!", font=title_font, text_color="white").grid(row=0, column=0, padx=20, pady=10, sticky="w")

    def update(self, text):
        self.user_test = CTkLabel(app.display_frame, text=self.inputBox.get(0, -1), font=title_font, text_color="white").grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
class InputFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.suggest_text = CTkLabel(self, text='Suggested text: ', font=small_font, fg_color=small_font_color[0], text_color=small_font_color[1]).pack(side="top")
        self.inputBox = CTkTextbox(self, width=460, height=52, font=basic_font, border_width=2, border_color="#404040", fg_color=small_font_color[0], text_color=small_font_color[1], corner_radius=10).pack(side="left", padx=10, pady=10, fill=X, expand=True)
        self.send_Button = CTkButton(self, text="Send", width=50, height=50, font=basic_font, fg_color="#4CAF50", hover_color="#45A049", corner_radius=10).pack(side="left", padx=10, pady=10)

    def send_input(self):
        app.display_frame.update(self.inputBox.value)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Adventure Text Game")
        self.geometry("600x600")
        self.configure(fg_color="#1B1B1B")
        self.display_frame = DisplayFrame(master=self, fg_color="#2A2A2A", corner_radius=10, height=360).pack(side="top", fill=BOTH, padx=20, pady=20)
        self.input_frame = InputFrame(master=self).pack(side="bottom", fill=X)

if __name__ == "__main__":
    app = App()
    app.mainloop()