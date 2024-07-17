description: Tool details that the model may use to generate response.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Tool" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Tool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L343-L379">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tool details that the model may use to generate response.

<!-- Placeholder for "Used in" -->

A ``Tool`` is a piece of code that enables the system to interact
with external systems to perform an action, or set of actions,
outside of knowledge and scope of the model.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`function_declarations`<a id="function_declarations"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.FunctionDeclaration]`

Optional. A list of ``FunctionDeclarations`` available to
the model that can be used for function calling.

The model or system does not execute the function. Instead
the defined function may be returned as a
[FunctionCall][content.part.function_call] with arguments to
the client side for execution. The model may decide to call
a subset of these functions by populating
[FunctionCall][content.part.function_call] in the response.
The next conversation turn may contain a
[FunctionResponse][content.part.function_response] with the
[content.role] "function" generation context for the next
model turn.
</td>
</tr><tr>
<td>
`code_execution`<a id="code_execution"></a>
</td>
<td>
`google.ai.generativelanguage.CodeExecution`

Optional. Enables the model to execute code
as part of generation.
</td>
</tr>
</table>



