description: An input/output example used to instruct the Model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Example" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Example

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/discuss_service.py#L280-L303">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An input/output example used to instruct the Model.

<!-- Placeholder for "Used in" -->

It demonstrates how the model should respond or format its
response.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
`google.ai.generativelanguage.Message`

Required. An example of an input ``Message`` from the user.
</td>
</tr><tr>
<td>
`output`<a id="output"></a>
</td>
<td>
`google.ai.generativelanguage.Message`

Required. An example of what the model should
output given the input.
</td>
</tr>
</table>



