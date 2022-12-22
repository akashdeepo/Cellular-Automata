# Cellular-Automata
Implement Conway's Game of Life
This code is implementing the Game of Life, a cellular automaton invented by John Horton Conway in 1970. It is a zero-player game, meaning that once it is set up, it runs on its own according to a set of rules.

The Game of Life is played on a grid of cells, where each cell can be in one of two states: "on" or "off". The game follows a set of rules to determine the next state of each cell, based on the current state of the cell and the states of its eight neighbors (the cells that are horizontally, vertically, or diagonally adjacent to it).

The rules for the Game of Life are:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

FUTURE WORK
#TODO 
Use ML to Predict Future States
----------------------------------------------------%% Idea generated using ChatGPT %%--------------------------------------------------------------------------------

1. Collect a dataset of initial states and corresponding future states of the game. This dataset will be used to train the predictive model. You can generate this dataset by running the Game of Life simulation multiple times and storing the initial and final states of the game. Make sure to include a diverse range of initial states in the dataset to ensure that the model generalizes well.

2. Preprocess the data. You will need to convert the initial and final states of the game into a format that can be used as input and output to a machine learning model. One way to do this is to flatten the grid into a 1D array, where each element of the array corresponds to the state of a cell in the grid. You can then use the flattened initial state as the input to the model, and the flattened final state as the output.

3. Split the dataset into training and test sets. It is important to reserve some of the data for testing the model, to ensure that it generalizes well to unseen data. You can use the train_test_split function from the scikit-learn library to split the data into training and test sets.

4. Choose a machine learning model. There are many different types of machine learning models that you can use for this task. Some options include linear regression, support vector machines, decision trees, and neural networks. You will need to choose a model that is suitable for the type of data you are working with, and that can handle the complexity of the Game of Life.

5. Train the model. Once you have chosen a model, you can use the training data to fit the model to the data using the fit method. This will involve optimizing the model's parameters to minimize the error between the predicted and actual outputs.

6. Evaluate the model. After training the model, you can use the test data to evaluate its performance. You can use metrics such as accuracy, precision, and recall to assess the model's ability to correctly predict the future state of the game.

7. Fine-tune the model. If the model's performance is not satisfactory, you may need to fine-tune the model by adjusting its hyperparameters or using a different model altogether. You can use techniques such as cross-validation and grid search to find the best hyperparameter values.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
