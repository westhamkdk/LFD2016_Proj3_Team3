__author__ = 'insookyo'

import tensorflow as tf
import numpy as np
import os

# Create model
class CNN(object):

    def __init__(self, sess, learning_rate, training_iters, batch_size, display_step, n_input, n_classes):
        self.sess = sess
        self.learning_rate = learning_rate
        self.training_iters = training_iters
        self.batch_size = batch_size
        self.display_step = display_step
        self.n_input = n_input
        self.n_classes = n_classes
        print "graph is building..."
        self.build_graph()
        print "graph is built"

    def conv2d(self, img, w, b):
        return tf.nn.tanh(tf.nn.bias_add(tf.nn.conv2d(img, w, strides=[1, 1, 1, 1], padding='SAME'),b))

    def max_pool(self, img, k):
        return tf.nn.max_pool(img, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME')

    def conv_net(self):
        # Reshape input picture
        # self.x_4d = tf.reshape(self.x, shape=[-1, self.resize_shape, self.resize_shape, 1])
        # Convolution Layer
        self.conv1 = self.conv2d(self.x, self.wc1, self.bc1)
        # Max Pooling (down-sampling)
        # self.conv1 = self.max_pool(self.conv1, k=2)


        # Convolution Layer
        self.conv2 = self.conv2d(self.conv1, self.wc2, self.bc2)
        # Max Pooling (down-sampling)
        # self.conv2 = self.max_pool(self.conv2, k=2)

        self.conv3 = self.conv2d(self.conv2, self.wc3, self.bc3)
        self.conv4 = self.conv2d(self.conv3, self.wc4, self.bc4)
        self.conv4 = self.max_pool(self.conv4, k=2)


        # Fully connected layer
        self.dense1 = tf.reshape(self.conv4, [-1, self.wd1.get_shape().as_list()[0]]) # Reshape conv2 output to fit dense layer input
        self.dense1 = tf.nn.tanh(tf.add(tf.matmul(self.dense1, self.wd1), self.bd1)) # Relu activation

        # Output, class prediction
        out = tf.add(tf.matmul(self.dense1, self.out), self.bout)

        return out

    def build_graph(self):
        filter_size =[32, 64, 64, 128]
        fc_size = 1024

        # tf Graph input
        self.x = tf.placeholder(tf.float32, [None, 15, 15, 1])
        self.y = tf.placeholder(tf.float32, [None, self.n_classes])

        # Store layers weight & bias
        self.wc1 = tf.Variable(tf.truncated_normal([5, 5, 1, filter_size[0]]), name='wc1') # 5x5 conv, 1 input, 32 outputs
        self.wc2 = tf.Variable(tf.truncated_normal([5, 5, filter_size[0], filter_size[1]]), name='wc2') # 5x5 conv, 32 inputs, 64 outputs
        self.wc3 = tf.Variable(tf.truncated_normal([5, 5, filter_size[1], filter_size[2]]), name='wc3') # 5x5 conv, 32 inputs, 64 outputs
        self.wc4 = tf.Variable(tf.truncated_normal([5, 5, filter_size[2], filter_size[3]]), name='wc4')  # 5x5 conv, 32 inputs, 64 outputs

        self.wd1 = tf.Variable(tf.truncated_normal([8*8*filter_size[-1], fc_size]), name='wd1') # fully connected, 7*7*64 inputs, 1024 outputs
        self.out = tf.Variable(tf.truncated_normal([fc_size, self.n_classes]), name='out') # 1024 inputs, 10 outputs (class prediction)

        self.bc1 = tf.Variable(tf.constant(0.1, shape =[filter_size[0]]), name='bc1')
        self.bc2 = tf.Variable(tf.constant(0.1, shape =[filter_size[1]]), name='bc2')
        self.bc3 = tf.Variable(tf.constant(0.1, shape =[filter_size[2]]), name='bc3')
        self.bc4 = tf.Variable(tf.constant(0.1, shape =[filter_size[3]]), name='bc4')

        self.bd1 = tf.Variable(tf.constant(0.1, shape =[fc_size]), name='bd1')
        self.bout = tf.Variable(tf.constant(0.1, shape =[self.n_classes]), name='bout')

        # Construct model
        self.pred = self.conv_net()

        # Define loss and optimizer
        self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.pred, self.y))


    def inference(self, x, file_name):
        y = np.zeros(shape=[x.shape[0], 225])

        # Define Saver
        self.saver = tf.train.Saver()
        tf.initialize_all_variables().run()
        if self.load(file_name) is True:
            # print(" [*] Load SUCCESS")
            pass
        else:
            print(" [!] Load failed...")

        return self.sess.run(self.pred, feed_dict={self.x: x, self.y: y})


    def load(self, file_name):
        """ """
        # print(" [*] Reading checkpoints...")

        checkpoint_dir = os.path.join(os.path.dirname(__file__), 'assets')
        model_name = file_name
        try:
            self.saver.restore(self.sess, os.path.join(checkpoint_dir, model_name))
            return True
        except:
            return False