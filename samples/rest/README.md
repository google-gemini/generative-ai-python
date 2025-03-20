# Gemini API REST sample code

This directory contains sample code for key features of the API, organised by high level feature.

These samples are embedded in parts of the [documentation](https://ai.google.dev), most notably in the [API reference](https://ai.google.dev/api).

Each file is structured as a runnable script, ensuring that samples are executable and functional. Each filee contains region tags that are used to demarcate the script from the spotlight code. If you are contributing, code within region tags should follow sample code best practices - being clear, complete and concise.

## Parameter Naming Conventions

The Gemini API accepts REST parameters in camelCase format, which is the convention used in these examples and the official API reference. For example:
- `generationConfig`
- `maxOutputTokens`
- `systemInstruction`
- `topP`, `topK`

**Note:** While the API also accepts snake_case format for compatibility (e.g., `system_instruction` instead of `systemInstruction`), the official and recommended style is camelCase for REST API requests.

## Contents

| File | Description |
| ---- | ----------- |
| [cache.sh](./cache.sh) | Context caching |
| [chat.sh](./chat.sh) | Multi-turn chat conversations |
| [code_execution.sh](./code_execution.sh) | Executing code |
| [configure_model_parameters.sh](./configure_model_parameters.sh) | Setting model parameters |
| [controlled_generation.sh](./controlled_generation.sh) | Generating content with output constraints (e.g. JSON mode) |
| [count_tokens.sh](./count_tokens.sh) | Counting input and output tokens |
| [embed.sh](./embed.sh) | Generating embeddings |
| [files.sh](./files.sh) | Managing files with the File API |
| [function_calling.sh](./function_calling.sh) | Using function calling |
| [inline_pdf_example.sh](./inline_pdf_example.sh) | Using inline PDF data with the API |
| [models.sh](./models.sh) | Listing models and model metadata |
| [safety_settings.sh](./safety_settings.sh) | Setting and using safety controls |
| [system_instruction.sh](./system_instruction.sh) | Setting system instructions |
| [text_generation.sh](./text_generation.sh) | Generating text |
| [tuned_models.sh](./tuned_models.sh) | Tuned models |
