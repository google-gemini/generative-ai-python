description: A file uploaded to the API.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.File" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="State"/>
</div>

# google.generativeai.protos.File

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/file.py#L34-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A file uploaded to the API.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`video_metadata`<a id="video_metadata"></a>
</td>
<td>
`google.ai.generativelanguage.VideoMetadata`

Output only. Metadata for a video.

This field is a member of `oneof`_ ``metadata``.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
`str`

Immutable. Identifier. The ``File`` resource name. The ID
(name excluding the "files/" prefix) can contain up to 40
characters that are lowercase alphanumeric or dashes (-).
The ID cannot start or end with a dash. If the name is empty
on create, a unique name will be generated. Example:
``files/123-456``
</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
`str`

Optional. The human-readable display name for the ``File``.
The display name must be no more than 512 characters in
length, including spaces. Example: "Welcome Image".
</td>
</tr><tr>
<td>
`mime_type`<a id="mime_type"></a>
</td>
<td>
`str`

Output only. MIME type of the file.
</td>
</tr><tr>
<td>
`size_bytes`<a id="size_bytes"></a>
</td>
<td>
`int`

Output only. Size of the file in bytes.
</td>
</tr><tr>
<td>
`create_time`<a id="create_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp of when the ``File`` was created.
</td>
</tr><tr>
<td>
`update_time`<a id="update_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp of when the ``File`` was last
updated.
</td>
</tr><tr>
<td>
`expiration_time`<a id="expiration_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp of when the ``File`` will be
deleted. Only set if the ``File`` is scheduled to expire.
</td>
</tr><tr>
<td>
`sha256_hash`<a id="sha256_hash"></a>
</td>
<td>
`bytes`

Output only. SHA-256 hash of the uploaded
bytes.
</td>
</tr><tr>
<td>
`uri`<a id="uri"></a>
</td>
<td>
`str`

Output only. The uri of the ``File``.
</td>
</tr><tr>
<td>
`state`<a id="state"></a>
</td>
<td>
`google.ai.generativelanguage.File.State`

Output only. Processing state of the File.
</td>
</tr><tr>
<td>
`error`<a id="error"></a>
</td>
<td>
`google.rpc.status_pb2.Status`

Output only. Error status if File processing
failed.
</td>
</tr>
</table>



## Child Classes
[`class State`](../../../google/generativeai/protos/File/State.md)

