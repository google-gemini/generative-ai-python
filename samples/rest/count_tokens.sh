set -eu 

echo "[START tokens_text_only]"
# [START tokens_text_only]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{
          "text": "Write a story about a magic backpack."}]}]}' > response.json
# [END tokens_text_only]

echo "[START tokens_chat]"
# [START tokens_chat]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {"role":"user",
         "parts":[{
           "text": "Hi, my name is Bob."}]},
        {"role": "model",
         "parts":[{
           "text": "Hi Bob"}]},
      ] ' 2> response.json
# [END tokens_chat]