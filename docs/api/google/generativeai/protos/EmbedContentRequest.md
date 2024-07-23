description: Request containing the Content for the model to embed.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.EmbedContentRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.EmbedContentRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L959-L1023">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request containing the ``Content`` for the model to embed.

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

Required. The model's resource name. This serves as an ID
for the Model to use.

This name should match a model name returned by the
``ListModels`` method.

Format: ``models/{model}``
</td>
</tr><tr>
<td>
`content`<a id="content"></a>
</td>
<td>
`google.ai.generativelanguage.Content`

Required. The content to embed. Only the ``parts.text``
fields will be counted.
</td>
</tr><tr>
<td>
`task_type`<a id="task_type"></a>
</td>
<td>
`google.ai.generativelanguage.TaskType`

Optional. Optional task type for which the embeddings will
be used. Can only be set for ``models/embedding-001``.

</td>
</tr><tr>
<td>
`title`<a id="title"></a>
</td>
<td>
`str`

Optional. An optional title for the text. Only applicable
when TaskType is ``RETRIEVAL_DOCUMENT``.

Note: Specifying a ``title`` for ``RETRIEVAL_DOCUMENT``
provides better quality embeddings for retrieval.

</td>
</tr><tr>
<td>
`output_dimensionality`<a id="output_dimensionality"></a>
</td>
<td>
`int`

Optional. Optional reduced dimension for the output
embedding. If set, excessive values in the output embedding
are truncated from the end. Supported by newer models since
2024, and the earlier model (``models/embedding-001``)
cannot specify this value.

</td>
</tr>
</table>



