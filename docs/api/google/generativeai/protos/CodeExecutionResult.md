description: Result of executing the ExecutableCode.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CodeExecutionResult" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="Outcome"/>
</div>

# google.generativeai.protos.CodeExecutionResult

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L295-L340">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Result of executing the ``ExecutableCode``.

<!-- Placeholder for "Used in" -->

Only generated when using the ``CodeExecution``, and always follows
a ``part`` containing the ``ExecutableCode``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`outcome`<a id="outcome"></a>
</td>
<td>
`google.ai.generativelanguage.CodeExecutionResult.Outcome`

Required. Outcome of the code execution.
</td>
</tr><tr>
<td>
`output`<a id="output"></a>
</td>
<td>
`str`

Optional. Contains stdout when code execution
is successful, stderr or other description
otherwise.
</td>
</tr>
</table>



## Child Classes
[`class Outcome`](../../../google/generativeai/protos/CodeExecutionResult/Outcome.md)

