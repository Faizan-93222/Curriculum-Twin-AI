YOUTUBE_RESOURCES = {
    "introduction to ai": [
        "https://www.youtube.com/watch?v=ad79nYk2keg"
    ],
    "ai applications": [
        "https://www.youtube.com/watch?v=2ePf9rue1Ao"
    ],
    "machine learning": [
        "https://www.youtube.com/watch?v=ukzFI9rgwfU"
    ],
    "neural networks": [
        "https://www.youtube.com/watch?v=aircAruvnKk"
    ],
    "deep learning": [
        "https://www.youtube.com/watch?v=6M5VXKLf4D4"
    ],
    "ai ethics": [   # ✅ ADD THIS
        "https://www.youtube.com/watch?v=8QnMmpfKWvo",
        "https://www.youtube.com/watch?v=H2J9p4sQkP4"
    ]
}

def copilot_assist(feedback, optimized_curriculum):
    text = feedback.lower()
    updated = []
    actions = []
    links = {}

    wants_links = any(word in text for word in ["youtube", "video", "link", "watch", "resource"])

    # ---------- UPDATE OPTIMIZED CURRICULUM ----------
    for topic in optimized_curriculum:
        new = topic.copy()
        name = new["name"].lower()

        # Optimization rules
        if "hard" in text:
            new["difficulty"] = "medium"
            actions.append(f"Reduced difficulty for {new['name']}")

        if "long" in text:
            new["duration"] = max(10, new["duration"] // 2)
            actions.append(f"Shortened {new['name']}")

        if "confusing" in text:
            new["format"] = "video"
            actions.append(f"Changed {new['name']} to video format")

        updated.append(new)

    # ---------- PROVIDE VIDEOS ONLY FOR OPTIMIZED TOPICS ----------
    if wants_links:
        for topic in updated:
            # ONLY if this topic is optimized (format is video)
            if topic["format"] == "video":
                topic_name = topic["name"].lower()

                for key, urls in YOUTUBE_RESOURCES.items():
                    if key in topic_name:
                        links[topic["name"]] = urls

    # ---------- RESPONSE ----------
    explanation = ""
    if actions:
        explanation += "I updated your optimized curriculum:\n- " + "\n- ".join(set(actions))

    if links:
        explanation += "\n\n📺 Video resources for optimized topics:\n"
        for topic, urls in links.items():
            explanation += f"\n{topic}:\n"
            for u in urls:
                explanation += f"  - {u}\n"

    if not explanation:
        explanation = (
            "I work only on the optimized curriculum.\n"
            "Try: 'make topics confusing' or 'show video links'"
        )

    return updated, explanation
