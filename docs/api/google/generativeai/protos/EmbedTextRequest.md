description: Request to get a text embedding from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.EmbedTextRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.EmbedTextRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/text_service.py#L286-L305">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to get a text embedding from the model.

<!-- Placeholder for "Used in" -->




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

Required. The model name to use with the
format model=models/{model}.
</td>
</tr><tr>
<td>
`text`<a id="text"></a>
</td>
<td>
`str`

Optional. The free-form input text that the
model will turn into an embedding.
</td>
</tr>
</table>



