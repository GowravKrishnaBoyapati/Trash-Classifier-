# Trash Classifier

## Motivation for this Project
Being able to sort trash according to different materials is very important for recycling. However, sorting trash is one of the toughest tasks to do. While it is easy to sort metals and non-metals, it is very difficult to sort paper, glass, plastic and cardboard.

Currently, it is done by people. It is not a good job and such people are often at danger of being exposed to harmful chemicals, medical wastes and be exposed to diseases. If instead we can use a neural network that can do the classification then we can make the process faster, safer and more accurate.

This project attempts to use a convolutional neural network to do just that.

## Edge Computing
It is not always possible to run a machine learning model on a GPU as there can be cost and space restrictions. And always making an API call can have latencies and internet might not always be available.

In these cases using small, cheap devices at the edge (where the data is generated) is the best solution.

The problem with running models on the edge is that we are limited by the amount of computation power that we have. There are many ways to overcome this. You could use a hardware accelerator like a Neural Computer Stick. Or you could use some models that are built specifically to not be computationally expensive and run on the edge.

In this project we use the UP Embedded Vision Kit to run inference on the edge. We use the mobilenet model which is computationally less expensive.
