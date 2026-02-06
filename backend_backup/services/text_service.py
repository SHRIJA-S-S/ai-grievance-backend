def handle_text(text: str):
    text_lower = text.lower()

    if any(word in text_lower for word in ["fight", "violence", "abuse", "attack"]):
        return {
            "category": "disciplinary",
            "priority": "High",
            "action": "Route to Discipline Committee"
        }

    if any(word in text_lower for word in ["tap", "water", "leak"]):
        return {
            "category": "water",
            "priority": "Medium",
            "action": "Route to Maintenance"
        }

    if any(word in text_lower for word in ["projector", "fan", "light", "bench"]):
        return {
            "category": "infrastructure",
            "priority": "Medium",
            "action": "Route to Infrastructure Team"
        }

    return {
        "category": "general",
        "priority": "Medium",
        "action": "Route to Admin"
    }
