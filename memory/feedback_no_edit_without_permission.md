---
name: Don't edit code without explicit instruction
description: User wants analysis and advice reported as text, not applied as code changes, unless explicitly asked to make edits
type: feedback
---

Do not make code edits proactively when the user asks to "review" or "give advice." Report findings as text so the user can share with their engineer or decide what to action.

**Why:** User interrupted an edit session saying "just give me the advice." They want a report, not direct modification.

**How to apply:** When asked to review code and suggest improvements, always respond with a written findings list. Only apply code changes when the user explicitly says "make the changes," "fix it," "apply this," etc.
