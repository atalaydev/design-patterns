import abc
from typing import Dict


class Letter(abc.ABC):
    @property
    @abc.abstractmethod
    def dimensions(self) -> str:
        ...


class A3(Letter):
    @property
    def dimensions(self) -> str:
        return "297 x 420mm"


class A4(Letter):
    @property
    def dimensions(self) -> str:
        return "210 x 297mm"


class A5(Letter):
    @property
    def dimensions(self) -> str:
        return "148 x 210mm"


class LetterFactory(abc.ABC):
    @abc.abstractmethod
    def create_letter(self):
        ...


class A3Factory(LetterFactory):
    def __init__(self):
        self.letter = None

    def create_letter(self):
        self.letter = A3()
        print(self.letter.dimensions)


class A4Factory(LetterFactory):
    def __init__(self):
        self.letter = None

    def create_letter(self):
        self.letter = A4()
        print(self.letter.dimensions)


class A5Factory(LetterFactory):
    def __init__(self):
        self.letter = None

    def create_letter(self):
        self.letter = A5()
        print(self.letter.dimensions)


if __name__ == "__main__":
    choices: Dict[str, LetterFactory] = {
        "A3": A3Factory(),
        "A4": A4Factory(),
        "A5": A5Factory(),
    }

    letter = (input("Please choose a letter size: [A3/A4/A5]? : ")).upper()
    assert letter in choices, "Unsupported latter provided!"

    choices[letter].create_letter()
