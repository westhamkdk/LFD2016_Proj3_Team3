__author__ = 'insookyo'

import tensorflow as tf
import numpy as np
import os
from change import DataLoader

# Create model
class CNN(object):
    def __init__(self, sess, learning_rate, training_iters, batch_size, display_step, n_input, n_classes, model_type):
        self.sess = sess
        self.learning_rate = learning_rate
        self.training_iters = training_iters
        self.batch_size = batch_size
        self.display_step = display_step
        self.n_input = n_input
        self.n_classes = n_classes
        self.model_type = model_type
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

        # Fully connected layer
        self.dense1 = tf.reshape(self.conv3, [-1, self.wd1.get_shape().as_list()[0]]) # Reshape conv2 output to fit dense layer input
        self.dense1 = tf.nn.tanh(tf.add(tf.matmul(self.dense1, self.wd1), self.bd1)) # Relu activation

        # Output, class prediction
        out = tf.add(tf.matmul(self.dense1, self.out), self.bout)

        if self.model_type == "regression":
            out = tf.add(tf.matmul(tf.nn.tanh(out), self.regout), self.bregout)

        return out

    def build_graph(self):
        filter_size =[16, 32, 64]
        fc_size = 1024


        # tf Graph input
        self.x = tf.placeholder(tf.float32, [None, 15, 15, 1])
        if self.model_type == "regression":
            self.y = tf.placeholder(tf.float32, [None, 1])
        else:
            self.y = tf.placeholder(tf.float32, [None, self.n_classes])

        # Store layers weight & bias
        self.wc1 = tf.Variable(tf.random_normal([5, 5, 1, filter_size[0]]), name='wc1') # 5x5 conv, 1 input, 32 outputs
        self.wc2 = tf.Variable(tf.random_normal([5, 5, filter_size[0], filter_size[1]]), name='wc2') # 5x5 conv, 32 inputs, 64 outputs
        self.wc3 = tf.Variable(tf.random_normal([5, 5, filter_size[1], filter_size[2]]), name='wc3') # 5x5 conv, 32 inputs, 64 outputs

        self.wd1 = tf.Variable(tf.random_normal([15*15*filter_size[-1], fc_size]), name='wd1') # fully connected, 7*7*64 inputs, 1024 outputs
        self.out = tf.Variable(tf.random_normal([fc_size, self.n_classes]), name='out') # 1024 inputs, 10 outputs (class prediction)

        if self.model_type == 'regression':
            self.regout = tf.Variable(tf.random_normal([self.n_classes, 1]), name='regout')


        self.bc1 = tf.Variable(tf.random_normal([filter_size[0]]), name='bc1')
        self.bc2 = tf.Variable(tf.random_normal([filter_size[1]]), name='bc2')
        self.bc3 = tf.Variable(tf.random_normal([filter_size[2]]), name='bc3')

        self.bd1 = tf.Variable(tf.random_normal([fc_size]), name='bd1')
        self.bout = tf.Variable(tf.random_normal([self.n_classes]), name='bout')

        if self.model_type == "regression":
            self.bregout = tf.Variable(tf.random_normal([1]), name='bregout')

        # Construct model
        self.pred = self.conv_net()

        # Define loss and optimizer
        if self.model_type == "regression":
            self.cost = tf.reduce_mean(tf.pow(self.pred - self.y, 2))
        else:
            self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.pred, self.y))


    def train_classification(self):

        self.optimizer = tf.train.AdamOptimizer(learning_rate=self.learning_rate).minimize(self.cost)

        # Evaluate model
        correct_pred = tf.equal(tf.argmax(self.pred,1), tf.argmax(self.y,1))
        accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
        # Define Saver
        self.saver = tf.train.Saver()

        tf.initialize_all_variables().run()
        print "data is loading..."
        data_loader = DataLoader(self.model_type)
        print "data is loaded"

        epoch = 0
        step = 1
        # Keep training until reach max iterations
        while epoch < self.training_iters:
            batch_xs, batch_ys, epoch_over =  data_loader.generate_batch(self.batch_size)

            # Fit training using batch data
            self.sess.run(self.optimizer, feed_dict={self.x: batch_xs, self.y: batch_ys})
            if step % self.display_step == 0:
                print "step : %d " % step
                # Calculate batch accuracy and loss
                acc, loss = self.sess.run([accuracy, self.cost], feed_dict={self.x: batch_xs, self.y: batch_ys})
                print "epoch :", str(epoch+1), ", Minibatch Loss= " + "{:.6f}".format(loss) + ", Minibatch Accuracy= " + "{:.5f}".format(acc)
            step += 1
            if epoch_over is True:
                epoch +=1
                self.save(epoch)

        print "Optimization Finished!"


    def train_regression(self):
        self.optimizer = tf.train.AdamOptimizer(learning_rate=self.learning_rate).minimize(self.cost)

        # Define Saver
        self.saver = tf.train.Saver()

        tf.initialize_all_variables().run()
        tf.train.Saver([self.wc1, self.wc2, self.wc3, self.wd1, self.out, self.bc1, self.bc2, self.bc3, self.bd1, self.bout]).restore(sess, \
         save_path='assets/cnn_classification.model-1')
        print "data is loading..."
        data_loader = DataLoader(self.model_type)
        print "data is loaded"

        epoch = 0
        step = 1
        # Keep training until reach max iterations
        while epoch < self.training_iters:
            batch_xs, batch_ys, epoch_over = data_loader.generate_batch(self.batch_size)

            # Fit training using batch data
            self.sess.run(self.optimizer, feed_dict={self.x: batch_xs, self.y: batch_ys})
            if step % self.display_step == 0:
                print "step : %d" % step
                # Calculate batch accuracy and loss
                loss = self.sess.run(self.cost, feed_dict={self.x: batch_xs, self.y: batch_ys})
                print "epoch :" + str(epoch+1) + ", Minibatch Loss= " + "{:.6f}".format(loss)
            step += 1

            if epoch_over is True:
                epoch +=1
                self.save_reg(epoch)

        print "Optimization Finished!"


    def inference(self, x):
        y = np.zeros(shape=[x.shape[0], self.n_classes])

        # Define Saver
        self.saver = tf.train.Saver()

        if self.load() is True:
            print(" [*] Load SUCCESS")
        else:
            print(" [!] Load failed...")

        return self.sess.run(self.dense1, feed_dict={self.x: x, self.y: y, self.keep_prob: 1.})

    # def calculate_error(self):
    #     # Define Saver
    #     self.saver = tf.train.Saver()
    #
    #     if self.load() is True:
    #         print(" [*] Load SUCCESS")
    #     else:
    #         print(" [!] Load failed...")
    #
    #     # Evaluate model
    #     correct_pred = tf.equal(tf.argmax(self.pred,1), tf.argmax(self.y,1))
    #     accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    #
    #     train_dir = os.path.join(os.path.dirname(__file__), '../data', 'train')
    #     xs, ys = load_images(train_dir, mode="train", one_hot=True, resize_shape=resize_shape)
    #
    #     acc = self.sess.run(accuracy, feed_dict={self.x: xs, self.y: ys, self.keep_prob: 1.})
    #     print "accuracy : {:.5f}".format(acc)

    def save(self, step):
        """ """
        model_name ='cnn_%s.model' % self.model_type
        checkpoint_dir = os.path.join(os.path.dirname(__file__), 'assets')

        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)

        self.saver.save(self.sess, os.path.join(checkpoint_dir, model_name), global_step=step)

    def save_reg(self, step):
        """ """
        model_name = 'cnn_reg_%s.model' % self.model_type
        checkpoint_dir = os.path.join(os.path.dirname(__file__), 'assets')

        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)

        self.saver.save(self.sess, os.path.join(checkpoint_dir, model_name), global_step=step)


    def load(self):
        """ """
        print(" [*] Reading checkpoints...")

        checkpoint_dir = os.path.join(os.path.dirname(__file__), 'assets')

        ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
        if ckpt and ckpt.model_checkpoint_path:
            ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
            self.saver.restore(self.sess, os.path.join(checkpoint_dir, ckpt_name))
            return True
        else:
            return False

if __name__ == '__main__':
    import time
    # Parameters
    learning_rate = 0.0015
    training_iters = 100
    batch_size = 128
    display_step = 50

    # Network Parameters
    n_input = 15*15 # MNIST data input (img shape: 28*28)
    n_classes = 225 # MNIST total classes (0-9 digits)

    is_train = True
    model_type = "classification"
#    model_type = "regression"


    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)

    if model_type =="classification":
        with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
            #        with tf.Session() as sess:
            cnn = CNN(sess, learning_rate, training_iters, batch_size, display_step, n_input, n_classes, model_type=model_type)

            if is_train is True:
                start_time = time.time()
                cnn.train_classification()
                print("--- %s seconds ---" % (time.time() - start_time))
                print("--- %s min ---" % ((time.time() - start_time)/float(60)))
            else:
                cnn.calculate_error()
    else:
        with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
            cnn = CNN(sess, learning_rate, training_iters, batch_size, display_step, n_input, n_classes,
                      model_type=model_type)

            if is_train is True:
                start_time = time.time()
                cnn.train_regression()
                print("--- %s seconds ---" % (time.time() - start_time))
                print("--- %s min ---" % ((time.time() - start_time) / float(60)))
            else:
                cnn.calculate_error()
