import random

def choose_food(options):
    chosen_food = random.choice(options)
    print(chosen_food)
    return chosen_food

food_options = [
    "phở chè",
    "trà sữa",
    "kem",
    "2land",
    "bánh bột lọc",
    "bánh",
    "kem xôi",
    "bánh trôi nước",
    "bánh đúc",
    "trà dâu",
    "bánh chuối",
    "bò bía",
    "bánh tráng",
    "donut",
    "gà bó xôi",
    "xiên bẩn",
    "trà đường",
    "sữa chua trân châu hạ long",
    "sữa tươi trân châu đường đen",
    "bánh gà",
    "quẩy",
    "nem chua",
    "nem nướng",
    "bánh rán",
    "hotdog"
]
chosen_food = choose_food(food_options)