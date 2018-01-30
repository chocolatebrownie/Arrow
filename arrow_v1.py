import numpy as np
import tensorflow as tf

def calcDist(w,g,v,a):
	
	t = np.square(v*np.sin(a))/(2*g)
	d = (v*np.cos(a) - w)*t
	return d

w = tf.random_gamma([1],2,1)
g = tf.random_normal([1],9.8,0.8)
d = tf.random_uniform([1],10,300)
precision = 1 

R = 0

# If the arrow lands 1m around the target, then its given points as abs(distance from
# center)

sess = tf.Session()

for i in xrange(iters):
	[w_i,g_i,d_i] = sess.run([w,g,d])
	v = 
	a = 
	d_a = calcDist(w_i,g_i,v,a)
	if np.absolute(d_i-d_a) < 1:
		R = np.absolute(d_i-d_a)
	else:
		R = 0


