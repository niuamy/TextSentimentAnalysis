# TextSentimentAnalysis

## Objective
Using https://api-ninjas.com/, the objective of this project is to take a given sentence and convert it into a less a negative version.

## How it's done
Given a piece of text, it uses sentiment analysis to determine a negativity score of a given word.
It then uses a thesaurus api to find a synonym of this word and uses sentiment analysis to determine the least negative synonym of this word.
Finally, it prints out the original and new text.

## Additional details
The goal is not to change the meaning of the text itself but simply to convert the text into a less negative version.
