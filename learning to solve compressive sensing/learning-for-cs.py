import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


k = 10
n = 100
m = 30

idxArr = np.random.choice(n, k, replace=False)
valueArr = 10 * (np.random.rand(k) + 0.5)

hiddenArr = np.zeros((n,1))

for i in range(k):
    hiddenArr[idxArr[i]] = valueArr[i]

sensingMat = np.random.rand(m, n) - 0.5

sensingResult = np.dot(sensingMat, hiddenArr)

### y is the result, sensingMat is the sensing mat.

rng = np.random

# Parameters
learning_rate = 0.1
training_epochs = 100000
display_step = 100


# tf Graph Input
X = tf.placeholder("float64", shape=(None, n))
Y = tf.placeholder("float64", shape=(None, 1))

# Set model weights
w = tf.Variable(2 * np.random.rand(n, 1), name="weight")
g = tf.Variable(np.random.rand(1, n) - 0.5, name="gate")

pred = tf.matmul(tf.multiply (tf.nn.softmax(g) * k, X), w)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*m)
# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()
lossall = []
# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(sensingMat, sensingResult):
            sess.run(optimizer, feed_dict={X: x.reshape(1, n), Y: y.reshape(-1, 1)})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: sensingMat, Y:sensingResult})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c))
            lossall.append(np.log(c))

        if (epoch+1) % (display_step*10) == display_step*5:
            plt.plot(lossall)
            plt.pause(0.05)

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: sensingMat, Y: sensingResult})
    print("Training cost=", training_cost, "W=", sess.run(w), "b=", sess.run(tf.nn.softmax(g)), '\n')

plt.show()

print hiddenArr