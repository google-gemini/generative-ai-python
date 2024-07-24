description: A dataclass representation of a <a href="../../../google/generativeai/protos/TunedModel.md"><code>protos.TunedModel</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.TunedModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="base_model"/>
<meta itemprop="property" content="create_time"/>
<meta itemprop="property" content="description"/>
<meta itemprop="property" content="display_name"/>
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="source_model"/>
<meta itemprop="property" content="state"/>
<meta itemprop="property" content="temperature"/>
<meta itemprop="property" content="top_k"/>
<meta itemprop="property" content="top_p"/>
<meta itemprop="property" content="tuning_task"/>
<meta itemprop="property" content="update_time"/>
</div>

# google.generativeai.types.TunedModel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/model_types.py#L181-L201">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A dataclass representation of a <a href="../../../google/generativeai/protos/TunedModel.md"><code>protos.TunedModel</code></a>.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.TunedModel(
    name: (str | None) = None,
    source_model: (str | None) = None,
    base_model: (str | None) = None,
    display_name: str = &#x27;&#x27;,
    description: str = &#x27;&#x27;,
    temperature: (float | None) = None,
    top_p: (float | None) = None,
    top_k: (float | None) = None,
    state: TunedModelState = TunedModelState.STATE_UNSPECIFIED,
    create_time: (datetime.datetime | None) = None,
    update_time: (datetime.datetime | None) = None,
    tuning_task: (TuningTask | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`permissions`<a id="permissions"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`source_model`<a id="source_model"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`base_model`<a id="base_model"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`description`<a id="description"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`top_k`<a id="top_k"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`state`<a id="state"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`create_time`<a id="create_time"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`update_time`<a id="update_time"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`tuning_task`<a id="tuning_task"></a>
</td>
<td>
Dataclass field
</td>
</tr>
</table>



## Methods

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
base_model<a id="base_model"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
create_time<a id="create_time"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
description<a id="description"></a>
</td>
<td>
`''`
</td>
</tr><tr>
<td>
display_name<a id="display_name"></a>
</td>
<td>
`''`
</td>
</tr><tr>
<td>
name<a id="name"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
source_model<a id="source_model"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
state<a id="state"></a>
</td>
<td>
`<State.STATE_UNSPECIFIED: 0>`
</td>
</tr><tr>
<td>
temperature<a id="temperature"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
top_k<a id="top_k"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
top_p<a id="top_p"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
tuning_task<a id="tuning_task"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
update_time<a id="update_time"></a>
</td>
<td>
`None`
</td>
</tr>
</table>

