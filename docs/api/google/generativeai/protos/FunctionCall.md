description: A predicted FunctionCall returned from the model that contains a string representing the <a href="../../../google/generativeai/protos/FunctionDeclaration.md#name"><code>FunctionDeclaration.name</code></a> with the arguments and their values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.FunctionCall" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.FunctionCall

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L511-L540">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A predicted ``FunctionCall`` returned from the model that contains a string representing the <a href="../../../google/generativeai/protos/FunctionDeclaration.md#name"><code>FunctionDeclaration.name</code></a> with the arguments and their values.

<!-- Placeholder for "Used in" -->





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

Required. The name of the function to call.
Must be a-z, A-Z, 0-9, or contain underscores
and dashes, with a maximum length of 63.
</td>
</tr><tr>
<td>
`args`<a id="args"></a>
</td>
<td>
`google.protobuf.struct_pb2.Struct`

Optional. The function parameters and values
in JSON object format.

</td>
</tr>
</table>



