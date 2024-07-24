description: A permission to access a resource.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.Permission" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="delete"/>
<meta itemprop="property" content="delete_async"/>
<meta itemprop="property" content="get"/>
<meta itemprop="property" content="get_async"/>
<meta itemprop="property" content="to_dict"/>
<meta itemprop="property" content="update"/>
<meta itemprop="property" content="update_async"/>
<meta itemprop="property" content="email_address"/>
</div>

# google.generativeai.types.Permission

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L92-L267">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A permission to access a resource.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.Permission(
    name: str,
    role: RoleOptions,
    grantee_type: Optional[GranteeTypeOptions] = None,
    email_address: Optional[str] = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`role`<a id="role"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`grantee_type`<a id="grantee_type"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`email_address`<a id="email_address"></a>
</td>
<td>
Dataclass field
</td>
</tr>
</table>



## Methods

<h3 id="delete"><code>delete</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L122-L132">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>delete(
    client: (glm.PermissionServiceClient | None) = None
) -> None
</code></pre>

Delete permission (self).


<h3 id="delete_async"><code>delete_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L134-L144">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>delete_async(
    client=None
)
</code></pre>

This is the async version of <a href="../../../google/generativeai/types/Permission.md#delete"><code>Permission.delete</code></a>.


<h3 id="get"><code>get</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L231-L251">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>get(
    name: str, client: (glm.PermissionServiceClient | None) = None
) -> Permission
</code></pre>

Get information about a specific permission.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the permission to get.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Requested permission as an instance of `Permission`.
</td>
</tr>

</table>



<h3 id="get_async"><code>get_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L253-L267">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_async(
    name, client=None
)
</code></pre>

This is the async version of <a href="../../../google/generativeai/types/Permission.md#get"><code>Permission.get</code></a>.


<h3 id="to_dict"><code>to_dict</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L228-L229">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_dict() -> dict[str, Any]
</code></pre>




<h3 id="update"><code>update</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L153-L188">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update(
    updates: dict[str, Any],
    client: (glm.PermissionServiceClient | None) = None
) -> Permission
</code></pre>

Update a list of fields for a specified permission.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`updates`
</td>
<td>
The list of fields to update.
Currently only `role` is supported as an update path.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Permission` object with specified updates.
</td>
</tr>

</table>



<h3 id="update_async"><code>update_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L190-L218">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_async(
    updates, client=None
)
</code></pre>

This is the async version of <a href="../../../google/generativeai/types/Permission.md#update"><code>Permission.update</code></a>.


<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.






<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Class Variables</h2></th></tr>

<tr>
<td>
email_address<a id="email_address"></a>
</td>
<td>
`None`
</td>
</tr>
</table>

