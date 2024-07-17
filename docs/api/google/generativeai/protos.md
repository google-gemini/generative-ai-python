description: This module provides low level access to the ProtoBuffer "Message" classes used by the API.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos" />
<meta itemprop="path" content="Stable" />
</div>

# Module: google.generativeai.protos

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/protos.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



This module provides low level access to the ProtoBuffer "Message" classes used by the API.


**For typical usage of this SDK you do not need to use any of these classes.**

ProtoBufers are Google API's serilization format. They are strongly typed and efficient.

The `genai` SDK tries to be permissive about what objects it will accept from a user, but in the end
the SDK always converts input to an appropriate Proto Message object to send as the request. Each API request
has a `*Request` and `*Response` Message defined here.

If you have any uncertainty about what the API may accept or return, these classes provide the
complete/unambiguous answer. They come from the `google-ai-generativelanguage` package which is
generated from a snapshot of the API definition.

```
>>> from google.generativeai import protos
>>> import inspect
>>> print(inspect.getsource(protos.Part))
```

Proto classes can have "oneof" fields. Use `in` to check which `oneof` field is set.

```
>>> p = protos.Part(text='hello')
>>> 'text' in p
True
>>> p.inline_data = {'mime_type':'image/png', 'data': b'PNG'}
>>> type(p.inline_data) is protos.Blob
True
>>> 'inline_data' in p
True
>>> 'text' in p
False
```

Instances of all Message classes can be converted into JSON compatible dictionaries with the following construct
(Bytes are base64 encoded):

```
>>> p_dict = type(p).to_dict(p)
>>> p_dict
{'inline_data': {'mime_type': 'image/png', 'data': 'UE5H'}}
```

A compatible dict can be converted to an instance of a Message class by passing it as the first argument to the
constructor:

```
>>> p = protos.Part(p_dict)
inline_data {
  mime_type: "image/png"
  data: "PNG"
}
```

Note when converting that `to_dict` accepts additional arguments:

- `use_integers_for_enums:bool = True`, Set it to `False` to replace enum int values with their string
   names in the output
- ` including_default_value_fields:bool = True`, Set it to `False` to reduce the verbosity of the output.

Additional arguments are described in the docstring:

```
>>> help(proto.Part.to_dict)
```

## Classes

[`class AttributionSourceId`](../../google/generativeai/protos/AttributionSourceId.md): Identifier for the source contributing to this attribution.

[`class BatchCreateChunksRequest`](../../google/generativeai/protos/BatchCreateChunksRequest.md): Request to batch create ``Chunk``\ s.

[`class BatchCreateChunksResponse`](../../google/generativeai/protos/BatchCreateChunksResponse.md): Response from ``BatchCreateChunks`` containing a list of created ``Chunk``\ s.

[`class BatchDeleteChunksRequest`](../../google/generativeai/protos/BatchDeleteChunksRequest.md): Request to batch delete ``Chunk``\ s.

[`class BatchEmbedContentsRequest`](../../google/generativeai/protos/BatchEmbedContentsRequest.md): Batch request to get embeddings from the model for a list of prompts.

[`class BatchEmbedContentsResponse`](../../google/generativeai/protos/BatchEmbedContentsResponse.md): The response to a ``BatchEmbedContentsRequest``.

[`class BatchEmbedTextRequest`](../../google/generativeai/protos/BatchEmbedTextRequest.md): Batch request to get a text embedding from the model.

[`class BatchEmbedTextResponse`](../../google/generativeai/protos/BatchEmbedTextResponse.md): The response to a EmbedTextRequest.

[`class BatchUpdateChunksRequest`](../../google/generativeai/protos/BatchUpdateChunksRequest.md): Request to batch update ``Chunk``\ s.

[`class BatchUpdateChunksResponse`](../../google/generativeai/protos/BatchUpdateChunksResponse.md): Response from ``BatchUpdateChunks`` containing a list of updated ``Chunk``\ s.

[`class Blob`](../../google/generativeai/protos/Blob.md): Raw media bytes.

[`class CachedContent`](../../google/generativeai/protos/CachedContent.md): Content that has been preprocessed and can be used in subsequent request to GenerativeService.

[`class Candidate`](../../google/generativeai/protos/Candidate.md): A response candidate generated from the model.

[`class Chunk`](../../google/generativeai/protos/Chunk.md): A ``Chunk`` is a subpart of a ``Document`` that is treated as an independent unit for the purposes of vector representation and storage.

[`class ChunkData`](../../google/generativeai/protos/ChunkData.md): Extracted data that represents the ``Chunk`` content.

[`class CitationMetadata`](../../google/generativeai/protos/CitationMetadata.md): A collection of source attributions for a piece of content.

[`class CitationSource`](../../google/generativeai/protos/CitationSource.md): A citation to a source for a portion of a specific response.

[`class CodeExecution`](../../google/generativeai/protos/CodeExecution.md): Tool that executes code generated by the model, and automatically returns the result to the model.

[`class CodeExecutionResult`](../../google/generativeai/protos/CodeExecutionResult.md): Result of executing the ``ExecutableCode``.

[`class Condition`](../../google/generativeai/protos/Condition.md): Filter condition applicable to a single key.

[`class Content`](../../google/generativeai/protos/Content.md): The base structured datatype containing multi-part content of a message.

[`class ContentEmbedding`](../../google/generativeai/protos/ContentEmbedding.md): A list of floats representing an embedding.

[`class ContentFilter`](../../google/generativeai/protos/ContentFilter.md): Content filtering metadata associated with processing a single request.

[`class Corpus`](../../google/generativeai/protos/Corpus.md): A ``Corpus`` is a collection of ``Document``\ s.

[`class CountMessageTokensRequest`](../../google/generativeai/protos/CountMessageTokensRequest.md): Counts the number of tokens in the ``prompt`` sent to a model.

[`class CountMessageTokensResponse`](../../google/generativeai/protos/CountMessageTokensResponse.md): A response from ``CountMessageTokens``.

[`class CountTextTokensRequest`](../../google/generativeai/protos/CountTextTokensRequest.md): Counts the number of tokens in the ``prompt`` sent to a model.

[`class CountTextTokensResponse`](../../google/generativeai/protos/CountTextTokensResponse.md): A response from ``CountTextTokens``.

[`class CountTokensRequest`](../../google/generativeai/protos/CountTokensRequest.md): Counts the number of tokens in the ``prompt`` sent to a model.

[`class CountTokensResponse`](../../google/generativeai/protos/CountTokensResponse.md): A response from ``CountTokens``.

[`class CreateCachedContentRequest`](../../google/generativeai/protos/CreateCachedContentRequest.md): Request to create CachedContent.

[`class CreateChunkRequest`](../../google/generativeai/protos/CreateChunkRequest.md): Request to create a ``Chunk``.

[`class CreateCorpusRequest`](../../google/generativeai/protos/CreateCorpusRequest.md): Request to create a ``Corpus``.

[`class CreateDocumentRequest`](../../google/generativeai/protos/CreateDocumentRequest.md): Request to create a ``Document``.

[`class CreateFileRequest`](../../google/generativeai/protos/CreateFileRequest.md): Request for ``CreateFile``.

[`class CreateFileResponse`](../../google/generativeai/protos/CreateFileResponse.md): Response for ``CreateFile``.

[`class CreatePermissionRequest`](../../google/generativeai/protos/CreatePermissionRequest.md): Request to create a ``Permission``.

[`class CreateTunedModelMetadata`](../../google/generativeai/protos/CreateTunedModelMetadata.md): Metadata about the state and progress of creating a tuned model returned from the long-running operation

[`class CreateTunedModelRequest`](../../google/generativeai/protos/CreateTunedModelRequest.md): Request to create a TunedModel.

[`class CustomMetadata`](../../google/generativeai/protos/CustomMetadata.md): User provided metadata stored as key-value pairs.

[`class Dataset`](../../google/generativeai/protos/Dataset.md): Dataset for training or validation.

[`class DeleteCachedContentRequest`](../../google/generativeai/protos/DeleteCachedContentRequest.md): Request to delete CachedContent.

[`class DeleteChunkRequest`](../../google/generativeai/protos/DeleteChunkRequest.md): Request to delete a ``Chunk``.

[`class DeleteCorpusRequest`](../../google/generativeai/protos/DeleteCorpusRequest.md): Request to delete a ``Corpus``.

[`class DeleteDocumentRequest`](../../google/generativeai/protos/DeleteDocumentRequest.md): Request to delete a ``Document``.

[`class DeleteFileRequest`](../../google/generativeai/protos/DeleteFileRequest.md): Request for ``DeleteFile``.

[`class DeletePermissionRequest`](../../google/generativeai/protos/DeletePermissionRequest.md): Request to delete the ``Permission``.

[`class DeleteTunedModelRequest`](../../google/generativeai/protos/DeleteTunedModelRequest.md): Request to delete a TunedModel.

[`class Document`](../../google/generativeai/protos/Document.md): A ``Document`` is a collection of ``Chunk``\ s.

[`class EmbedContentRequest`](../../google/generativeai/protos/EmbedContentRequest.md): Request containing the ``Content`` for the model to embed.

[`class EmbedContentResponse`](../../google/generativeai/protos/EmbedContentResponse.md): The response to an ``EmbedContentRequest``.

[`class EmbedTextRequest`](../../google/generativeai/protos/EmbedTextRequest.md): Request to get a text embedding from the model.

[`class EmbedTextResponse`](../../google/generativeai/protos/EmbedTextResponse.md): The response to a EmbedTextRequest.

[`class Embedding`](../../google/generativeai/protos/Embedding.md): A list of floats representing the embedding.

[`class Example`](../../google/generativeai/protos/Example.md): An input/output example used to instruct the Model.

[`class ExecutableCode`](../../google/generativeai/protos/ExecutableCode.md): Code generated by the model that is meant to be executed, and the result returned to the model.

[`class File`](../../google/generativeai/protos/File.md): A file uploaded to the API.

[`class FileData`](../../google/generativeai/protos/FileData.md): URI based data.

[`class FunctionCall`](../../google/generativeai/protos/FunctionCall.md): A predicted ``FunctionCall`` returned from the model that contains a string representing the <a href="../../google/generativeai/protos/FunctionDeclaration.md#name"><code>FunctionDeclaration.name</code></a> with the arguments and their values.

[`class FunctionCallingConfig`](../../google/generativeai/protos/FunctionCallingConfig.md): Configuration for specifying function calling behavior.

[`class FunctionDeclaration`](../../google/generativeai/protos/FunctionDeclaration.md): Structured representation of a function declaration as defined by the `OpenAPI 3.03 specification <https://spec.openapis.org/oas/v3.0.3>`__.

[`class FunctionResponse`](../../google/generativeai/protos/FunctionResponse.md): The result output from a ``FunctionCall`` that contains a string representing the <a href="../../google/generativeai/protos/FunctionDeclaration.md#name"><code>FunctionDeclaration.name</code></a> and a structured JSON object containing any output from the function is used as context to the model.

[`class GenerateAnswerRequest`](../../google/generativeai/protos/GenerateAnswerRequest.md): Request to generate a grounded answer from the model.

[`class GenerateAnswerResponse`](../../google/generativeai/protos/GenerateAnswerResponse.md): Response from the model for a grounded answer.

[`class GenerateContentRequest`](../../google/generativeai/protos/GenerateContentRequest.md): Request to generate a completion from the model.

[`class GenerateContentResponse`](../../google/generativeai/protos/GenerateContentResponse.md): Response from the model supporting multiple candidates.

[`class GenerateMessageRequest`](../../google/generativeai/protos/GenerateMessageRequest.md): Request to generate a message response from the model.

[`class GenerateMessageResponse`](../../google/generativeai/protos/GenerateMessageResponse.md): The response from the model.

[`class GenerateTextRequest`](../../google/generativeai/protos/GenerateTextRequest.md): Request to generate a text completion response from the model.

[`class GenerateTextResponse`](../../google/generativeai/protos/GenerateTextResponse.md): The response from the model, including candidate completions.

[`class GenerationConfig`](../../google/generativeai/protos/GenerationConfig.md): Configuration options for model generation and outputs.

[`class GetCachedContentRequest`](../../google/generativeai/protos/GetCachedContentRequest.md): Request to read CachedContent.

[`class GetChunkRequest`](../../google/generativeai/protos/GetChunkRequest.md): Request for getting information about a specific ``Chunk``.

[`class GetCorpusRequest`](../../google/generativeai/protos/GetCorpusRequest.md): Request for getting information about a specific ``Corpus``.

[`class GetDocumentRequest`](../../google/generativeai/protos/GetDocumentRequest.md): Request for getting information about a specific ``Document``.

[`class GetFileRequest`](../../google/generativeai/protos/GetFileRequest.md): Request for ``GetFile``.

[`class GetModelRequest`](../../google/generativeai/protos/GetModelRequest.md): Request for getting information about a specific Model.

[`class GetPermissionRequest`](../../google/generativeai/protos/GetPermissionRequest.md): Request for getting information about a specific ``Permission``.

[`class GetTunedModelRequest`](../../google/generativeai/protos/GetTunedModelRequest.md): Request for getting information about a specific Model.

[`class GroundingAttribution`](../../google/generativeai/protos/GroundingAttribution.md): Attribution for a source that contributed to an answer.

[`class GroundingPassage`](../../google/generativeai/protos/GroundingPassage.md): Passage included inline with a grounding configuration.

[`class GroundingPassages`](../../google/generativeai/protos/GroundingPassages.md): A repeated list of passages.

[`class HarmCategory`](../../google/generativeai/protos/HarmCategory.md): The category of a rating.

[`class Hyperparameters`](../../google/generativeai/protos/Hyperparameters.md): Hyperparameters controlling the tuning process.

[`class ListCachedContentsRequest`](../../google/generativeai/protos/ListCachedContentsRequest.md): Request to list CachedContents.

[`class ListCachedContentsResponse`](../../google/generativeai/protos/ListCachedContentsResponse.md): Response with CachedContents list.

[`class ListChunksRequest`](../../google/generativeai/protos/ListChunksRequest.md): Request for listing ``Chunk``\ s.

[`class ListChunksResponse`](../../google/generativeai/protos/ListChunksResponse.md): Response from ``ListChunks`` containing a paginated list of ``Chunk``\ s.

[`class ListCorporaRequest`](../../google/generativeai/protos/ListCorporaRequest.md): Request for listing ``Corpora``.

[`class ListCorporaResponse`](../../google/generativeai/protos/ListCorporaResponse.md): Response from ``ListCorpora`` containing a paginated list of ``Corpora``.

[`class ListDocumentsRequest`](../../google/generativeai/protos/ListDocumentsRequest.md): Request for listing ``Document``\ s.

[`class ListDocumentsResponse`](../../google/generativeai/protos/ListDocumentsResponse.md): Response from ``ListDocuments`` containing a paginated list of ``Document``\ s.

[`class ListFilesRequest`](../../google/generativeai/protos/ListFilesRequest.md): Request for ``ListFiles``.

[`class ListFilesResponse`](../../google/generativeai/protos/ListFilesResponse.md): Response for ``ListFiles``.

[`class ListModelsRequest`](../../google/generativeai/protos/ListModelsRequest.md): Request for listing all Models.

[`class ListModelsResponse`](../../google/generativeai/protos/ListModelsResponse.md): Response from ``ListModel`` containing a paginated list of Models.

[`class ListPermissionsRequest`](../../google/generativeai/protos/ListPermissionsRequest.md): Request for listing permissions.

[`class ListPermissionsResponse`](../../google/generativeai/protos/ListPermissionsResponse.md): Response from ``ListPermissions`` containing a paginated list of permissions.

[`class ListTunedModelsRequest`](../../google/generativeai/protos/ListTunedModelsRequest.md): Request for listing TunedModels.

[`class ListTunedModelsResponse`](../../google/generativeai/protos/ListTunedModelsResponse.md): Response from ``ListTunedModels`` containing a paginated list of Models.

[`class Message`](../../google/generativeai/protos/Message.md): The base unit of structured text.

[`class MessagePrompt`](../../google/generativeai/protos/MessagePrompt.md): All of the structured input text passed to the model as a prompt.

[`class MetadataFilter`](../../google/generativeai/protos/MetadataFilter.md): User provided filter to limit retrieval based on ``Chunk`` or ``Document`` level metadata values.

[`class Model`](../../google/generativeai/protos/Model.md): Information about a Generative Language Model.

[`class Part`](../../google/generativeai/protos/Part.md): A datatype containing media that is part of a multi-part ``Content`` message.

[`class Permission`](../../google/generativeai/protos/Permission.md): Permission resource grants user, group or the rest of the world access to the PaLM API resource (e.g.

[`class QueryCorpusRequest`](../../google/generativeai/protos/QueryCorpusRequest.md): Request for querying a ``Corpus``.

[`class QueryCorpusResponse`](../../google/generativeai/protos/QueryCorpusResponse.md): Response from ``QueryCorpus`` containing a list of relevant chunks.

[`class QueryDocumentRequest`](../../google/generativeai/protos/QueryDocumentRequest.md): Request for querying a ``Document``.

[`class QueryDocumentResponse`](../../google/generativeai/protos/QueryDocumentResponse.md): Response from ``QueryDocument`` containing a list of relevant chunks.

[`class RelevantChunk`](../../google/generativeai/protos/RelevantChunk.md): The information for a chunk relevant to a query.

[`class SafetyFeedback`](../../google/generativeai/protos/SafetyFeedback.md): Safety feedback for an entire request.

[`class SafetyRating`](../../google/generativeai/protos/SafetyRating.md): Safety rating for a piece of content.

[`class SafetySetting`](../../google/generativeai/protos/SafetySetting.md): Safety setting, affecting the safety-blocking behavior.

[`class Schema`](../../google/generativeai/protos/Schema.md): The ``Schema`` object allows the definition of input and output data types.

[`class SemanticRetrieverConfig`](../../google/generativeai/protos/SemanticRetrieverConfig.md): Configuration for retrieving grounding content from a ``Corpus`` or ``Document`` created using the Semantic Retriever API.

[`class StringList`](../../google/generativeai/protos/StringList.md): User provided string values assigned to a single metadata key.

[`class TaskType`](../../google/generativeai/protos/TaskType.md): Type of task for which the embedding will be used.

[`class TextCompletion`](../../google/generativeai/protos/TextCompletion.md): Output text returned from a model.

[`class TextPrompt`](../../google/generativeai/protos/TextPrompt.md): Text given to the model as a prompt.

[`class Tool`](../../google/generativeai/protos/Tool.md): Tool details that the model may use to generate response.

[`class ToolConfig`](../../google/generativeai/protos/ToolConfig.md): The Tool configuration containing parameters for specifying ``Tool`` use in the request.

[`class TransferOwnershipRequest`](../../google/generativeai/protos/TransferOwnershipRequest.md): Request to transfer the ownership of the tuned model.

[`class TransferOwnershipResponse`](../../google/generativeai/protos/TransferOwnershipResponse.md): Response from ``TransferOwnership``.

[`class TunedModel`](../../google/generativeai/protos/TunedModel.md): A fine-tuned model created using ModelService.CreateTunedModel.

[`class TunedModelSource`](../../google/generativeai/protos/TunedModelSource.md): Tuned model as a source for training a new model.

[`class TuningExample`](../../google/generativeai/protos/TuningExample.md): A single example for tuning.

[`class TuningExamples`](../../google/generativeai/protos/TuningExamples.md): A set of tuning examples. Can be training or validation data.

[`class TuningSnapshot`](../../google/generativeai/protos/TuningSnapshot.md): Record for a single tuning step.

[`class TuningTask`](../../google/generativeai/protos/TuningTask.md): Tuning tasks that create tuned models.

[`class Type`](../../google/generativeai/protos/Type.md): Type contains the list of OpenAPI data types as defined by https://spec.openapis.org/oas/v3.0.3#data-types

[`class UpdateCachedContentRequest`](../../google/generativeai/protos/UpdateCachedContentRequest.md): Request to update CachedContent.

[`class UpdateChunkRequest`](../../google/generativeai/protos/UpdateChunkRequest.md): Request to update a ``Chunk``.

[`class UpdateCorpusRequest`](../../google/generativeai/protos/UpdateCorpusRequest.md): Request to update a ``Corpus``.

[`class UpdateDocumentRequest`](../../google/generativeai/protos/UpdateDocumentRequest.md): Request to update a ``Document``.

[`class UpdatePermissionRequest`](../../google/generativeai/protos/UpdatePermissionRequest.md): Request to update the ``Permission``.

[`class UpdateTunedModelRequest`](../../google/generativeai/protos/UpdateTunedModelRequest.md): Request to update a TunedModel.

[`class VideoMetadata`](../../google/generativeai/protos/VideoMetadata.md): Metadata for a video ``File``.

