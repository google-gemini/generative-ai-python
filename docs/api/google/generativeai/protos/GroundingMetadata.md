
# google.generativeai.protos.GroundingMetadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L958-L1002">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Metadata returned to client when grounding is enabled.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`search_entry_point`<a id="search_entry_point"></a>

</td>
<td>

`google.ai.generativelanguage.SearchEntryPoint`

Optional. Google search entry for the
following-up web searches.


</td>
</tr><tr>
<td>

`grounding_chunks`<a id="grounding_chunks"></a>

</td>
<td>

`MutableSequence[google.ai.generativelanguage.GroundingChunk]`

List of supporting references retrieved from
specified grounding source.

</td>
</tr><tr>
<td>

`grounding_supports`<a id="grounding_supports"></a>

</td>
<td>

`MutableSequence[google.ai.generativelanguage.GroundingSupport]`

List of grounding support.

</td>
</tr><tr>
<td>

`retrieval_metadata`<a id="retrieval_metadata"></a>

</td>
<td>

`google.ai.generativelanguage.RetrievalMetadata`

Metadata related to retrieval in the
grounding flow.


</td>
</tr>
</table>



