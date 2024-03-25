import random

def choose_food(options):
    chosen_food = random.choice(options)
    print(chosen_food)
    return chosen_food
    
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
    "Bún đậu",
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
    "Miến trộn"
]

chosen_food = choose_food(food_options)


