def handle_edge_cases(decision_text: str):
    if not decision_text or len(decision_text.strip()) < 20:
        return None, "Decision is too short. Please provide more details."

    emotional_words = [
        "stressed", "confused", "sad", "afraid",
        "angry", "depressed", "worried"
    ]

    cleaned_text = decision_text
    for word in emotional_words:
        cleaned_text = cleaned_text.replace(word, "")

    return cleaned_text.strip(), None
