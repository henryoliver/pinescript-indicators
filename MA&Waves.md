# MA&Waves

## Purpose
Define the concepts and rules for the MAs & Waves indicator so the Pine implementation can be rebuilt cleanly.

## Core Concepts
- Trend: Determined by SMA slope over a lookback; classifies current market direction.
- Cycle: A full cycle is HIGH→LOW→HIGH or LOW→HIGH→LOW.
- Half-cycle: A single transition HIGH→LOW or LOW→HIGH.
- Wave: A label placed at half-cycle transitions.
- Odd Wave = Impulse Wave: Must progress beyond the prior impulse in the trend direction.
- Even Wave = Retrace Wave: No progression rule relative to prior retrace.

## High-Level Rules
- Wave labels are placed only on confirmed bars.
- Impulse validation uses the body direction rules (open/close vs previous impulse) as currently defined.
- Retrace waves are selected from the preceding half-cycle without progression constraints.
- When trend changes during a half-cycle, wave classification must align to the new trend.

## Open Questions
- Should impulse validation use body-only, wick-only, or mixed rules?
- Should retrace waves be the most extreme point or first qualifying point?
- How many historical labels should be retained on chart?
