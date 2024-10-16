
# google.generativeai.types.Tool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L703-L769">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A wrapper for <a href="../../../google/generativeai/protos/Tool.md"><code>protos.Tool</code></a>, Contains a collection of related `FunctionDeclaration` objects, protos.CodeExecution object, and protos.GoogleSearchRetrieval object.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.Tool(
    *,
    function_declarations: (Iterable[FunctionDeclarationType] | None) = None,
    google_search_retrieval: (GoogleSearchRetrievalType | None) = None,
    code_execution: (protos.CodeExecution | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`code_execution`<a id="code_execution"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`function_declarations`<a id="function_declarations"></a>

</td>
<td>



</td>
</tr><tr>
<td>

`google_search_retrieval`<a id="google_search_retrieval"></a>

</td>
<td>



</td>
</tr>
</table>



## Methods

<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L768-L769">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto()
</code></pre>




<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L761-L766">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    fc: protos.FunctionCall
) -> (protos.FunctionResponse | None)
</code></pre>

Call self as a function.


<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L753-L759">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    name: (str | protos.FunctionCall)
) -> (FunctionDeclaration | protos.FunctionDeclaration)
</code></pre>






