def reverse_words_preserve_spaces(text):
    # Split while keeping the spaces
    parts = text.split(" ")
    print(parts)
    # Reverse each non-empty part
    reversed_parts = [part[::-1] for part in parts]
    # Join back with spaces
    return " ".join(reversed_parts)

# Example usage
input_str = "one two  three     four"
output_str = reverse_words_preserve_spaces(input_str)
print(output_str)  # Output: "eno owt  eerht  ruof"
