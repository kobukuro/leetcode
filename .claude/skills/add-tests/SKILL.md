---
name: add-tests
description: Write the LeetCode website's example test cases into a given test file (e.g. problems/easy/<name>_<number>/test_solution.py), following this repo's test conventions (BaseTestSolution + parametrize + timeout). Use when the user runs /add-tests <file> or asks to add the LeetCode examples as tests for a specific problem file.
argument-hint: <test_solution.py path, or the problem directory>
---

# add-tests

Write the official LeetCode example test cases into the test file given as the argument (`$ARGUMENTS`).

## Steps

1. **Resolve the target.**
   - Resolve the path relative to the repo root if not absolute. If the argument is a problem directory, use its `test_solution.py`; if the argument is `solution.py`, use the sibling `test_solution.py`.
   - The directory must match `problems/{easy,medium,hard}/<snake_case_name>_<number>/` and contain `solution.py`. If not, tell the user and stop (legacy flat files such as `Array/15. 3Sum.py` are not supported; they must be migrated first).
   - If `test_solution.py` already exists with tests, read it and only add examples that are missing; never delete or rewrite existing cases.

2. **Read `solution.py`.** Note the class name, every public method (some problems have several approaches, e.g. `climb_stairs_memoization` / `climb_stairs_dp`), the parameter names/types and the `# Tags:` line. Also read the `utils/data_structures.py` helpers if the signature uses `TreeNode`, `ListNode` or `Node`.

3. **Fetch the examples from LeetCode.**
   - The problem number is the trailing `_<number>` of the directory name. Derive the slug as in `update-docs` (strip the number, `_` -> `-`, lowercase) and confirm it with WebSearch (`leetcode <number> <title words>`); load WebSearch/WebFetch via ToolSearch `select:WebSearch,WebFetch` if needed.
   - leetcode.com blocks WebFetch with HTTP 403, so get the statement from WebSearch results or a mirror/solution page that quotes the official "Example N" blocks. Verify that the problem number and title match before using anything.
   - Copy the inputs/outputs exactly as the statement shows them. Never invent examples and never guess an expected value. If the examples cannot be found reliably, tell the user and stop.
   - Also note the **Constraints** section; it decides whether a timeout is needed (step 5).

4. **Choose the test style (follow the repo, don't invent).**

   **Style A: `BaseTestSolution` + parametrize (default, used for plain value-in/value-out problems).**

   ```python
   import pytest
   from tests.base_test import BaseTestSolution
   from .solution import Solution


   class TestSolution(BaseTestSolution):
       solution = Solution()

       @pytest.mark.parametrize("method_name, nums, target, expected, timeout", [
           ('search', [-1, 0, 3, 5, 9, 12], 9, 4, None),
           ('search', [-1, 0, 3, 5, 9, 12], 2, -1, None),
       ])
       def test_search(self, method_name, nums, target, expected, timeout):
           self._run_test(self.solution, method_name, (nums, target,), expected, timeout)
   ```

   Rules:
   - Parametrize names are `"method_name, <the solution's parameter names>, expected, timeout"`; the test function is `test_<main_method_name>` and passes the arguments as a tuple to `self._run_test(self.solution, method_name, (<args>,), expected, timeout)`.
   - One tuple per LeetCode example, in order. Python values: `True/False/None`, lists, strings with double quotes for inputs when the statement quotes them. Keep the existing quote style of neighbouring files (method names in single quotes).
   - If `solution.py` has several approach methods for the same problem, repeat every example for every method (group by method, like `climbing_stairs_70`).
   - Wrap a long argument list over multiple lines only when needed for readability.

   **Style B: plain class with `setup_method` (used when the input/output is a data structure or the result isn't directly `==`-comparable).** Use this when the signature involves `TreeNode`, `ListNode`, `Node`, a class-design problem, or several valid answers.
   - Plain `class TestSolution:` with `def setup_method(self): self.solution = Solution()`, one `test_example_<n>` method per example, no timeout (the repo does not use timeouts in this style).
   - Trees/lists: build with `from utils.data_structures import TreeNode, ListNode`, and put the LeetCode form in a comment above (e.g. `# root = [1,null,2,3]`). See `problems/easy/binary_tree_inorder_traversal_94/test_solution.py` and `reverse_linked_list_206/test_solution.py`.
   - Multiple valid answers: assert membership (`assert result in (expected1, expected2)`), see `two_sum_1`.
   - Class-design problems (e.g. `ParkingSystem`): use a `call(self, methods, params, expected)` helper and put the full LeetCode example in the docstring, see `design_parking_system_1603`.
   - If a file already exists in a given style, keep that style.

5. **Timeout (only when needed, per repo convention).**
   - The `timeout` column is **always present** in Style A. Use `None` by default (no time limit, runs in-process).
   - Use `BaseTestSolution.DEFAULT_TIMEOUT` (1 second; do not hard-code a number) only for cases where the constraints make a naive/slow approach unacceptable, e.g. a large `n` that forces memoization/DP over brute force (`climb_stairs` with `n = 38`), or heavy input on a hard problem. Apply it to the large/performance-sensitive example(s) for the efficient method(s) only.
   - Otherwise, small LeetCode examples get `None`. Do not add a timeout "just in case".
   - Some existing files use `DEFAULT_TIMEOUT` for every case of an efficient solution (e.g. `unique_number_of_occurrences_1207`, `escape_the_spreading_fire_2258`). If the user says to use the timeout for all cases, do that; otherwise default to `None` for small examples.
   - If a timeout case is used, tell the user which cases got it and why.

6. **Write the file.** Create or edit `test_solution.py` with the cases. Make sure `__init__.py` exists in the problem directory (the repo needs it for the relative `.solution` import); create an empty one if missing. Do not modify `solution.py`.

7. **Run the tests.** Pick the interpreter first: if the repo root has a virtual environment (`.venv/` or `venv/`, with `Scripts/python.exe` on Windows or `bin/python` elsewhere), run with that interpreter, e.g. `.venv/Scripts/python.exe -m pytest <test file> -q` (run from the repo root so `utils` and `tests` import). Only if no virtual environment exists, fall back to the system `python -m pytest <test file> -q`. If a case fails:
   - Re-check that the example was copied correctly from LeetCode first.
   - If the example is right and the solution is wrong, report it to the user; do not change the expected value to make it pass, and do not edit `solution.py` unless asked.

8. **Report briefly:** the file written, how many examples (and for which methods), which style was used, which cases have a timeout and why, and the pytest result.
