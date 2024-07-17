description: Request to update a Chunk.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.UpdateChunkRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.UpdateChunkRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L618-L638">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to update a ``Chunk``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`chunk`<a id="chunk"></a>
</td>
<td>
`google.ai.generativelanguage.Chunk`

Required. The ``Chunk`` to update.
</td>
</tr><tr>
<td>
`update_mask`<a id="update_mask"></a>
</td>
<td>
`google.protobuf.field_mask_pb2.FieldMask`

Required. The list of fields to update. Currently, this only
supports updating ``custom_metadata`` and ``data``.
</td>
</tr>
</table>



