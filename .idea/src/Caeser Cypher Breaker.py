from pathlib import Path

def get_user_input(msg: str) -> Path:
    file_name: str = input(msg)
    file_path: Path = Path(file_name)
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

def word_in_dict(word: str, english_words: list[str]):
    pass

def brute_force_cypher(words: list[str], english_words: list[str]):
    a_ascii: int = ord('a')
    alphabet_length: int = 26
    for i in range(alphabet_length):
        success: bool = True
        for word in words:
            shifted_word: str = ""
            for j in range(len(word)):
                schar = (((word[j] - a_ascii) + i) % alphabet_length) + a_ascii
                shifted_word += schar
                if shifted_word not in english_words:
                    break
         pass



def parse_file(file_path: Path, english_words: list[str]):
    with file_path.open("r") as file:
        lines = file.readlines()

    sentences: list[str] = []
    for line in lines:
        a_line: str = line.lower()
        a_line: str = a_line.strip()
        sentences.append(a_line)

    parse_line(sentences, english_words)

def main():
    file_path = get_user_input("Enter dictionary file name or path:")
    english_words = read_dictionary()
    file_path: Path = get_user_input("Please enter name of text file or full path:")
    parse_file(file_path, english_words)

# end main


if __name__ == "__main__":
    main()