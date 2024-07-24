description: Content that has been preprocessed and can be used in subsequent request to GenerativeService.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CachedContent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="UsageMetadata"/>
</div>

# google.generativeai.protos.CachedContent

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/cached_content.py#L34-L179">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Content that has been preprocessed and can be used in subsequent request to GenerativeService.

<!-- Placeholder for "Used in" -->

Cached content can be only used with model it was created for.

This message has `oneof`_ fields (mutually exclusive fields).
For each oneof, at most one member field can be set at the same time.
Setting any member of the oneof automatically clears all other
members.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`expire_time`<a id="expire_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Timestamp in UTC of when this resource is considered
expired. This is *always* provided on output, regardless of
what was sent on input.

This field is a member of `oneof`_ ``expiration``.
</td>
</tr><tr>
<td>
`ttl`<a id="ttl"></a>
</td>
<td>
`google.protobuf.duration_pb2.Duration`

Input only. New TTL for this resource, input
only.

This field is a member of `oneof`_ ``expiration``.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
`str`

Optional. Identifier. The resource name referring to the
cached content. Format: ``cachedContents/{id}``

</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
`str`

Optional. Immutable. The user-generated
meaningful display name of the cached content.
Maximum 128 Unicode characters.

</td>
</tr><tr>
<td>
`model`<a id="model"></a>
</td>
<td>
`str`

Required. Immutable. The name of the ``Model`` to use for
cached content Format: ``models/{model}``

</td>
</tr><tr>
<td>
`system_instruction`<a id="system_instruction"></a>
</td>
<td>
`google.ai.generativelanguage.Content`

Optional. Input only. Immutable. Developer
set system instruction. Currently text only.

</td>
</tr><tr>
<td>
`contents`<a id="contents"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Content]`

Optional. Input only. Immutable. The content
to cache.
</td>
</tr><tr>
<td>
`tools`<a id="tools"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Tool]`

Optional. Input only. Immutable. A list of ``Tools`` the
model may use to generate the next response
</td>
</tr><tr>
<td>
`tool_config`<a id="tool_config"></a>
</td>
<td>
`google.ai.generativelanguage.ToolConfig`

Optional. Input only. Immutable. Tool config.
This config is shared for all tools.

</td>
</tr><tr>
<td>
`create_time`<a id="create_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. Creation time of the cache
entry.
</td>
</tr><tr>
<td>
`update_time`<a id="update_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. When the cache entry was last
updated in UTC time.
</td>
</tr><tr>
<td>
`usage_metadata`<a id="usage_metadata"></a>
</td>
<td>
`google.ai.generativelanguage.CachedContent.UsageMetadata`

Output only. Metadata on the usage of the
cached content.
</td>
</tr>
</table>



## Child Classes
[`class UsageMetadata`](../../../google/generativeai/protos/CachedContent/UsageMetadata.md)

