# Reserved Book Probability Tutor

README prose word count: [count after final edits]

## Project status

A single-exercise prototype for learning conditional probability. It
checks reservation counts, the selected sampling group and the final
fraction. Missing evidence prompts clarification. An identified issue
can lead to a second hint on request. The exercise uses fictional data
and local authored rules. Source and tests are provided. Execution
and manual replay results should be recorded below.

## Technology and reuse

- Streamlit 1.52.2, Apache License 2.0, provides the interface,
  session state and AppTest. https://github.com/streamlit/streamlit
- The Python standard library provides fraction comparison, input
  checking and testing.
- The library exercise, feedback text and decision rules were authored
  for this project with ChatGPT assistance. The app needs no API key.

## Run or inspect

From the project directory, using Python 3.12:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
python -m unittest discover -s tests -v
```

See [storyboards and verification](docs/storyboard_and_verification.md)
for three replay paths and their expected outcomes.

## Development record

| Decision | Reason | Verification |
|---|---|---|
| Ask for the sampling group after a fraction-only submission | The fraction alone leaves the choice of denominator unclear | Replay storyboard C and record the actual result |
| Reveal the table on demand | The learner can first act on a short cue | Replay storyboard B and record when the table appears |
| Invalidate feedback after editing | The last hint may no longer match the revised attempt | Edit the selected group after opening the table |
| Preserve other inputs during clarification | The learner can supply Time demand minimal missing evidence in one action | Check that 2/5 survives the clarification sequence |

## AI assistance

ChatGPT helped draft the rules, interface, test cases, storyboards and
report. The draft was checked for consistency between the arithmetic,
feedback policy and storyboard cases. Add the checks you personally
perform, what you change and the final results before submission.

## Additional materials

The English project report accompanies the repository. Its repository
section identifies the submitted version and links to this README.