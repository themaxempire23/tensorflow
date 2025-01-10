import tensorflow as tf

#Defining and running TensorFlow Opps

a = tf.constant(2)
b = tf.constant(3)

# Defining a TensorFlow operation to add two constants
add_op = tf.add(a, b)

# Starting a TensorFlow session
with tf.compat.v1.Session() as sess:
    # Run the TensorFlow operation to evaluate the result
    result = sess.run(add_op)
    print("Result:", result)