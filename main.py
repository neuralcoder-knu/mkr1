import re


def count(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = re.split(r'[ ,:;]+', text)
    num_words = len(words)

    sentences = re.split(r'[.!?]+', text)
    num_sentences = len(sentences)

    return num_words, num_sentences


def main():
    filepath = input("Введіть шлях до файлу: ")

    try:
        num_words, num_sentences = count(filepath)

        with open("result.txt", "w") as result_file:
            result_file.write(f"Кількість слів: {num_words}\n")
            result_file.write(f"Кількість речень: {num_sentences}\n")

        print("Результати були записані в файл 'result.txt'")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


if __name__ == "__main__":
    main()