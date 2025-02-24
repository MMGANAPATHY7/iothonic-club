def text_to_emoji(text):
    # Dictionary for word-to-emoji conversion
    emoji_dict = {
        "love": "❤️",
        "pizza": "🍕",
        "cat": "🐱",
        "cats": "🐱",
        "dog": "🐶",
        "happy": "😊",
        "sad": "😢",
        "laugh": "😂",
        "cool": "😎",
        "angry": "😡",
        "fire": "🔥",
        "star": "⭐",
        "ok": "👌",
        "yes": "👍",
        "no": "👎",
        "wow": "😲"
    }

    # Split text into words and replace with emojis where possible
    words = text.split()
    converted_text = " ".join([emoji_dict.get(word.lower(), word) for word in words])

    return converted_text


# Example usage
input_text = "I love pizza and cats!"
output_text = text_to_emoji(input_text)
print(output_text)
