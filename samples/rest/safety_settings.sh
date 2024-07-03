set -eu

echo "[START safety_settings]"
# [START safety_settings]
echo '{
    "safetySettings": [
        {'category': 7, 'threshold': 3}
    ],
    "contents": [{
        "parts":[{
            "text": "'I support Martians Soccer Club and I think Jupiterians Football Club sucks! Write a ironic phrase about them.'"}]}]}' > request.json
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GOOGLE_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d @request.json  2> /dev/null > response.json

    jq .promptFeedback < response.json
# [END safety_settings]

echo "[START safety_settings_multi]"
# [START safety_settings_multi]
echo '{
    "safetySettings": [
        {'category': 7, 'threshold': 3},
        {'category': 8, 'threshold': 2}
    ],
    "contents": [{
        "parts":[{
            "text": "'I support Martians Soccer Club and I think Jupiterians Football Club sucks! Write a ironic phrase about them.'"}]}]}' > request.json

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GOOGLE_API_KEY" \
        -H 'Content-Type: application/json' \
        -X POST \
        -d @request.json  2> /dev/null > response.json

    jq .promptFeedback < response.json
# [END safety_settings_multi]
