description: Calls the API to create an embedding for the text passed in.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.generate_embeddings" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.generate_embeddings

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/text.py#L297-L347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to create an embedding for the text passed in.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.generate_embeddings(
    model: model_types.BaseModelNameOptions,
    text: (str | Sequence[str]),
    client: glm.TextServiceClient = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> (text_types.EmbeddingDict | text_types.BatchEmbeddingDict)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
Which model to call, as a string or a <a href="../../google/generativeai/types/Model.md"><code>types.Model</code></a>.
</td>
</tr><tr>
<td>
`text`<a id="text"></a>
</td>
<td>
Free-form input text given to the model. Given a string, the model will
generate an embedding based on the input text.
</td>
</tr><tr>
<td>
`client`<a id="client"></a>
</td>
<td>
If you're not relying on a default client, you pass a `glm.TextServiceClient` instead.
</td>
</tr><tr>
<td>
`request_options`<a id="request_options"></a>
</td>
<td>
Options for the request.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Dictionary containing the embedding (list of float values) for the input text.
</td>
</tr>

</table>

