import os,sys
import numpy as np
from InputPipeline import DataReader
from singleTask import CNNSingle
from singleTask_att import CNNSingleAtt
from multiTask import CNNMulti
import tensorflow as tf


train_txt = "training.txt"
# train_txt = "aug_training.txt"

dataFolder = os.path.abspath(os.path.join("./", os.pardir)+"/MTFL")
data = DataReader(dataFolder, [train_txt, "validation.txt", "testing.txt"])

# network = CNNSingle(data, 50, -1) #batch size, landmark
# network = CNNSingleAtt(data, 50, 1) #batch size, attribute
# network = CNNMulti(data, 50) #batch size

# network.debug_network()
# sess = network.train_network(30, 1.0, True) # epochs, keep_prob
# network.test_network(sess)
# network.output_images(sess, "multi_es1_")

import sys
args = sys.arv
trial_nr = int(args[0])
network_type = int(args[1])
if network_type == 0:
  network = CNNSingle(data, 50, -1) #batch size, landmark
elif network_type == 1:
  network = CNNSingleAtt(data, 50, 1) #batch size, attribute
elif network_type == 2:
  network = CNNMulti(data, 50) #batch size
else:
  print("ERROR: INCORRECT NETWORK TYPE")

sess = network.train_network(1, 1.0, False) # epochs, keep_prob
network.test_network(sess)
# network.output_images(sess, "multi_es"+str(trial_nr)+"_")
sess.close()

# for i in range(1,4):
#   print("======= RUNNING NETWORK "+str(i)+" ========")
#   network = CNNMulti(data, 50)
#   sess = network.train_network(30, 1.0, False) # epochs, keep_prob
#   network.test_network(sess)
#   network.output_images(sess, "multi_es"+str(i)+"_")
#   sess.close()


# for i in range(1,4):
#   print("======= RUNNING NETWORK "+str(i)+" ========")
#   network = CNNSingle(data, 50, -1)
#   sess = network.train_network(30, 1.0)
#   network.test_network(sess)
#   network.output_images(sess, "single"+str(i)+"_")
#   sess.close()
