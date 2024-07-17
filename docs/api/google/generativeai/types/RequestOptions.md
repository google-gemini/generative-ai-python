description: Request options

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.RequestOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__contains__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="get"/>
<meta itemprop="property" content="items"/>
<meta itemprop="property" content="keys"/>
<meta itemprop="property" content="values"/>
</div>

# google.generativeai.types.RequestOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/helper_types.py#L35-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request options

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.RequestOptions(
    *,
    retry: (google.api_core.retry.Retry | None) = None,
    timeout: (int | float | google.api_core.timeout.TimeToDeadlineTimeout | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->


```
>>> import google.generativeai as genai
>>> from google.generativeai.types import RequestOptions
>>> from google.api_core import retry
>>>
>>> model = genai.GenerativeModel()
>>> response = model.generate_content('Hello',
...     request_options=RequestOptions(
...         retry=retry.Retry(initial=10, multiplier=2, maximum=60, timeout=300)))
>>> response = model.generate_content('Hello',
...     request_options=RequestOptions(timeout=600)))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`retry`<a id="retry"></a>
</td>
<td>
Refer to [retry docs](https://googleapis.dev/python/google-api-core/latest/retry.html) for details.
</td>
</tr><tr>
<td>
`timeout`<a id="timeout"></a>
</td>
<td>
In seconds (or provide a [TimeToDeadlineTimeout](https://googleapis.dev/python/google-api-core/latest/timeout.html) object).
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`retry`<a id="retry"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`timeout`<a id="timeout"></a>
</td>
<td>
Dataclass field
</td>
</tr>
</table>



## Methods

<h3 id="get"><code>get</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get(
    key, default=None
)
</code></pre>

D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.


<h3 id="items"><code>items</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>items()
</code></pre>

D.items() -> a set-like object providing a view on D's items


<h3 id="keys"><code>keys</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>keys()
</code></pre>

D.keys() -> a set-like object providing a view on D's keys


<h3 id="values"><code>values</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>values()
</code></pre>

D.values() -> an object providing a view on D's values


<h3 id="__contains__"><code>__contains__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__contains__(
    key
)
</code></pre>




<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/helper_types.py#L68-L77">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    item
)
</code></pre>




<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/helper_types.py#L79-L81">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/helper_types.py#L83-L84">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>






