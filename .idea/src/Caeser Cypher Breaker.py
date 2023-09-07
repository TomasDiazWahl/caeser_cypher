from pathlib import Path

def get_user_input(msg: str) -> Path:
    file_name: str = input(msg)
    current_directory = Path.cwd()
    file_path: Path = Path(file_name)
    if not file_path.is_absolute():
        file_path = current_directory / file_path
    return file_path

def parse_line(line: str, english_words: list[str]):
    words: list[str] = line.split()
    brute_force_cypher(words, english_words)

def read_dictionary(file_path: Path) -> list[str]:
    with file_path.open("r") as file:
        lines: list[str] = file.readlines()

    words: list[str] = []
    for line in lines:
        a_line: str = line.lower()
        a_line: str = a_line.strip()
        words.append(a_line)

    return words

def word_in_dict(word: str, english_words: list[str]) -> bool:
    if word not in english_words:
        return False
    else:
        return True

def shift(word) -> str:
    alphabet_length: int = 26
    a_ascii: int = ord('a')
    shifted_word: str = ""
    for i in range(len(word)):
        schar = chr((((ord(word[i]) - a_ascii) + 1) % alphabet_length) + a_ascii)
        shifted_word += schar
    return shifted_word

def brute_force_cypher(sentence: list[str], english_words: list[str]):
    alphabet_length: int = 26
    shift_counter: int = 0
    all_words_correct: bool = False
    word_correct: bool = True
    shifted_word_sentence = sentence.copy()

    while not all_words_correct:
        for word in shifted_word_sentence:
            if not word_in_dict(word, english_words):
                word_correct = False
                break
        if word_correct:
            all_words_correct = True
            print(shifted_word_sentence)
            print(shift_counter)
            break
        else:
            for i, word in enumerate(shifted_word_sentence):
                shifted_word = shift(word)
                shifted_word_sentence[i] = shifted_word
            shift_counter += 1
        if shift_counter >= alphabet_length - 1:
            print("We fucked up")
            break

    print(shifted_word_sentence)
    return shift_counter


def parse_file(file_path: Path, english_words: list[str]):
    with file_path.open("r") as file:
        lines = file.readlines()

    sentences: list[str] = []
    for line in lines:
        a_line: str = line.lower()
        a_line: str = a_line.strip()
        sentences.append(a_line)

    for sentence in sentences:
        parse_line(sentence, english_words)

def main():
    # file_path = get_user_input("Enter dictionary file name or path:")
    file_path = Path("dictionary.dic")
    english_words = read_dictionary(file_path)
    # file_path: Path = get_user_input("Please enter name of text file or full path:")
    file_path = Path("caesar-ciphertext.txt")
    parse_file(file_path, english_words)

# end main


if __name__ == "__main__":
    main()