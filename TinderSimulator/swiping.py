import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

class TinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tinder")
        
        self.df = pd.read_csv("girls_data.csv")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="---Tinder---")
        self.label.pack()
        
        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack()
        
        self.button_yes = tk.Button(self.root, text="Yes", command=self.like)
        self.button_yes.pack(side="left")
        
        self.button_no = tk.Button(self.root, text="No", command=self.dislike)
        self.button_no.pack(side="left")
        
        self.button_stop = tk.Button(self.root, text="Stop", command=self.stop)
        self.button_stop.pack(side="left")
        
        self.display_girl_data()
        
    def print_random_girl_data(self):
        random_index = random.randint(0, len(self.df) - 1)
        girl_info = self.df.iloc[random_index]
        info = f"Name: {girl_info['Name']}\nAge: {girl_info['Age']}\nBio: {girl_info['Tinder Bio']}\nLanguages: {girl_info['Languages']}\nLocation: {girl_info['Location']}\nZodiac: {girl_info['Zodiac']}\nPassions: {girl_info['Passions']}\nLifestyle: {girl_info['Lifestyle']}"
        return info
    
    def display_girl_data(self):
        info = self.print_random_girl_data()
        self.info_label.config(text=info)
        
    def like(self):
        self.display_girl_data()
        
    def dislike(self):
        self.display_girl_data()
        
    def stop(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TinderApp(root)
    root.mainloop()
