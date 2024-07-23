description: Counts the number of tokens in the prompt sent to a model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CountMessageTokensRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CountMessageTokensRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/discuss_service.py#L306-L334">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Counts the number of tokens in the ``prompt`` sent to a model.

<!-- Placeholder for "Used in" -->

Models may tokenize text differently, so each model may return a
different ``token_count``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
`str`

Required. The model's resource name. This serves as an ID
for the Model to use.

This name should match a model name returned by the
``ListModels`` method.

Format: ``models/{model}``
</td>
</tr><tr>
<td>
`prompt`<a id="prompt"></a>
</td>
<td>
`google.ai.generativelanguage.MessagePrompt`

Required. The prompt, whose token count is to
be returned.
</td>
</tr>
</table>



