def analyze_text(text: str):
    stripped_text = text.strip()

    if not stripped_text:
        print("Notice: No input provided. Please enter a valid sentence.")
        return

    # Splitting with no arguments cleanly handles multiple consecutive spaces
    words = stripped_text.split()
    word_count = len(words)
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    print(f"Word count: {word_count}")
    print(f"Total characters (including spaces): {char_count}")
    print(f"Total characters (excluding spaces): {char_count_no_spaces}")

def main():
    user_input = input("Enter a sentence: ")
    analyze_text(user_input)

if __name__ == "__main__":
    main()