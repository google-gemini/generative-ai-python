set -eu

echo "[START models_list]"
# [START models_list]
curl https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY
# [END models_list]

echo "[START models_get]"
# [START models_get]
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash?key=$GEMINI_API_KEY
# [END models_get]
