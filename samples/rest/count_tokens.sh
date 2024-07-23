set -eu 

SCRIPT_DIR=$(dirname "$0")
MEDIA_DIR=$(realpath ${SCRIPT_DIR}/../../third_party)

TEXT_PATH=${MEDIA_DIR}/poem.txt
IMG_PATH=${MEDIA_DIR}/organ.jpg
AUDIO_PATH=${MEDIA_DIR}/sample.mp3
VIDEO_PATH=${MEDIA_DIR}/Big_Buck_Bunny.mp4

BASE_URL="https://generativelanguage.googleapis.com"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

echo "[START tokens_text_only]"
# [START tokens_text_only]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }],
        }],
      }'
# [END tokens_text_only]

echo "[START tokens_chat]"
# [START tokens_chat]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {"role": "user",
        "parts": [{"text": "Hi, my name is Bob."}],
        },
        {"role": "model",
         "parts":[{"text": "Hi Bob"}],
        },
      ],
      }'
# [END tokens_chat]

echo "[START tokens_multimodal_image_inline]"
# [START tokens_multimodal_image_inline]
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Tell me about this instrument"},
            {
              "inline_data": {
                "mime_type":"image/jpeg",
                "data": "'$(base64 $B64FLAGS $IMG_PATH)'"
              }
            }
        ]
        }]
       }' 2> /dev/null
# [END tokens_multimodal_image_inline]

echo "[START tokens_multimodal_image_file_api]"
# [START tokens_multimodal_image_file_api]
MIME_TYPE=$(file -b --mime-type "${IMG_PATH}")
NUM_BYTES=$(wc -c < "${IMG_PATH}")
DISPLAY_NAME=TEXT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMG_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Can you tell me about the instruments in this photo?"},
          {"file_data":
            {"mime_type": "image/jpeg", 
            "file_uri": '$file_uri'}
          }]
        }]
       }' 
# [END tokens_multimodal_image_file_api]

echo "# [START tokens_multimodal_video_audio_file_api]"
# [START tokens_multimodal_video_audio_file_api]

MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO_PATH

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

state=$(jq ".file.state" file_info.json)
echo state=$state

name=$(jq ".file.name" file_info.json)
echo name=$name

while [[ "($state)" = *"PROCESSING"* ]];
do
  echo "Processing video..."
  sleep 5
  # Get the file of interest to check state
  curl https://generativelanguage.googleapis.com/v1beta/files/$name > file_info.json
  state=$(jq ".file.state" file_info.json)
done

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this video clip"},
          {"file_data":{"mime_type": "video/mp4", "file_uri": '$file_uri'}}]
        }]
       }'
# [END tokens_multimodal_video_audio_file_api]