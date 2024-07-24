description: A collection of type definitions used throughout the library.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="annotations"/>
</div>

# Module: google.generativeai.types

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A collection of type definitions used throughout the library.



## Classes

[`class AsyncGenerateContentResponse`](../../google/generativeai/types/AsyncGenerateContentResponse.md): This is the async version of `genai.GenerateContentResponse`.

[`class AuthorError`](../../google/generativeai/types/AuthorError.md): Raised by the `chat` (or `reply`) functions when the author list can't be normalized.

[`class BlobDict`](../../google/generativeai/types/BlobDict.md): dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.

[`class BlockedPromptException`](../../google/generativeai/types/BlockedPromptException.md): Common base class for all non-exit exceptions.

[`class BlockedReason`](../../google/generativeai/types/BlockedReason.md): A list of reasons why content may have been blocked.

[`class BrokenResponseError`](../../google/generativeai/types/BrokenResponseError.md): Common base class for all non-exit exceptions.

[`class CallableFunctionDeclaration`](../../google/generativeai/types/CallableFunctionDeclaration.md): An extension of `FunctionDeclaration` that can be built from a python function, and is callable.

[`class ChatResponse`](../../google/generativeai/types/ChatResponse.md): A chat response from the model.

[`class CitationMetadataDict`](../../google/generativeai/types/CitationMetadataDict.md): A collection of source attributions for a piece of content.

[`class CitationSourceDict`](../../google/generativeai/types/CitationSourceDict.md): A citation to a source for a portion of a specific response.

[`class Completion`](../../google/generativeai/types/Completion.md): The result returned by <a href="../../google/generativeai/generate_text.md"><code>generativeai.generate_text</code></a>.

[`class ContentDict`](../../google/generativeai/types/ContentDict.md): dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.

[`class ContentFilterDict`](../../google/generativeai/types/ContentFilterDict.md): Content filtering metadata associated with processing a single request.

[`class ExampleDict`](../../google/generativeai/types/ExampleDict.md): A dict representation of a <a href="../../google/generativeai/protos/Example.md"><code>protos.Example</code></a>.

[`class File`](../../google/generativeai/types/File.md)

[`class FileDataDict`](../../google/generativeai/types/FileDataDict.md): dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.

[`class FunctionDeclaration`](../../google/generativeai/types/FunctionDeclaration.md)

[`class FunctionLibrary`](../../google/generativeai/types/FunctionLibrary.md): A container for a set of `Tool` objects, manages lookup and execution of their functions.

[`class GenerateContentResponse`](../../google/generativeai/types/GenerateContentResponse.md): Instances of this class manage the response of the `generate_content` method.

[`class GenerationConfig`](../../google/generativeai/types/GenerationConfig.md): A simple dataclass used to configure the generation parameters of <a href="../../google/generativeai/GenerativeModel.md#generate_content"><code>GenerativeModel.generate_content</code></a>.

[`class GenerationConfigDict`](../../google/generativeai/types/GenerationConfigDict.md): dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.

[`class HarmBlockThreshold`](../../google/generativeai/types/HarmBlockThreshold.md): Block at and beyond a specified harm probability.

[`class HarmCategory`](../../google/generativeai/types/HarmCategory.md): Harm Categories supported by the gemini-family model

[`class HarmProbability`](../../google/generativeai/types/HarmProbability.md): The probability that a piece of content is harmful.

[`class IncompleteIterationError`](../../google/generativeai/types/IncompleteIterationError.md): Common base class for all non-exit exceptions.

[`class MessageDict`](../../google/generativeai/types/MessageDict.md): A dict representation of a <a href="../../google/generativeai/protos/Message.md"><code>protos.Message</code></a>.

[`class MessagePromptDict`](../../google/generativeai/types/MessagePromptDict.md): A dict representation of a <a href="../../google/generativeai/protos/MessagePrompt.md"><code>protos.MessagePrompt</code></a>.

[`class Model`](../../google/generativeai/types/Model.md): A dataclass representation of a <a href="../../google/generativeai/protos/Model.md"><code>protos.Model</code></a>.

[`class PartDict`](../../google/generativeai/types/PartDict.md): dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.

[`class Permission`](../../google/generativeai/types/Permission.md): A permission to access a resource.

[`class Permissions`](../../google/generativeai/types/Permissions.md)

[`class RequestOptions`](../../google/generativeai/types/RequestOptions.md): Request options

[`class ResponseDict`](../../google/generativeai/types/ResponseDict.md): A dict representation of a <a href="../../google/generativeai/protos/GenerateMessageResponse.md"><code>protos.GenerateMessageResponse</code></a>.

[`class SafetyFeedbackDict`](../../google/generativeai/types/SafetyFeedbackDict.md): Safety feedback for an entire request.

[`class SafetyRatingDict`](../../google/generativeai/types/SafetyRatingDict.md): Safety rating for a piece of content.

[`class SafetySettingDict`](../../google/generativeai/types/SafetySettingDict.md): Safety setting, affecting the safety-blocking behavior.

[`class Status`](../../google/generativeai/types/Status.md): A ProtocolMessage

[`class StopCandidateException`](../../google/generativeai/types/StopCandidateException.md): Common base class for all non-exit exceptions.

[`class Tool`](../../google/generativeai/types/Tool.md): A wrapper for <a href="../../google/generativeai/protos/Tool.md"><code>protos.Tool</code></a>, Contains a collection of related `FunctionDeclaration` objects.

[`class ToolDict`](../../google/generativeai/types/ToolDict.md): dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.

[`class TunedModel`](../../google/generativeai/types/TunedModel.md): A dataclass representation of a <a href="../../google/generativeai/protos/TunedModel.md"><code>protos.TunedModel</code></a>.

[`class TunedModelState`](../../google/generativeai/types/TunedModelState.md): The state of the tuned model.

## Functions

[`TypedDict(...)`](../../google/generativeai/types/TypedDict.md): A simple typed namespace. At runtime it is equivalent to a plain dict.

[`get_default_file_client(...)`](../../google/generativeai/types/get_default_file_client.md)

[`to_file_data(...)`](../../google/generativeai/types/to_file_data.md)

## Type Aliases

[`AnyModelNameOptions`](../../google/generativeai/types/AnyModelNameOptions.md)

[`BaseModelNameOptions`](../../google/generativeai/types/BaseModelNameOptions.md)

[`BlobType`](../../google/generativeai/types/BlobType.md)

[`ContentType`](../../google/generativeai/types/ContentType.md)

[`ContentsType`](../../google/generativeai/types/ContentsType.md)

[`ExampleOptions`](../../google/generativeai/types/ExampleOptions.md)

[`ExamplesOptions`](../../google/generativeai/types/ExamplesOptions.md)

[`FileDataType`](../../google/generativeai/types/FileDataType.md)

[`FunctionDeclarationType`](../../google/generativeai/types/FunctionDeclarationType.md)

[`FunctionLibraryType`](../../google/generativeai/types/FunctionLibraryType.md)

[`GenerationConfigType`](../../google/generativeai/types/GenerationConfigType.md)

[`MessageOptions`](../../google/generativeai/types/MessageOptions.md)

[`MessagePromptOptions`](../../google/generativeai/types/MessagePromptOptions.md)

[`MessagesOptions`](../../google/generativeai/types/MessagesOptions.md)

[`ModelNameOptions`](../../google/generativeai/types/AnyModelNameOptions.md)

[`ModelsIterable`](../../google/generativeai/types/ModelsIterable.md)

[`PartType`](../../google/generativeai/types/PartType.md)

[`RequestOptionsType`](../../google/generativeai/types/RequestOptionsType.md)

[`StrictContentType`](../../google/generativeai/types/StrictContentType.md)

[`ToolsType`](../../google/generativeai/types/ToolsType.md)

[`TunedModelNameOptions`](../../google/generativeai/types/TunedModelNameOptions.md)



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Other Members</h2></th></tr>

<tr>
<td>
annotations<a id="annotations"></a>
</td>
<td>
Instance of `__future__._Feature`
</td>
</tr>
</table>

