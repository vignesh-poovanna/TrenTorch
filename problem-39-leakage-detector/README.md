# Leakage Detector

Beginner | problemset | data-stats-for-ds | data-leakage

Flag feature columns whose names suggest data leakage. A column is suspicious when its lower-cased name contains any of the substrings `target`, `label`, `future`, `outcome` or `post_`.

Implement `solve(columns)`.

**Returns.** Return a list of the suspicious column names in their original order. Return an empty list when none match.

### Examples

**Example 1**

Input:

```python
solve(['age', 'income', 'target_encoded', 'future_balance', 'city'])
```

Output:

```text
['target_encoded', 'future_balance']
```

**Example 2**

Input:

```python
solve(['Age', 'Plan', 'tenure'])
```

Output:

```text
[]
```
