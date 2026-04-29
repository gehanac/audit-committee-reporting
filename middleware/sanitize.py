# middleware/sanitize.py

import re
from flask import request, jsonify

# Basic HTML tag removal
def strip_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Detect prompt injection patterns
def detect_prompt_injection(text):
    patterns = [
        r"ignore previous instructions",
        r"disregard rules",
        r"system prompt",
        r"act as",
        r"bypass",
        r"jailbreak"
    ]

    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

# Middleware function
def sanitize_input():
    if request.method == "POST":
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid input"}), 400

        user_input = data.get("message", "")

        # Strip HTML
        cleaned_input = strip_html(user_input)

        # Detect prompt injection
        if detect_prompt_injection(cleaned_input):
            return jsonify({
                "error": "Prompt injection detected. Request blocked."
            }), 400

        # Replace original input with cleaned input
        data["message"] = cleaned_input