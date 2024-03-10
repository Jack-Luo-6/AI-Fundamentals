# AI-Fundamentals

This program uses the mathematical foundations of AI to create a trainable neural network, which means that it doesn't use PyTorch or TensorFlow to create a trainable neural network. It breaks down the process into matrix creation, matrix multiplication, forward and backward propagation, and evaluation. 

For matrix creation, a dynamic matrix with dimentions coherent with the neural network with randomly created numbers from 1 to -1 is created. For matrix multiplication, the values are multiplied in a loop structure, which serves the purpose of y = W * x + b for each neuron in the neural network. For forward and backward propagation, the loss function and activation function is calculated by hand. For evaluation, a final value of proximity with the actual value is printed. 
