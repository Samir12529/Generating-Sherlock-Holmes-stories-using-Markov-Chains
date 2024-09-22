# Sherlock Holmes Stories - Markov Chains
This project generates sherlock holmes stories using markov chains. To build the markov chain we need two things: set of states, transition probabilities.

## Code setup
1. *Importing libraries:* numpy / pandas / os / re / string / nltk / random.

2. *Collecting data from a kaggle dataset:* append each line of every text file into one list called "text".

3. *Cleaning "text":* convert to lower case, remove punctuation, and tokenize.

4. *Creating the markov model:* we need a nested dictionary to:
        Represent the state as key
        Represent **both** the transition **and** its probability as value. So the nested dictionary is the following: {state:{transition:transitionProbability}, ...}

5. *Generating the stories:* the model generates the story depending on the starting state.

## Result
Starting from the user provided initial word the model generates the story with **correct** grammatical structure and somewhat meaningful sentences.