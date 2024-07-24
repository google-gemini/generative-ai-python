<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.FunctionDeclaration" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_function"/>
<meta itemprop="property" content="from_proto"/>
<meta itemprop="property" content="to_proto"/>
</div>

# google.generativeai.types.FunctionDeclaration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L514-L561">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>





<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.FunctionDeclaration(
    *, name: str, description: str, parameters: (dict[str, Any] | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




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

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L542-L561">View source</a>

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

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L533-L537">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_proto(
    proto
) -> FunctionDeclaration
</code></pre>




<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L539-L540">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto() -> protos.FunctionDeclaration
</code></pre>






