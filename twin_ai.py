# twin_ai.py

def create_learning_dna(attention_span, content_pref, difficulty_level):
    return {
        "attention_span": attention_span,
        "content_pref": content_pref,
        "difficulty_level": difficulty_level
    }


def predict_friction_points(dna, curriculum):
    friction = []

    for topic in curriculum:
        score = 0

        # Attention span logic
        if dna["attention_span"] == "short" and topic["duration"] > 30:
            score += 2

        # Difficulty tolerance
        if dna["difficulty_level"] == "low" and topic["difficulty"] == "hard":
            score += 2

        # Content mismatch
        if dna["content_pref"] != topic["format"]:
            score += 1

        if score >= 3:
            friction.append(topic["name"])

    return friction
