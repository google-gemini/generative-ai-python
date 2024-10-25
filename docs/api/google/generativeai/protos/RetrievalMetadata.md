
# google.generativeai.protos.RetrievalMetadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L938-L955">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Metadata related to retrieval in the grounding flow.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`google_search_dynamic_retrieval_score`<a id="google_search_dynamic_retrieval_score"></a>

</td>
<td>

`float`

Optional. Score indicating how likely information from
google search could help answer the prompt. The score is in
the range [0, 1], where 0 is the least likely and 1 is the
most likely. This score is only populated when google search
grounding and dynamic retrieval is enabled. It will be
compared to the threshold to determine whether to trigger
google search.

</td>
</tr>
</table>



