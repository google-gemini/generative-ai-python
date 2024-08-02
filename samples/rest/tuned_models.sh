set -eu

export access_token=$(gcloud auth application-default print-access-token)
export project_id=<your project id>

access_token=$(gcloud auth application-default print-access-token)


echo "[START tuned_models_create]"
# [START tuned_models_create]
curl -X POST https://generativelanguage.googleapis.com/v1beta/tunedModels \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" \
    -d '
      {
        "display_name": "number generator model",
        "base_model": "models/gemini-1.0-pro-001",
        "tuning_task": {
          "hyperparameters": {
            "batch_size": 2,
            "learning_rate": 0.001,
            "epoch_count":5,
          },
          "training_data": {
            "examples": {
              "examples": [
                {
                    "text_input": "1",
                    "output": "2",
                },{
                    "text_input": "3",
                    "output": "4",
                },{
                    "text_input": "-3",
                    "output": "-2",
                },{
                    "text_input": "twenty two",
                    "output": "twenty three",
                },{
                    "text_input": "two hundred",
                    "output": "two hundred one",
                },{
                    "text_input": "ninety nine",
                    "output": "one hundred",
                },{
                    "text_input": "8",
                    "output": "9",
                },{
                    "text_input": "-98",
                    "output": "-97",
                },{
                    "text_input": "1,000",
                    "output": "1,001",
                },{
                    "text_input": "10,100,000",
                    "output": "10,100,001",
                },{
                    "text_input": "thirteen",
                    "output": "fourteen",
                },{
                    "text_input": "eighty",
                    "output": "eighty one",
                },{
                    "text_input": "one",
                    "output": "two",
                },{
                    "text_input": "three",
                    "output": "four",
                },{
                    "text_input": "seven",
                    "output": "eight",
                }
              ]
            }
          }
        }
      }' | tee tunemodel.json

# Check the operation for status updates during training.
# Note: you can only check the operation on v1/
operation=$(cat tunemodel.json | jq ".name" | tr -d '"')
curl -X GET  https://generativelanguage.googleapis.com/v1/${operation} \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}"

# Or get the TunedModel and check it's state. The model is ready to use if the state is active.
modelname=$(cat tunemodel.json | jq ".metadata.tunedModel" | tr -d '"')
curl -X GET  https://generativelanguage.googleapis.com/v1beta/${modelname} \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | tee check.json

cat check.json | jq ".state"
# [END tuned_models_create]

echo "[START tuned_models_generate_content]"
# [START tuned_models_generate_content]
curl -X POST https://generativelanguage.googleapis.com/v1beta/$modelname:generateContent \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" \
    -d '{
        "contents": [{
        "parts": [{
          "text": "LXIII"
          }]
        }]
        }' 2> /dev/null
# [END tuned_models_generate_content]

echo "[START tuned_models_get]"
# [START tuned_models_get]
curl -X GET https://generativelanguage.googleapis.com/v1beta/${modelname} \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep state
# [END tuned_models_get]

echo "[START tuned_models_list]"
# [START tuned_models_list]
curl -X GET https://generativelanguage.googleapis.com/v1beta/tunedModels \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}"
# [END tuned_models_list]

