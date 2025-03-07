set -eu

echo "[START configure_model_parameters]"
# [START configure_model_parameters]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
        "contents": [{
            "parts":[
                {"text": "Explain how AI works"}
            ]
        }],
        "generationConfig": {
            "stopSequences": [
                "Title"
            ],
            "temperature": 1.0,
            "maxOutputTokens": 800,
            "topP": 0.8,
            "topK": 10
        }
    }'  2> /dev/null | grep "text"
# [END configure_model_parameters]
