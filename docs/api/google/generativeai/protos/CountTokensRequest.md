description: Counts the number of tokens in the prompt sent to a model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CountTokensRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CountTokensRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1103-L1140">
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
`contents`<a id="contents"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Content]`

Optional. The input given to the model as a prompt. This
field is ignored when ``generate_content_request`` is set.
</td>
</tr><tr>
<td>
`generate_content_request`<a id="generate_content_request"></a>
</td>
<td>
`google.ai.generativelanguage.GenerateContentRequest`

Optional. The overall input given to the
model. CountTokens will count prompt, function
calling, etc.
</td>
</tr>
</table>



