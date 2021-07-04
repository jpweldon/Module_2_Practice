
# Build CLI

import fire
import random

def clothes_picker(pants=False):
    shirts_list = ["solid blue", "red striped","purple and green tie dye", "black dress shirt"]

    pants_list = ["Black dress pants", "Gray sweatpants", "Khakis"]

    if pants:
        return random.choice(shirts_list), random.choice(pants_list)

    return random.choice(shirts_list)

if __name__ == '__main__':
    fire.Fire(clothes_picker)
