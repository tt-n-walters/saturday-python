from typing import Generator
from timer_decorator import timer_decorator
from pylev3 import Levenshtein

from random import choice


def random_sentence_gen() -> Generator[None, None, str]:
    sentences = open("sentences.txt", "r", encoding="utf-8").read().splitlines()
    while True:
        yield choice(sentences)


@timer_decorator
def get_user_sentence() -> str:
    return input("Type here: ")


def calculate_accuracy(goal: str, user: str) -> float:
    num_of_edits = Levenshtein.wfi(goal, user)
    return (len(goal) - num_of_edits) / len(goal)


def calculate_speed(user: str, time_taken: float) -> float:
    return len(user) / (time_taken / 60)


def display_results(accuracy: float, speed: float) -> None:
    print(f"You had an accuracy of {round(accuracy * 100, 1)}% and a speed of {round(speed, 2)}lpm.")


if __name__ == "__main__":
    import os
    print(os.path.abspath(__file__))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    sentence_generator = random_sentence_gen()

    while True:
        sentence = next(sentence_generator)
        print(sentence)
        user_input, time_taken = get_user_sentence()
        accuracy = calculate_accuracy(sentence, user_input)
        speed = calculate_speed(user_input, time_taken)

        display_results(accuracy, speed)
