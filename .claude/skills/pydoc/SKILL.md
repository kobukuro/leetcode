---
name: pydoc
description: Add English docstrings (with detailed time and space complexity analysis) to every function/method in a given Python file. Use when the user runs /pydoc <file> or asks to write pydoc/docstrings for a specific file.
argument-hint: <file path>
---

# pydoc

Write English docstrings for the functions in the file given as the argument (`$ARGUMENTS`).

## Steps

1. Resolve the file path (relative to the repo root if not absolute). If it does not exist or is not a `.py` file, tell the user and stop.
2. Read the whole file. Understand what each function does before writing.
3. For every function/method that does not already have a docstring (including helper/nested functions that contain real logic), add one using the format below. Skip `__init__.py` boilerplate and `test_*` functions in test files unless the user asks.
   - If a function already has a docstring, keep it unless it lacks complexity analysis; in that case, extend it rather than rewrite it.
4. Do not change any code, signatures, comments (such as `# Tags:` lines), or formatting outside the docstrings.
5. Run `python -m py_compile <file>` to confirm the file still parses. If a test file sits next to it, run it with `python -m pytest <test file> -q` as well.
6. Report briefly which functions were documented and the complexity stated for each.

## Docstring format

Place the docstring as the first statement inside the function body (PEP 257), using `"""` and matching the surrounding indentation. Follow the style already used in this repo:

```python
def are_occurrences_equal(self, s: str) -> bool:
    """
    Check whether every distinct character in s occurs the same number of times.

    Args:
        s: Input string.

    Returns:
        True if all characters have equal frequency, otherwise False.

    Time complexity: O(n)
    - n is the length of s, k is the number of distinct characters (k <= n)
    - Counter(s) scans the string once and each insertion/update is O(1)
      on average: O(n)
    - count_table.values() iterates over k counts: O(k)
    - set(...) hashes each of the k counts: O(k)
    - len(...) and the comparison with 1 are O(1)
    - Total: O(n) + O(k) + O(k) = O(n), since k <= n
    - Worst case: hash collisions could degrade dict operations, but this is
      not a practical concern for single characters

    Space complexity: O(k)
    - Counter stores one entry per distinct character: O(k)
    - The set of frequencies holds at most k values (usually far fewer): O(k)
    - No recursion, so no call stack overhead
    - Total auxiliary space: O(k); k is bounded by the alphabet size
      (e.g. 26 for lowercase letters), so it is O(1) if the alphabet is fixed
    """
```

Rules:
- Written in English. First line: a one-sentence summary in imperative mood.
- Include `Args:` and `Returns:` (and `Raises:` only if the code raises). Omit `Args:` for functions without parameters (other than `self`).
- **Always** include both `Time complexity:` and `Space complexity:` with Big-O.
- Make the complexity analysis detailed and step by step:
  - Define every variable first (n, m, k, h, ...) and any relationship between them (e.g. k <= n).
  - Break the cost down line by line / operation by operation (each loop, sort, hash lookup, slice, copy, string concatenation, built-in call such as `sorted`, `set`, `Counter`, `heapq`, `in` on list vs. set), then show how the parts sum to the final result and why lower-order terms are dropped.
  - Cover best / average / worst case when they differ (early return, hash collisions, unbalanced tree, quicksort-style pivots, amortized costs such as list append or dynamic resizing).
  - For loops, say how many iterations occur and the cost of each; for nested loops, multiply and explain why; for recursion, give the recurrence or the depth times the per-call work.
  - For space, separately account for: data structures built, recursion call stack depth, slices/copies created, and the output. State clearly whether the output is counted. Mention when space is bounded by a fixed alphabet or constraint (e.g. O(1) for 26 letters).
  - If a simpler or tighter bound exists under the problem constraints, mention it.
- Be accurate, not optimistic. Verify every claim against the actual code; don't copy complexity from the problem's editorial if the code differs.
- Don't restate the code line by line outside the complexity sections; keep summary, Args and Returns concise.
