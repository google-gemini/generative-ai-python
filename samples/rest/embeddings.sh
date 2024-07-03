set -eu

echo "[START embed]"
# [START embed]
curl "https://generativelanguage.googleapis.com/v1beta/models/text-embedding-004:embedContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"model": "models/text-embedding-004",
    "content": {
    "parts":[{
      "text": "Hello world"}]}, }' 2> /dev/null | head
# [END embed]

echo "[START batch_embed]"
# [START batch_embed]
curl "https://generativelanguage.googleapis.com/v1beta/models/text-embedding-004:batchEmbedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"requests": [{
      "model": "models/text-embedding-004",
      "content": {
      "parts":[{
        "text": "What is the meaning of life?"}]}, },
      {
      "model": "models/text-embedding-004",
      "content": {
      "parts":[{
        "text": "How much wood would a woodchuck chuck?"}]}, },
      {
      "model": "models/text-embedding-004",
      "content": {
      "parts":[{
        "text": "How does the brain work?"}]}, }, ]}' 2> /dev/null | grep -C 5 values
# [END batch_embed]