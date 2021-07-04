
# Build CLI

import fire
import random

def clothes_picker():
    shirts_list = ["solid blue", "red striped","purple and green tie dye", "black dress shirt"]

    return random.choice(shirts_list)

if __name__ == '__main__':
    fire.Fire(clothes_picker)
