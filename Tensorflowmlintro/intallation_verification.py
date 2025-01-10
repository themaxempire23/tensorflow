import tensorflow as tf

# Create a constant tensor
tensor = tf.constant("Hello, TensorFlow!, I'm alive!")

# Evaluate the tensor directly in eager mode
result = tensor.numpy().decode()
print(result)
