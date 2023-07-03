import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for ball, amount in kwargs.items():
            self.contents.extend([ball] * amount)

    def draw(self, amount):
        if amount >= len(self.contents):
            balls = copy.copy(self.contents)
            self.contents = []
            return balls

        # random.shuffle(self.contents)
        balls = random.sample(self.contents, amount)
        for ball in balls:
            self.contents.remove(ball)
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    contents = copy.copy(hat.contents)

    expected_balls_contents = []
    for ball, amount in expected_balls.items():
        expected_balls_contents.extend([ball] * amount)

    M = 0
    for _ in range(num_experiments):
        hat.contents = copy.copy(contents)
        balls = hat.draw(num_balls_drawn)
        for ball in expected_balls_contents:
            if ball in balls:
                balls.remove(ball)
            else:
                M += 1
                break

    return (num_experiments - M) / num_experiments
