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

## Improvements
 - To cut down the words in the dataset regular expressions were used, however, the efficiency of the implementation is poor and can definitely be improved
 - If a yellow letter is shown in a certain position it means that that letter will never be in said position, that is not taken into consideration by my algorithm and needs to be changed
 - Choosing the words randomly is not a good strategy and can be improved by taking word frequency into account
 - If a word that doesn't exist in Wordle's word pool is chosen an invalid message will show up to the player, my script doesn't recognize that and will keep running without deleting the invalid word, even if the word was deleted manually the script will not decrement the number of tries (6) counter, meaning if it makes one mistake it will stop at 5 tries, leaving one more try. 
