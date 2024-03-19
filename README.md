# AutomaticWordleSolver
Selenium script to automate solving the famous word game wordle 

## Tools

### Selenium
Selenium is an open source umbrella project for a range of tools and libraries aimed at supporting browser automation. [Wikipedia](https://en.wikipedia.org/wiki/Selenium_(software))

### Pandas
Pandas is a software library written for the Python programming language for data manipulation and analysis. [Wikipedia](https://en.wikipedia.org/wiki/Pandas_(software))


## Wordle
Wordle is a web-based word game created and developed by Welsh software engineer Josh Wardle, and owned and published by The New York Times Company since 2022.

In Wordle a random word of 5 letters is chosen and the player has to guess it in 6 tries, with every guess letters in the word the player chose are highlighted in one of three different colors: green, yellow, and gray. Green means the letter is in the word and is in its correct position. Yellow means the letter is in the word but not in its correct position. Gray means the letter is not in the word.

## Guessing Strategy
Available on the internet are a lot of wordle datasets that include all guessable words, using one of those datasets my program manages to narrow down the search space by initially trying a random word and seeing the result of the letters, it then follows by randomly choosing a word from the now smaller dataset.
