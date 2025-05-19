import tkinter as tk
from tkinter import messagebox
import random

history_points = [
    {"year": "Ancient Egypt (3500 BC)", "fact": "In ancient Egypt, body odor was considered a significant social problem, especially in the hot desert climate. To address this, Egyptians developed some of the earliest forms of deodorant, relying on natural methods. They used aromatic herbs, myrrh, frankincense, and other fragrant oils to mask body odor. They also placed scented cones of fat on their heads that would melt and release pleasant scents as they moved about, helping them stay fresh even in the intense heat.", "question": "What did ancient Egyptians use to reduce body odor?", "options": ["Natural oils and spices", "Perfume", "Soap", "Vinegar"], "answer": "Natural oils and spices"},
    {"year": "1888", "fact": "In 1888, the first commercial deodorant was created and trademarked in the United States under the brand name 'Mum.' It was a waxy cream applied by hand, primarily marketed to women. This innovation marked a turning point in personal hygiene, as it was the first time a product specifically designed to reduce body odor was made available to the public.", "question": "What was the first commercial deodorant called?", "options": ["Everfresh", "Mum", "Cool Breeze", "Fresh Start"], "answer": "Mum"},
    {"year": "1903", "fact": "The first antiperspirant, Everdry, hit the market in 1903. Unlike deodorants, which simply mask odors, antiperspirants actively prevent sweat by using compounds like aluminum chloride to temporarily block sweat glands. This marked a significant leap forward as it addressed the root cause of body odor — perspiration itself.", "question": "What chemical was used in the first antiperspirant?", "options": ["Sodium chloride", "Aluminum chloride", "Potassium sulfate", "Magnesium oxide"], "answer": "Aluminum chloride"},
    {"year": "1960s", "fact": "The 1960s brought a wave of innovation with the introduction of aerosol spray deodorants. These products were not only more convenient but also more effective at delivering a fine mist of deodorizing agents. However, they faced backlash due to their use of CFCs, which were later found to damage the ozone layer, leading to a shift back to roll-ons and sticks.", "question": "Which decade saw the rise of aerosol deodorants?", "options": ["1950s", "1960s", "1970s", "1980s"], "answer": "1960s"},
    {"year": "2020s", "fact": "In recent years, consumers have become more health and environmentally conscious, leading to a surge in natural and sustainable deodorant options. Modern products focus on using ingredients like baking soda, coconut oil, and essential oils, avoiding harsh chemicals like aluminum and parabens.", "question": "What is a major focus for modern deodorants?", "options": ["Longevity", "Natural ingredients", "Stronger scents", "Cheaper production"], "answer": "Natural ingredients"}
]

class DeodorantTimeTraveler(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🕰️ Deodorant Time Traveler")
        self.geometry("500x750")
        self.index = 0
        self.score = 0
        self.total_questions = len(history_points)
        self.configure(bg="#e6f7ff")

        self.canvas = tk.Canvas(self, width=500, height=750, bg="#e6f7ff", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.waves = []
        for i in range(5):
            y = 700 - i*30
            wave = self.canvas.create_oval(-200 + i*100, y, 200 + i*100, y+40, fill="#00bfff", outline="")
            self.waves.append(wave)

        self.create_start_screen()
        self.animate_waves()

    def animate_waves(self):
        for i, wave in enumerate(self.waves):
            self.canvas.move(wave, 2 + i, 0)
            pos = self.canvas.coords(wave)
            if pos[0] > 600:
                self.canvas.move(wave, -800, 0)
        self.after(50, self.animate_waves)

    def create_start_screen(self):
        self.clear_screen()
        self.title_label = tk.Label(self.canvas, text="🕰️ Deodorant Time Traveler", font=("Arial", 28, "bold"), bg="#e6f7ff", fg="#0077b6")
        self.start_button = tk.Button(self.canvas, text="Start Quiz", font=("Arial", 18, "bold"), width=20, bg="#00bfff", fg="white", activebackground="#0077b6", activeforeground="white", command=self.start_quiz)
        self.title_label.place(relx=0.5, rely=0.25, anchor="center")
        self.start_button.place(relx=0.5, rely=0.5, anchor="center")

    def start_quiz(self):
        self.index = 0
        self.score = 0
        self.clear_screen()
        self.update_content()

    def update_content(self):
        if self.index == self.total_questions:
            self.show_final_score()
            return

        current = history_points[self.index]
        self.clear_screen()

        self.year_label = tk.Label(self.canvas, text=current["year"], font=("Arial", 20, "bold"), bg="#e6f7ff", fg="#0077b6")
        self.fact_label = tk.Label(self.canvas, text=current["fact"], wraplength=450, font=("Arial", 14), bg="#e6f7ff", fg="#333333")
        self.question_label = tk.Label(self.canvas, text=current["question"], font=("Arial", 16, "italic"), wraplength=450, bg="#e6f7ff", fg="#555555")

        self.year_label.place(relx=0.5, rely=0.05, anchor="n")
        self.fact_label.place(relx=0.5, rely=0.2, anchor="n")
        self.question_label.place(relx=0.5, rely=0.4, anchor="n")

        self.options_frame = tk.Frame(self.canvas, bg="#e6f7ff")
        self.options_frame.place(relx=0.5, rely=0.5, anchor="n")

        options = current["options"][:]
        random.shuffle(options)
        for option in options:
            btn = tk.Button(self.options_frame, text=option, font=("Arial", 14), width=40, bg="#00bfff", fg="white", activebackground="#0077b6", activeforeground="white", command=lambda opt=option: self.check_answer(opt))
            btn.pack(pady=5)

    def show_final_score(self):
        self.clear_screen()
        final_message = f"🎯 Quiz Complete! You scored {self.score} out of {self.total_questions}!"
        self.final_label = tk.Label(self.canvas, text=final_message, font=("Arial", 20, "bold"), bg="#e6f7ff", fg="#0077b6")
        self.final_label.place(relx=0.5, rely=0.4, anchor="center")

        restart_button = tk.Button(self.canvas, text="Restart Quiz", font=("Arial", 16, "bold"), width=20, bg="#00bfff", fg="white", activebackground="#0077b6", activeforeground="white", command=self.start_quiz)
        restart_button.place(relx=0.5, rely=0.6, anchor="center")

    def clear_screen(self):
        for widget in self.canvas.winfo_children():
            widget.destroy()
        self.canvas.delete("all")
        for i, wave in enumerate(self.waves):
            self.waves[i] = self.canvas.create_oval(-200 + i*100, 700 - i*30, 200 + i*100, 740 - i*30, fill="#00bfff", outline="")

    def check_answer(self, selected):
        current = history_points[self.index]
        if selected == current["answer"]:
            messagebox.showinfo("Correct!", "🎉 Great job! That's the right answer.")
                        self.score += 1
        else:
            messagebox.showwarning("Incorrect", f"❌ Oops! The correct answer was '{current['answer']}'.")
                    self.index += 1
        self.update_content()

if __name__ == "__main__":
    app = DeodorantTimeTraveler()
    app.mainloop()
