set -eu

echo "[START text_gen_text_only_prompt]"
# [START text_gen_text_only_prompt]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{"text": "Write a story about a magic backpack."}]
        }]
       }' 2> /dev/null
# [END text_gen_text_only_prompt]

echo "[START text_gen_text_only_prompt_streaming]"
# [START text_gen_text_only_prompt_streaming]

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:streamGenerateContent?alt=sse&key=${GOOGLE_API_KEY}" \
        -H 'Content-Type: application/json' \
        --no-buffer \
        -d '{ "contents":[{"parts":[{"text": "Write a story about a magic backpack."}]}]}'
# [END text_gen_text_only_prompt_streaming]

echo "[START text_gen_multimodal_one_image_prompt]"
# [START text_gen_multimodal_one_image_prompt]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Tell me about this instrument"},
            {"inline_data": "../third_party/organ.jpg}
        ]
        }]
       }' 2> /dev/null
# [END text_gen_multimodal_one_image_prompt]