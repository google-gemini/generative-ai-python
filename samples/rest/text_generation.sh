set -eu

echo "[START text_gen_text_only_prompt]"
# [START text_gen_text_only_prompt]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?alt=sse&key=${GOOGLE_API_KEY}" \
        -H 'Content-Type: application/json' \
        --no-buffer \
        -d '{ "contents":[{"parts":[{"text": "Write a story about a magic backpack."}]}]}'
# [END text_gen_text_only_prompt_streaming]

echo "[START text_gen_multimodal_one_image_prompt]"
# [START text_gen_multimodal_one_image_prompt]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Tell me about this instrument"},
            {"inline_data": "../../third_party/organ.jpg"}
        ]
        }]
       }' 2> /dev/null
# [END text_gen_multimodal_one_image_prompt]

echo "[START text_gen_multimodal_one_image_prompt_streaming]"
# [START text_gen_multimodal_one_image_prompt_streaming]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Tell me about this instrument"},
            {"inline_data": "../../third_party/organ.jpg"}
        ]
        }]
       }' 2> /dev/null
# [END text_gen_multimodal_one_image_prompt_streaming]

echo "[START text_gen_multimodal_audio]"
# [START text_gen_multimodal_audio]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Give me a summary of this audio file."},
            {"inline_data": "../../third_party/sample.mp3"}
        ]
        }]
       }' 2> /dev/null
# [END text_gen_multimodal_audio]

echo "[START text_gen_multimodal_video_prompt]"
# [START text_gen_multimodal_video_prompt]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Describe this video clip."},
            {"inline_data": "../../third_party/Big_Buck_Bunny.mp4"}
        ]
        }]
       }' 2> /dev/null
# [END text_gen_multimodal_video_prompt]

echo "[START text_gen_multimodal_video_prompt_streaming]"
# [START text_gen_multimodal_video_prompt_streaming]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?key=$GOOGLE_API_KEY" \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Describe this video clip."},
            {"inline_data": "../../third_party/Big_Buck_Bunny.mp4"}
        ]
        }]
       }' 2> /dev/null
# [END text_gen_multimodal_video_prompt_streaming]