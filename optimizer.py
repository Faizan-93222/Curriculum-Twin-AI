# optimizer.py

def optimize_curriculum(curriculum, friction_points):
    optimized = []

    for topic in curriculum:
        if topic["name"] in friction_points:
            optimized.append({
                "name": topic["name"] + " (Optimized)",
                "duration": topic["duration"] // 2,
                "difficulty": "medium",
                "format": "video"
            })
        else:
            optimized.append(topic)

    return optimized
