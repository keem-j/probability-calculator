import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()

        for name, value in kwargs.items():
            for i in range(value): self.contents.append(name)
    

    def draw(self, n):
        balls_drawn = list()

        if n < len(self.contents):
            balls_drawn = random.sample(self.contents, n)
            for item in balls_drawn: self.contents.remove(item)
        else:
            balls_drawn = copy.copy(self.contents)
            self.contents.clear()

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    expected_balls_list = list()
    for name, value in expected_balls.items():
        for i in range(value): expected_balls_list.append(name)
    expected_balls_count = Counter(expected_balls_list)
    
    num_occurrences = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_drawn_count = Counter(balls_drawn)

        for element, count in expected_balls_count.items():
            if balls_drawn_count.get(element, 0) < count:
                break
        else:
            num_occurrences += 1
    
    probability = num_occurrences / num_experiments

    return probability
