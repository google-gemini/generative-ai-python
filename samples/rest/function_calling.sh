set -eu

echo "[START function_calling]"
# [START function_calling]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=$GOOGLE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d @<(echo '
  {
    "system_instruction": {
      "parts": {
        "text": "You are a helpful lighting system bot. You can turn lights on and off, and you can set the color. Do not perform any other tasks."
      }
    },
    "tools": [' $(cat tools.json) '],

    "tool_config": {
      "function_calling_config": {"mode": "none"}
    },

    "contents": {
      "role": "user",
      "parts": {
        "text": "What can you do?"
      }
    }
  }
') 2>/dev/null |sed -n '/"content"/,/"finishReason"/p'
# [END function_calling]