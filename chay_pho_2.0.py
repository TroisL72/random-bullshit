import tkinter as tk
import random

def choose_food(options):
    chosen_food = random.choice(options)
    return chosen_food

def display_chosen_food():
    chosen_food_label.config(text=choose_food(food_options))

food_options = [
    "Phở trộn",
    "Phở nước",
    "Bánh mì",
    "Gỏi cuốn",
    "Bún chả",
    "Bún bò Huế",
    "Cơm gà Hải Nam",
    "Bánh xèo",
    "Bánh mì xíu mại",
    "Bánh canh",
    "Bún riêu",
    "Bánh tráng trộn",
    "Bánh tráng cuốn thịt heo",
    "Bánh cuốn",
    "Bánh tráng nướng",
    "Bún mắm",
    "Bánh mì chảo",
    "Hủ tiếu",
    "Cơm tấm",
    "Bánh bèo",
    "Bánh bột lọc",
    "Bánh canh cua",
    "Bún măng vịt",
    "Bún đậu",
    "Chả cá",
    "Bánh tráng phơi sương",
    "Bánh mì trứng",
    "Bánh tráng trộn",
    "Xôi",
    "Gà rán",
    "Bún cá",
    "Mì vằn thắn",
    "Cơm bình dân",
    "Bánh đa",
    "Miến lươn",
    "Miến trộn",
    "Nem nướng",
    "Bân xiển",
    "Bánh mì chảo",
    "Bún trộn",
    "Mì trộn",
    "Tok"
]

root = tk.Tk()
root.title("Hôm nay ăn gì cả nhà ơiiiiii")

chosen_food_label = tk.Label(root, text="Ăn cái gì?", font=("Helvetica", 18))
chosen_food_label.pack(pady=20)

choose_button = tk.Button(root, text="Chọn", command=display_chosen_food)
choose_button.pack(pady=10)

root.mainloop()
