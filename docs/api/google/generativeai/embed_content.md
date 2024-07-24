description: Calls the API to create embeddings for content passed in.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.embed_content" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.embed_content

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/embedding.py#L124-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to create embeddings for content passed in.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.embed_content(
    model: model_types.BaseModelNameOptions,
    content: (content_types.ContentType | Iterable[content_types.ContentType]),
    task_type: (EmbeddingTaskTypeOptions | None) = None,
    title: (str | None) = None,
    output_dimensionality: (int | None) = None,
    client: glm.GenerativeServiceClient = None,
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
    Which [model](https://ai.google.dev/models/gemini#embedding) to
call, as a string or a <a href="../../google/generativeai/types/Model.md"><code>types.Model</code></a>.
</td>
</tr><tr>
<td>
`content`<a id="content"></a>
</td>
<td>
    Content to embed.
</td>
</tr><tr>
<td>
`task_type`<a id="task_type"></a>
</td>
<td>
    Optional task type for which the embeddings will be used. Can only
be set for `models/embedding-001`.
</td>
</tr><tr>
<td>
`title`<a id="title"></a>
</td>
<td>
    An optional title for the text. Only applicable when task_type is
`RETRIEVAL_DOCUMENT`.
</td>
</tr><tr>
<td>
`output_dimensionality`<a id="output_dimensionality"></a>
</td>
<td>
    Optional reduced dimensionality for the output embeddings. If set,
excessive values from the output embeddings will be truncated from
the end.
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
<tr><th colspan="2"><h2 class="add-link">Return</h2></th></tr>
<tr class="alt">
<td colspan="2">
Dictionary containing the embedding (list of float values) for the
input content.
</td>
</tr>

</table>

