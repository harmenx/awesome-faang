# Contribution Guidelines

Contributions are welcome. This list is a curation of strong resources for software engineering interviews at large technology companies, not a catalog of everything that exists.

## Adding a resource

- Search existing entries, including the guide pages, before suggesting a new one.
- Submit one resource per pull request.
- Add the entry at the bottom of the matching section in `README.md`.
- Use this format: `- [Name](https://example.com) - Description.`
- Start the description with an uppercase letter and end it with a period.
- Do not start the description with the name of the resource.
- Use the canonical URL, without a trailing slash, and check that it loads.
- Include a resource only when it is actively maintained, documented, and useful for coding, system design, behavioral, or company-specific interview preparation.
- Skip archived projects, dead links, and unmaintained material.
- Keep spelling and grammar consistent.
- Avoid details that change often, such as prices or the exact number of rounds. Link the page that states them instead.
- If you add a new section, add it to Contents with the same wording as the heading, and open it with a short note on when that stage of preparation matters.
- Say in the pull request if you are affiliated with the resource.

If you would rather not edit the readme yourself, use the **Suggest a resource** or **Report a problem** issue form.

## Checks

Every pull request runs [awesome-lint](https://github.com/sindresorhus/awesome-lint), a link check across all Markdown files, and every code example in the guides. Fix anything they report before asking for a review. A scheduled link check also runs every Monday and opens an issue when a link breaks.

## Guides

The pages in `guides/` are original, practical writing that goes with the list. Improvements are welcome: corrections, clearer explanations, better practice problems, or a missing pattern.

- Keep the plain, direct style of the existing pages.
- Every Python code block must run on its own and prove itself with `assert` statements. Run `python3 scripts/check_code_blocks.py` before opening a pull request.
- Link practice problems as `[Number. Title](https://leetcode.com/problems/slug/)` and avoid premium problems unless marked.
- Do not turn a guide into a second copy of the main list. Link to the list instead.

## Checks

Every pull request runs [awesome-lint](https://github.com/sindresorhus/awesome-lint), a link check across all Markdown files, and every code example in the guides. Fix anything they report before asking for a review. A scheduled link check also runs every Monday and opens an issue when a link breaks.

## Guide pages

`ALGORITHMS.md`, `DATA_STRUCTURES.md`, `DSA_PATTERNS.md`, `CODING_PATTERNS.md`, `SYSTEM_DESIGN.md`, `BEHAVIORAL.md`, `REAL_INTERVIEW_QUESTIONS.md`, `COMPANY_BREAKDOWN.md`, and `COMMON_MISTAKES.md` are longer notes kept beside the list. Fixes for dead links and factual errors belong there. Do not turn those pages into a second copy of the main list.

Thank you for your suggestions.
