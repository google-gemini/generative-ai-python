set -eu

echo "[START cache_create]"
# [START cache_create]
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-1.5-flash-001",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 -w0 a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d @request.json

rm a11.txt request.json
# [END cache_create]

echo "[START cache_list]"
# [START cache_list]
ALL_CACHES=$(curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GOOGLE_API_KEY")
CACHE_NAME=$(echo "$ALL_CACHES" | grep '"name":' | cut -d '"' -f 4 | head -n 1)
# [END cache_list]

echo "[START cache_get]"
# [START cache_get]
curl "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GOOGLE_API_KEY"
# [END cache_get]

echo "[START cache_update]"
# [START cache_update]
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GOOGLE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{"ttl": "600s"}'
# [END cache_update]

echo "[START cache_generate_content]"
# [START cache_generate_content]
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-001:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
# [END cache_generate_content]

echo "[START cache_delete]"
# [START cache_delete]
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GOOGLE_API_KEY"
# [END cache_delete]