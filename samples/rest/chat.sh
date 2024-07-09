set -eu

IMG_PATH=$(realpath ~/generative-ai-python/third_party/organ.jpg)

echo "[START chat]"
# [START chat]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {"role":"user",
         "parts":[{
           "text": "Hello"}]},
        {"role": "model",
         "parts":[{
           "text": "Great to meet you. What would you like to know?"}]},
      ]
    }' 2> /dev/null | grep "text"
# [END chat]

echo "[START chat_streaming]"
# [START chat_streaming]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {"role":"user",
         "parts":[{
           "text": "Hello"}]},
        {"role": "model",
         "parts":[{
           "text": "Great to meet you. What would you like to know?"}]},
      ]
    }' 2> /dev/null | grep "text"
# [END chat_streaming]

echo "[START chat_streaming_with_images]"
# [START chat_streaming_with_images]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {"role":"user",
         "parts":[{
           "text": "Hello"}]},
        {"role": "model",
         "parts":[
            {"text": "Tell me about this instrument"},
            {
              "inline_data": {
                "mime_type":"image/jpeg",
                "data": "'$(base64 -w0 $IMG_PATH)'"
              }
            }
          }
        ]
      ]
    }' 2> /dev/null | grep "text"
# [END chat_streaming_with_images]