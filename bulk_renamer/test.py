from typing import Generator
from random import choice
from string import ascii_letters, digits


def file_type_generator() -> Generator[None, None, str]:
    types = ["txt", "png", "jpg", "pdf", "csv", "tsv", "py", "c", "cs", "cpp",
             "java", "mp3", "wav", "ogg", "flac", "mp4", "mkv", "mov"]
    while True:
        yield choice(types)


def file_name_generator(length: int) -> Generator[int, None, str]:
    characters = ascii_letters + digits + "-_"
    while True:
        name = [choice(characters) for _ in range(length)]
        yield "".join(name)


def file_generator(
    name_generator: Generator[None, None, str],
    type_generator: Generator[int, None, str]
) -> Generator[None, None, str]:
    while True:
        yield next(name_generator) + "." + next(type_generator)


def create_files(output_path: str, file_generator: Generator[None, None, str], amount: int) -> bool:
    for _ in range(amount):
        filename = next(file_generator)
        open(filename, "x").close()


if __name__ == "__main__":
    generator = file_generator(file_name_generator(5), file_type_generator())
    create_files("C://Users/Admin/Desktop/randomfiles", generator, 200)
    
    
    
