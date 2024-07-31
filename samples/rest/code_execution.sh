set -eu 

echo "[START code_execution_basic]"
# [START code_execution_basic]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {
    "tools": [{"code_execution": {}}],
    "contents": {
        "parts": {
            "text": "What is the sum of the first 50 prime numbers? Generate
                     and run code for the calculation, and make sure you get all 50."
        }
    }
}'
# [END code_execution_basic]
