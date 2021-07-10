import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for c, n in kwargs.items():
            for x in range(n):
                self.contents.append(c)

    def draw(self, number):
        removed = []
        if number > len(self.contents):
            removed = self.contents
        else:
            for x in range(number):
                random_position = random.randrange(len(self.contents))
                removed.append(self.contents[random_position])
                self.contents.pop(random_position)
        return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    fails = 0
    contents_baseline = copy.copy(hat.contents)

    for n in range(0, num_experiments):
        removed_balls = hat.draw(num_balls_drawn)
        for e in expected_balls.keys():
            count = 0
            for r in range(0, len(removed_balls)):
                if removed_balls[r] == e:
                    count += 1
            if count < expected_balls.get(e):
                fails += 1
                break
        hat.contents = copy.copy(contents_baseline)
    probability = 1 - fails / num_experiments
    return probability
