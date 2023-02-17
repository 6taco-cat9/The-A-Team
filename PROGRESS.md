# The-A-Team's Element Wordle
description: daily wordle with words resulted from concatenating elements' abbreviations

### Day 1 -

Project overview - flow chart
<img width="1045" alt="Screen Shot 2023-02-13 at 22 20 49" src="https://user-images.githubusercontent.com/125279934/218599047-06c3eea8-75af-4f82-b1b3-8268f2a5720b.png">

### Day 2 -

Initiate the list. Recording each data to word and list.
<img width="1440" alt="Screen Shot 2023-02-15 at 01 16 56" src="https://user-images.githubusercontent.com/125279934/219540363-33491304-083a-41fd-afd5-ec3021613231.png">
*what I learned: list comprehension, recall how to record, ‘enumerate’ method*

### Day 3 -

Separate each format type to see if wordle is possible.
<img width="1440" alt="Screen Shot 2023-02-15 at 22 21 08" src="https://user-images.githubusercontent.com/125279934/219540650-1c5d5567-5883-4ff5-bc77-c5304dff1d29.png">
Come to conclusion to separate into 2 moods: wordle, and challenge (1 attempt if format count is 1)
<img width="1437" alt="Screen Shot 2023-02-17 at 01 39 28" src="https://user-images.githubusercontent.com/125279934/219540766-26db9f4a-42b6-413c-913d-7c1b1e3ce4bd.png">
Come up with the mentioned wordle algorithm in the flowchart
<img width="1440" alt="Screen Shot 2023-02-17 at 00 09 15" src="https://user-images.githubusercontent.com/125279934/219540862-56c618e9-4e2a-42a1-b7d6-1da2b74c96df.png">
steps(Ge Ni U S, Fe Ti S H, list, 0) returns 2 (example case in flowchart)

*what I learned: list is mutable in python, practice recursion*

### Day 4 -

revise the steps function from day 3 → realise green case is missing

e.g. steps(Po Li S H, Fe Ti S H, list, 0) returns 2 when it should’ve returned 1
<img width="1440" alt="Screen Shot 2023-02-17 at 01 57 56" src="https://user-images.githubusercontent.com/125279934/219541376-a6ba3d2b-3bbf-4562-bc2d-c8d0e14a3f82.png">
*what I learned: How ‘any’, ‘all’ methods work. One line if statement is possible in python:))*


