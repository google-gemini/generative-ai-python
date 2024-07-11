set -eu

echo "[START caching]"
# [START caching]
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
# [END caching]

echo "[START list_caches]"
# [START list_caches]
ALL_CACHES=$(curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GOOGLE_API_KEY")
CACHE_NAME=$(echo "$ALL_CACHES" | grep '"name":' | cut -d '"' -f 4 | head -n 1)
# [END list_caches]

echo "[START get_cache]"
# [START get_cache]
curl "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GOOGLE_API_KEY"
# [END get_cache]

echo "[START update_cache]"
# [START update_cache]
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GOOGLE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{"ttl": "600s"}'
# [END update_cache]

echo "[START use_cache]"
# [START use_cache]
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
# [END use_cache]

echo "[START delete_cache]"
# [START delete_cache]
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GOOGLE_API_KEY"
# [END delete_cache]