---
name: update-docs
description: Update README.md and the files under docs/ (EASY.md, MEDIUM.md, HARD.md) to reflect the current uncommitted changes (newly added, migrated, renamed or removed problems). Use when the user runs /update-docs or asks to sync the README/docs with their uncommitted changes.
---

# update-docs

Sync `README.md` and `docs/*.md` with the problems added, removed or renamed in the **uncommitted** changes (staged + unstaged + untracked).

## Steps

1. **Find the uncommitted changes.**
   - Run `git status --porcelain` (include untracked files) and `git diff HEAD --name-status`.
   - Only care about problem directories matching `problems/{easy,medium,hard}/<name>_<number>/`. Ignore changes to other files (tests/, utils/, docs/, README.md itself, `__pycache__`).
   - Classify each affected problem directory:
     - **Added**: `solution.py` is new (status `A` / `??`) and the directory is not yet listed in `docs/`.
     - **Removed**: the directory (or its `solution.py`) is deleted.
     - **Renamed/moved**: the directory moved (e.g. changed difficulty or name); treat as remove old + add new.
     - **Modified only**: a content change to an already-listed problem needs no docs change. Skip it.
   - Legacy files deleted from the old structure (e.g. `Hash Table/2351. First Letter to Appear Twice.py`) are part of a migration; they don't have their own docs row, so ignore them.
   - If there are no relevant problem changes, say so and stop without editing anything.

2. **Gather the facts for each added problem.**
   - Difficulty: from the parent directory (`easy` / `medium` / `hard`).
   - Number: the trailing `_<number>` of the directory name.
   - Slug: **derive it from the directory name**:
     1. strip the trailing problem number (`_2258`)
     2. replace underscores with hyphens
     3. lowercase everything

     | Directory | Slug |
     |-----------|------|
     | `escape_the_spreading_fire_2258` | `escape-the-spreading-fire` |
     | `first_letter_to_appear_twice_2351` | `first-letter-to-appear-twice` |
     | `binary_search_704` | `binary-search` |
   - Title: the official LeetCode title for that problem number (e.g. "Escape the Spreading Fire"), used as the link text. Take it from the search results that confirm the link (step 3). Never guess it.
   - Confirm that both `solution.py` and `test_solution.py` exist in the directory; link only the files that exist.

3. **Verify every new link.** The directory name is not guaranteed to match LeetCode's real slug: names may be abbreviated, and LeetCode drops apostrophes instead of turning them into separators (the real slug of "Check if All A's Appears Before All B's" is `check-if-all-as-appears-before-all-bs`, while the directory `check_if_all_a_s_appears_before_all_b_s_2124` would give `check-if-all-a-s-appears-before-all-b-s`). So always confirm:
   - Do not fetch leetcode.com directly: it blocks WebFetch with HTTP 403. Use WebSearch instead (load it via ToolSearch `select:WebSearch` if needed), with a query like `leetcode <number> <title or directory words>`.
   - In the results, look for a `leetcode.com/problems/<slug>/` URL whose problem number and title match, and use the slug from that URL. If it differs from the directory-derived slug, the search result wins.
   - Take the official title (the link text) from the same results.
   - If the search results do not show a matching `leetcode.com/problems/...` URL, do not guess: ask the user for the correct link, or add the row with the directory-derived slug and clearly flag it as **unverified** in the final report.
   - Include the confirming leetcode.com URL as a source link in the final report.

4. **Update `docs/<DIFFICULTY>.md`** (`EASY.md`, `MEDIUM.md`, `HARD.md`). Read the file first and follow its exact format:
   - Add one table row per added problem, **sorted ascending by problem number**, in this format (paths are relative to `docs/`; `<dir>` is the real directory name, `<slug>` is the verified slug):

     ```
     | <number> | [<Title>](https://leetcode.com/problems/<slug>/) | [solution.py](../problems/<difficulty>/<dir>/solution.py) | [test_solution.py](../problems/<difficulty>/<dir>/test_solution.py) |
     ```
   - Remove rows for removed problems (and for the old location of a moved one).
   - Update the `Total: N problem(s) solved` line to the new row count. Use "problem" when N is 1 and "problems" otherwise.
   - Do not touch the footer (`---` and the "Back to Main README" link) or any other row.

5. **Update `README.md`.**
   - Recompute the counts from the **actual table rows** in `docs/EASY.md`, `docs/MEDIUM.md` and `docs/HARD.md` (after step 4), not by incrementing the old numbers.
   - Update the `📊 **Statistics**: N problems solved (migrated to new structure)` line (N = easy + medium + hard) and the Easy / Medium / Hard counts in the statistics table, keeping the existing column alignment.
   - Only change other README sections (features, project structure, migration status) if the uncommitted changes actually invalidate them; otherwise leave them alone.

6. **Check consistency.**
   - For each docs file, check that the `Total:` number equals the number of table rows, rows are sorted by number with no duplicates, and every linked `solution.py` / `test_solution.py` path exists on disk.
   - Check that the README numbers match the docs files.

7. **Report** what changed: which problems were added/removed, the new totals, how each new LeetCode link was verified (and whether the slug had to be corrected from the directory-derived one), and anything unverified or uncertain. Do not commit; leave the changes in the working tree for the user to review.

## Rules

- Only edit `README.md` and files under `docs/`. Never modify solutions or tests.
- Match the existing Markdown style exactly (emoji, table format, pluralization, trailing newline).
- Never guess LeetCode titles or links; verify or ask.
- Be idempotent: running the skill twice in a row must not add duplicate rows or change counts a second time.
