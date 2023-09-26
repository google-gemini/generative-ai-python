
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