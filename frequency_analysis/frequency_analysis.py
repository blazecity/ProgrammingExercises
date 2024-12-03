def count_letters(text) -> dict[str, int]:
    letter_distribution = {}

    for character in text:
        if not character.isalpha():
            continue

        lower_char = character.lower()
        new_letter_count = letter_distribution.get(lower_char, 0) + 1
        letter_distribution[lower_char] = new_letter_count

    return letter_distribution


if __name__ == "__main__":

    example_text = """Frequency analysis is based on the fact that, in any given stretch of written language, certain letters and
combinations of letters occur with varying frequencies. Moreover, there is a characteristic distribution
of letters that is roughly the same for almost all samples of that language. For instance, given a section
of English language, E, T, A and O are the most common, while Z, Q, X and J are rare. Likewise,
TH, ER, ON, and AN are the most common pairs of letters (termed bigrams or digraphs), and SS,
EE, TT, and FF are the most common repeats. The nonsense phrase ”ETAOIN SHRDLU” represents
the 12 most frequent letters in typical English language text. In some ciphers, such properties of the
natural language plaintext are preserved in the ciphertext, and these patterns have the potential to be
exploited in a ciphertext-only attack."""

    result = count_letters(example_text)
    print(result)