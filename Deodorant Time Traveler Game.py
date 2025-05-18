import tkinter as tk
from tkinter import messagebox
import random

history_points = [
    {"year": "Ancient Egypt (3500 BC)", "fact": "In ancient Egypt, body odor was considered a significant social problem, especially in the hot desert climate. To address this, Egyptians developed some of the earliest forms of deodorant, relying on natural methods. They used aromatic herbs, myrrh, frankincense, and other fragrant oils to mask body odor. They also placed scented cones of fat on their heads that would melt and release pleasant scents as they moved about, helping them stay fresh even in the intense heat.", "question": "What did ancient Egyptians use to reduce body odor?", "options": ["Natural oils and spices", "Perfume", "Soap", "Vinegar"], "answer": "Natural oils and spices"},
    {"year": "1888", "fact": "In 1888, the first commercial deodorant was created and trademarked in the United States under the brand name 'Mum.' It was a waxy cream applied by hand, primarily marketed to women. This innovation marked a turning point in personal hygiene, as it was the first time a product specifically designed to reduce body odor was made available to the public. However, it had its drawbacks, including being somewhat messy and inconvenient to apply, which limited its early popularity.", "question": "What was the first commercial deodorant called?", "options": ["Everfresh", "Mum", "Cool Breeze", "Fresh Start"], "answer": "Mum"},
    {"year": "1903", "fact": "Just a few decades after Mum's invention, the first antiperspirant, Everdry, hit the market in 1903. Unlike deodorants, which simply mask odors, antiperspirants actively prevent sweat by using compounds like aluminum chloride to temporarily block sweat glands. This marked a significant leap forward, as it addressed not just the smell but the root cause of body odor — perspiration itself. However, the early versions were known to cause skin irritation due to the strong chemicals used.", "question": "What chemical was used in the first antiperspirant?", "options": ["Sodium chloride", "Aluminum chloride", "Potassium sulfate", "Magnesium oxide"], "answer": "Aluminum chloride"},
    {"year": "1960s", "fact": "The 1960s brought a wave of innovation with the introduction of aerosol spray deodorants. These products were not only more convenient but also more effective at delivering a fine mist of deodorizing agents. This era also marked the rise of aggressive marketing campaigns, emphasizing personal freshness and confidence. However, these sprays faced backlash in later decades due to their use of chlorofluorocarbons (CFCs), which were found to damage the ozone layer, leading to a shift back to roll-ons and sticks.", "question": "Which decade saw the rise of aerosol deodorants?", "options": ["1950s", "1960s", "1970s", "1980s"], "answer": "1960s"},
    {"year": "2020s", "fact": "In recent years, consumers have become more health and environmentally conscious, leading to a surge in natural and sustainable deodorant options. Modern products focus on using ingredients like baking soda, coconut oil, and essential oils, avoiding harsh chemicals like aluminum and parabens. Many brands also prioritize eco-friendly packaging, reflecting a broader cultural shift towards sustainability.", "question": "What is a major focus for modern deodorants?", "options": ["Longevity", "Natural ingredients", "Stronger scents", "Cheaper production"], "answer": "Natural ingredients"}
]

class DeodorantTimeTraveler(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Deodorant Time Traveler")
        self.geometry("500x750")
        self.index = 0
        self.score = 0
        self.total_questions = len(history_points)
        
        self.title_label = tk.Label(self, text="🕰️ Deodorant Time Traveler", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)
        
        self.score_label = tk.Label(self, text=f"Score: {self.score} / {self.total_questions}", font=("Arial", 14))
        self.score_label.pack(pady=5)
        
        self.year_label = tk.Label(self, font=("Arial", 16, "bold"))
        self.year_label.pack(pady=10)
        
        self.fact_label = tk.Label(self, wraplength=450, font=("Arial", 12))
        self.fact_label.pack(pady=10)
        
        self.question_label = tk.Label(self, font=("Arial", 14, "italic"), wraplength=450)
        self.question_label.pack(pady=10)
        
        self.options_frame = tk.Frame(self)
        self.options_frame.pack(pady=10)
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.options_frame, font=("Arial", 12), width=40, command=lambda i=i: self.check_answer(i))
            btn.grid(row=i, column=0, pady=5)
            self.option_buttons.append(btn)
        
        self.update_content()
        
    def update_content(self):
        current = history_points[self.index]
        self.year_label.config(text=current["year"])
        self.fact_label.config(text=current["fact"])
        self.question_label.config(text=current["question"])
        self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")
        options = current["options"][:]
        random.shuffle(options)
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=options[i])
        
    def check_answer(self, choice_index):
        current = history_points[self.index]
        selected = self.option_buttons[choice_index].cget("text")
        if selected == current["answer"]:
            messagebox.showinfo("Correct!", "🎉 Great job! That's the right answer.")
            self.score += 1
        else:
            messagebox.showwarning("Incorrect", f"❌ Oops! The correct answer was '{current['answer']}'.")
        
        self.index = (self.index + 1) % len(history_points)
        self.update_content()
        
    def reset_game(self):
        self.index = 0
        self.score = 0
        self.update_content()

if __name__ == "__main__":
    app = DeodorantTimeTraveler()
    app.mainloop()
