description: Tuned model as a source for training a new model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TunedModelSource" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.TunedModelSource

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/tuned_model.py#L198-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tuned model as a source for training a new model.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`tuned_model`<a id="tuned_model"></a>
</td>
<td>
`str`

Immutable. The name of the ``TunedModel`` to use as the
starting point for training the new model. Example:
``tunedModels/my-tuned-model``
</td>
</tr><tr>
<td>
`base_model`<a id="base_model"></a>
</td>
<td>
`str`

Output only. The name of the base ``Model`` this
``TunedModel`` was tuned from. Example:
``models/text-bison-001``
</td>
</tr>
</table>



