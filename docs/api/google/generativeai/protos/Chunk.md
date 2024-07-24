description: A Chunk is a subpart of a Document that is treated as an independent unit for the purposes of vector representation and storage.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Chunk" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="State"/>
</div>

# google.generativeai.protos.Chunk

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever.py#L310-L388">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A ``Chunk`` is a subpart of a ``Document`` that is treated as an independent unit for the purposes of vector representation and storage.

<!-- Placeholder for "Used in" -->
 A ``Corpus`` can have a maximum of 1 million ``Chunk``\ s.



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

Immutable. Identifier. The ``Chunk`` resource name. The ID
(name excluding the `corpora/*/documents/*/chunks/` prefix)
can contain up to 40 characters that are lowercase
alphanumeric or dashes (-). The ID cannot start or end with
a dash. If the name is empty on create, a random
12-character unique ID will be generated. Example:
``corpora/{corpus_id}/documents/{document_id}/chunks/123a456b789c``
</td>
</tr><tr>
<td>
`data`<a id="data"></a>
</td>
<td>
`google.ai.generativelanguage.ChunkData`

Required. The content for the ``Chunk``, such as the text
string. The maximum number of tokens per chunk is 2043.
</td>
</tr><tr>
<td>
`custom_metadata`<a id="custom_metadata"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.CustomMetadata]`

Optional. User provided custom metadata stored as key-value
pairs. The maximum number of ``CustomMetadata`` per chunk is
20.
</td>
</tr><tr>
<td>
`create_time`<a id="create_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The Timestamp of when the ``Chunk`` was
created.
</td>
</tr><tr>
<td>
`update_time`<a id="update_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The Timestamp of when the ``Chunk`` was last
updated.
</td>
</tr><tr>
<td>
`state`<a id="state"></a>
</td>
<td>
`google.ai.generativelanguage.Chunk.State`

Output only. Current state of the ``Chunk``.
</td>
</tr>
</table>



## Child Classes
[`class State`](../../../google/generativeai/protos/Chunk/State.md)

