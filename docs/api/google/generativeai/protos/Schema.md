description: The Schema object allows the definition of input and output data types.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Schema" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="PropertiesEntry"/>
</div>

# google.generativeai.protos.Schema

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L571-L649">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The ``Schema`` object allows the definition of input and output data types.

<!-- Placeholder for "Used in" -->
 These types can be objects, but also primitives and arrays.
Represents a select subset of an `OpenAPI 3.0 schema
object <https://spec.openapis.org/oas/v3.0.3#schema>`__.





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`type_`<a id="type_"></a>
</td>
<td>
`google.ai.generativelanguage.Type`

Required. Data type.
</td>
</tr><tr>
<td>
`format_`<a id="format_"></a>
</td>
<td>
`str`

Optional. The format of the data. This is
used only for primitive datatypes. Supported
formats:

 for NUMBER type: float, double
 for INTEGER type: int32, int64
</td>
</tr><tr>
<td>
`description`<a id="description"></a>
</td>
<td>
`str`

Optional. A brief description of the
parameter. This could contain examples of use.
Parameter description may be formatted as
Markdown.
</td>
</tr><tr>
<td>
`nullable`<a id="nullable"></a>
</td>
<td>
`bool`

Optional. Indicates if the value may be null.
</td>
</tr><tr>
<td>
`enum`<a id="enum"></a>
</td>
<td>
`MutableSequence[str]`

Optional. Possible values of the element of Type.STRING with
enum format. For example we can define an Enum Direction as
: {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH",
"WEST"]}
</td>
</tr><tr>
<td>
`items`<a id="items"></a>
</td>
<td>
`google.ai.generativelanguage.Schema`

Optional. Schema of the elements of
Type.ARRAY.

</td>
</tr><tr>
<td>
`properties`<a id="properties"></a>
</td>
<td>
`MutableMapping[str, google.ai.generativelanguage.Schema]`

Optional. Properties of Type.OBJECT.
</td>
</tr><tr>
<td>
`required`<a id="required"></a>
</td>
<td>
`MutableSequence[str]`

Optional. Required properties of Type.OBJECT.
</td>
</tr>
</table>



## Child Classes
[`class PropertiesEntry`](../../../google/generativeai/protos/Schema/PropertiesEntry.md)

