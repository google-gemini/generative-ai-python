description: Configuration for specifying function calling behavior.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.FunctionCallingConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="Mode"/>
</div>

# google.generativeai.protos.FunctionCallingConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L408-L462">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for specifying function calling behavior.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`mode`<a id="mode"></a>
</td>
<td>
`google.ai.generativelanguage.FunctionCallingConfig.Mode`

Optional. Specifies the mode in which
function calling should execute. If unspecified,
the default value will be set to AUTO.
</td>
</tr><tr>
<td>
`allowed_function_names`<a id="allowed_function_names"></a>
</td>
<td>
`MutableSequence[str]`

Optional. A set of function names that, when provided,
limits the functions the model will call.

This should only be set when the Mode is ANY. Function names
should match [FunctionDeclaration.name]. With mode set to
ANY, model will predict a function call from the set of
function names provided.
</td>
</tr>
</table>



## Child Classes
[`class Mode`](../../../google/generativeai/protos/FunctionCallingConfig/Mode.md)

