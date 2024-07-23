description: A Document is a collection of Chunk\ s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Document" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Document

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever.py#L84-L137">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A ``Document`` is a collection of ``Chunk``\ s.

<!-- Placeholder for "Used in" -->
 A ``Corpus`` can
have a maximum of 10,000 ``Document``\ s.



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

Immutable. Identifier. The ``Document`` resource name. The
ID (name excluding the `corpora/*/documents/` prefix) can
contain up to 40 characters that are lowercase alphanumeric
or dashes (-). The ID cannot start or end with a dash. If
the name is empty on create, a unique name will be derived
from ``display_name`` along with a 12 character random
suffix. Example:
``corpora/{corpus_id}/documents/my-awesome-doc-123a456b789c``
</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
`str`

Optional. The human-readable display name for the
``Document``. The display name must be no more than 512
characters in length, including spaces. Example: "Semantic
Retriever Documentation".
</td>
</tr><tr>
<td>
`custom_metadata`<a id="custom_metadata"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.CustomMetadata]`

Optional. User provided custom metadata stored as key-value
pairs used for querying. A ``Document`` can have a maximum
of 20 ``CustomMetadata``.
</td>
</tr><tr>
<td>
`update_time`<a id="update_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The Timestamp of when the ``Document`` was last
updated.
</td>
</tr><tr>
<td>
`create_time`<a id="create_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The Timestamp of when the ``Document`` was
created.
</td>
</tr>
</table>



