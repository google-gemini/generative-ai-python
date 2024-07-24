description: Structured representation of a function declaration as defined by the OpenAPI 3.03 specification <https://spec.openapis.org/oas/v3.0.3>__.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.FunctionDeclaration" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.FunctionDeclaration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L465-L508">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Structured representation of a function declaration as defined by the `OpenAPI 3.03 specification <https://spec.openapis.org/oas/v3.0.3>`__.

<!-- Placeholder for "Used in" -->
 Included in
this declaration are the function name and parameters. This
FunctionDeclaration is a representation of a block of code that can
be used as a ``Tool`` by the model and executed by the client.





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`<a id="name"></a>
</td>
<td>
`str`

Required. The name of the function.
Must be a-z, A-Z, 0-9, or contain underscores
and dashes, with a maximum length of 63.
</td>
</tr><tr>
<td>
`description`<a id="description"></a>
</td>
<td>
`str`

Required. A brief description of the
function.
</td>
</tr><tr>
<td>
`parameters`<a id="parameters"></a>
</td>
<td>
`google.ai.generativelanguage.Schema`

Optional. Describes the parameters to this
function. Reflects the Open API 3.03 Parameter
Object string Key: the name of the parameter.
Parameter names are case sensitive. Schema
Value: the Schema defining the type used for the
parameter.

</td>
</tr>
</table>



