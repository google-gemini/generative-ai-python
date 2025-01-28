
# google.generativeai.types.FunctionLibrary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L837-L871">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A container for a set of `Tool` objects, manages lookup and execution of their functions.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.FunctionLibrary(
    tools: Iterable[ToolType]
)
</code></pre>



<!-- Placeholder for "Used in" -->


## Methods

<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L870-L871">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto()
</code></pre>




<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L862-L868">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    fc: protos.FunctionCall
) -> (protos.Part | None)
</code></pre>

Call self as a function.


<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/content_types.py#L854-L860">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    name: (str | protos.FunctionCall)
) -> (FunctionDeclaration | protos.FunctionDeclaration)
</code></pre>






