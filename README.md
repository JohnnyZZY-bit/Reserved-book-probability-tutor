# Reserved Book Probability Tutor

README prose word count: [count after final edits]

## Project status

This work prototype based on Streamlit guides learners to solve a conditional probability problem related to library book reservations. It checks the reservation quantity, sampling group, and final probability. If any information is missing, it will ask follow-up questions. For identifiable errors, learners can request more specific hints. This exercise uses fictional data and deterministic rules, and is accompanied by preset feedback. More exercises, free text reasoning, and learning outcome assessment remain future work.

## Technology and reuse

- Streamlit 1.52.2, Apache License 2.0, provides the interface,session state and AppTest. https://github.com/streamlit/streamlit
- Python 3.13.3 runs the application. The standard library provides exact fraction comparison and unit testing.
- ChatGPT supported development. The running app requires no AI model, API key or external database.

## Run or inspect

Use PowerShell from the repository root. Set $basePython to the path of a working Python 3.13 interpreter on your computer.

$labPython = "$env:APPDATA\uv\python\cpython-3.13.3-windows-x86_64-none\python.exe"
& $basePython -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" -m streamlit run app.py

Open the local address printed in the terminal. Check app.py to understand the interface, and view tutor.py to learn about the evaluation rules and feedback.


## Development record

| Change | Reason | What the walkthrough showed |
|---|---|---|
| Capture counts and sampling group alongside the fraction. | The fraction alone does not identify the learner's reasoning. | Entering 28 for Zone A prompted a count cue. Changing it to 12 and checking again prompted a request for the Zone B count. |
| Keep the fraction during clarification. | The learner can supply missing evidence without re-entering the answer. | Submitting only 2/5 prompted a question about the denominator. Choosing Zone A produced a cue about the direction of conditioning. With counts 12 and 14 and Reserved books from both zones selected, the same fraction prompted a cue about fraction construction. Submitting 6/13 then succeeded. |
| Reveal a table on request and label excluded groups. | Blank cells could look like missing data. The detailed hint should identify the eligible groups and leave the sum to the learner. | Selecting All 100 books produced a short cue. The expanded table showed 'Outside the draw' for unreserved books in both zones. |
| Diagnose the reset behaviour. | Previous checks revealed that there were still old inputs after resuming. | The suggestion of directly clearing the input values and feedback values has been made. After the improvement, the re-running function is working properly. |

## AI assistance

ChatGPT assisted in drafting the judgment rules, the wording of the prompts, and the test cases. I separated the clarified content from the optional prompts based on these suggestions, and replaced the blank table cells with explicit exclusion labels. I used the above attempts to check the feedback in the local browser. The screenshots record these checks. At the same time, I used AI to assist me in modifying the code.
