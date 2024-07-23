description: The base structured datatype containing multi-part content of a message.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Content" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Content

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L76-L103">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The base structured datatype containing multi-part content of a message.

<!-- Placeholder for "Used in" -->

A ``Content`` includes a ``role`` field designating the producer of
the ``Content`` and a ``parts`` field containing multi-part data
that contains the content of the message turn.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`parts`<a id="parts"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Part]`

Ordered ``Parts`` that constitute a single message. Parts
may have different MIME types.
</td>
</tr><tr>
<td>
`role`<a id="role"></a>
</td>
<td>
`str`

Optional. The producer of the content. Must
be either 'user' or 'model'.
Useful to set for multi-turn conversations,
otherwise can be left blank or unset.
</td>
</tr>
</table>



