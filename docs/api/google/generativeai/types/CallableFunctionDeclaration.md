
# google.generativeai.types.CallableFunctionDeclaration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L609-L630">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An extension of `FunctionDeclaration` that can be built from a python function, and is callable.

Inherits From: [`FunctionDeclaration`](../../../google/generativeai/types/FunctionDeclaration.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.CallableFunctionDeclaration(
    *,
    name: str,
    description: str,
    parameters: (dict[str, Any] | None) = None,
    function: Callable[..., Any]
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: The python function must have type annotations.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`description`<a id="description"></a>

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

`parameters`<a id="parameters"></a>

</td>
<td>



</td>
</tr>
</table>



## Methods

<h3 id="from_function"><code>from_function</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L583-L602">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_function(
    function: Callable[..., Any], descriptions: (dict[str, str] | None) = None
)
</code></pre>

Builds a `CallableFunctionDeclaration` from a python function.

The function should have type annotations.

This method is able to generate the schema for arguments annotated with types:

`AllowedTypes = float | int | str | list[AllowedTypes] | dict`

This method does not yet build a schema for `TypedDict`, that would allow you to specify the dictionary
contents. But you can build these manually.

<h3 id="from_proto"><code>from_proto</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L574-L578">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_proto(
    proto
) -> FunctionDeclaration
</code></pre>




<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L580-L581">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto() -> protos.FunctionDeclaration
</code></pre>




<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L626-L630">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    fc: protos.FunctionCall
) -> protos.FunctionResponse
</code></pre>

Call self as a function.




