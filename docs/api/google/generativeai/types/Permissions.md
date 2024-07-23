<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.Permissions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="create"/>
<meta itemprop="property" content="create_async"/>
<meta itemprop="property" content="get"/>
<meta itemprop="property" content="get_async"/>
<meta itemprop="property" content="list"/>
<meta itemprop="property" content="list_async"/>
<meta itemprop="property" content="transfer_ownership"/>
<meta itemprop="property" content="transfer_ownership_async"/>
</div>

# google.generativeai.types.Permissions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L270-L479">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>





<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.Permissions(
    parent
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`parent`<a id="parent"></a>
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="create"><code>create</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L317-L348">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create(
    role: RoleOptions,
    grantee_type: Optional[GranteeTypeOptions] = None,
    email_address: Optional[str] = None,
    client: (glm.PermissionServiceClient | None) = None
) -> Permission
</code></pre>

Create a new permission on a resource (self).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`parent`
</td>
<td>
The resource name of the parent resource in which the permission will be listed.
</td>
</tr><tr>
<td>
`role`
</td>
<td>
role that will be granted by the permission.
</td>
</tr><tr>
<td>
`grantee_type`
</td>
<td>
The type of the grantee for the permission.
</td>
</tr><tr>
<td>
`email_address`
</td>
<td>
The email address of the grantee.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Permission` object with specified parent, role, grantee type, and email address.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When email_address is specified and grantee_type is set to EVERYONE.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
When email_address is not specified and grantee_type is not set to EVERYONE.
</td>
</tr>
</table>



<h3 id="create_async"><code>create_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L350-L368">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_async(
    role, grantee_type=None, email_address=None, client=None
)
</code></pre>

This is the async version of `PermissionAdapter.create_permission`.


<h3 id="get"><code>get</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L419-L430">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>get(
    name: str
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

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L432-L443">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_async(
    name
)
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



<h3 id="list"><code>list</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L370-L393">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>list(
    page_size: Optional[int] = None,
    client: (glm.PermissionServiceClient | None) = None
) -> Iterable[Permission]
</code></pre>

List `Permission`s enforced on a resource (self).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`parent`
</td>
<td>
The resource name of the parent resource in which the permission will be listed.
</td>
</tr><tr>
<td>
`page_size`
</td>
<td>
The maximum number of permissions to return (per page). The service may return fewer permissions.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Paginated list of `Permission` objects.
</td>
</tr>

</table>



<h3 id="list_async"><code>list_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L398-L414">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>list_async(
    page_size=None, client=None
)
</code></pre>

This is the async version of `PermissionAdapter.list_permissions`.


<h3 id="transfer_ownership"><code>transfer_ownership</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L445-L464">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>transfer_ownership(
    email_address: str, client: (glm.PermissionServiceClient | None) = None
) -> None
</code></pre>

Transfer ownership of a resource (self) to a new owner.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Name of the resource to transfer ownership.
</td>
</tr><tr>
<td>
`email_address`
</td>
<td>
Email address of the new owner.
</td>
</tr>
</table>



<h3 id="transfer_ownership_async"><code>transfer_ownership_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L466-L479">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>transfer_ownership_async(
    email_address, client=None
)
</code></pre>

This is the async version of `PermissionAdapter.transfer_ownership`.


<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/permission_types.py#L395-L396">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>






