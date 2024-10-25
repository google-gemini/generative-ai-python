
# google.generativeai.caching.CachedContent

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/caching.py#L32-L314">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Cached content resource.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.caching.CachedContent(
    name
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>

`name`<a id="name"></a>

</td>
<td>

The resource name referring to the cached content.

</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`create_time`<a id="create_time"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`display_name`<a id="display_name"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`expire_time`<a id="expire_time"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`model`<a id="model"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`name`<a id="name"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`update_time`<a id="update_time"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`usage_metadata`<a id="usage_metadata"></a>

</td>
<td>



</td>
</tr>
</table>



## Methods

<h3 id="create"><code>create</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/caching.py#L172-L221">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>create(
    model: str,
    *,
    display_name: (str | None) = None,
    system_instruction: Optional[content_types.ContentType] = None,
    contents: Optional[content_types.ContentsType] = None,
    tools: Optional[content_types.FunctionLibraryType] = None,
    tool_config: Optional[content_types.ToolConfigType] = None,
    ttl: Optional[caching_types.TTLTypes] = None,
    expire_time: Optional[caching_types.ExpireTimeTypes] = None
) -> CachedContent
</code></pre>

Creates `CachedContent` resource.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>

`model`

</td>
<td>

The name of the `model` to use for cached content creation.
Any `CachedContent` resource can be only used with the
`model` it was created for.

</td>
</tr><tr>
<td>

`display_name`

</td>
<td>

The user-generated meaningful display name
of the cached content. `display_name` must be no
more than 128 unicode characters.

</td>
</tr><tr>
<td>

`system_instruction`

</td>
<td>

Developer set system instruction.

</td>
</tr><tr>
<td>

`contents`

</td>
<td>

Contents to cache.

</td>
</tr><tr>
<td>

`tools`

</td>
<td>

A list of `Tools` the model may use to generate response.

</td>
</tr><tr>
<td>

`tool_config`

</td>
<td>

Config to apply to all tools.

</td>
</tr><tr>
<td>

`ttl`

</td>
<td>

TTL for cached resource (in seconds). Defaults to 1 hour.
`ttl` and `expire_time` are exclusive arguments.

</td>
</tr><tr>
<td>

`expire_time`

</td>
<td>

Expiration time for cached resource.
`ttl` and `expire_time` are exclusive arguments.

</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">

`CachedContent` resource with specified name.

</td>
</tr>

</table>



<h3 id="delete"><code>delete</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/caching.py#L261-L267">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>delete() -> None
</code></pre>

Deletes `CachedContent` resource.


<h3 id="get"><code>get</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/caching.py#L223-L241">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>get(
    name: str
) -> CachedContent
</code></pre>

Fetches required `CachedContent` resource.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>

`name`

</td>
<td>

The resource name referring to the cached content.

</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">

`CachedContent` resource with specified `name`.

</td>
</tr>

</table>



<h3 id="list"><code>list</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/caching.py#L243-L259">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>list(
    page_size: Optional[int] = 1
) -> Iterable[CachedContent]
</code></pre>

Lists `CachedContent` objects associated with the project.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>

`page_size`

</td>
<td>

The maximum number of permissions to return (per page).
The service may return fewer `CachedContent` objects.

</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">

A paginated list of `CachedContent` objects.

</td>
</tr>

</table>



<h3 id="update"><code>update</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/caching.py#L269-L314">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update(
    *,
    ttl: Optional[caching_types.TTLTypes] = None,
    expire_time: Optional[caching_types.ExpireTimeTypes] = None
) -> None
</code></pre>

Updates requested `CachedContent` resource.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>

`ttl`

</td>
<td>

TTL for cached resource (in seconds). Defaults to 1 hour.
`ttl` and `expire_time` are exclusive arguments.

</td>
</tr><tr>
<td>

`expire_time`

</td>
<td>

Expiration time for cached resource.
`ttl` and `expire_time` are exclusive arguments.

</td>
</tr>
</table>





