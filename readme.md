# Cellular Automaton
###### Brahm Capoor

This is a simple Cellular Automation, inspired by [this video](https://www.youtube.com/watch?v=bc-fVdbjAwk) by funfunfunction. After seeing it made in Javascript, I didn't think it was very fair to use Javascript, so I used Python instead.

---

### Details
* Uses numpy matrices to represent the state of the automaton's spacetime
* Uses matplotlib to plot and animate the automaton
* Uses [rule 18](http://atlas.wolfram.com/01/01/18/) from [Wolfram Atlas](http://atlas.wolfram.com/) to find the next state of the automaton (I'm going to implement the other rules as well, but hardcoding them would be a pain so I'm going to try and find an API or a procedural way to generate them.)

### Installation
1. Download or clone the repository
2. Make sure numpy and matplotlib are installed
3. Run

    python3 main.py

### Demo
![A demo of it in action](https://github.com/brahmcapoor/cellular-automata/blob/master/Demo.gif)
