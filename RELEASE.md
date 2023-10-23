## v0.2.2

- Handle maximum batch size for `embed_text`.
- Restore `types.ModelNameOptions`.
- Update tuning to handle more dataset types (json, pandas, urls, google-sheets).
- Expose `count_text_tokens`
- Expose operations management.
- Allow users to pass custom `metadata` (HTML headers).
- Add dataclass prettyprinting.

## v0.2.1

- Bugfix: Add missing enum names to `saftey_types.py`
- Update to `google.ai.generativelanguage` v0.3.3 

## v0.2

- More flexible safety settings: 
  - accept strings, ints for enums.
  - accept a `{category:threshold}` dict in addition to the
    list of dicts format (`[{"category": category, "threshold": threshold}, ...]`).
- Add support for batched embeddings.
- Add support for tuning:
  - Add `get_{base,tuned}_model`.
  - Add `list_tuned_models`.
  - Add `create_tuned_model`.

## v0.1

Initial version
