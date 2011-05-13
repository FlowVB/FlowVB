import numpy as np
from numpy.random import multivariate_normal as rmvnorm

from flowvb import FlowVBAnalysis
from flowvb.core.flow_vb import Options
from flowvb.initialize import D2Initialiser

'''
Demo using synthetic data with a large and a small cluster
'''

np.random.seed(0)

mean = np.array([[0., -2.], [3., 3.]])
cov = np.array([[[2., 0.], [0., .2]], [[.2, 0], [0, .2]]])

n_obs = [2000, 100]

data = np.vstack([np.array(rmvnorm(mean[k, :], cov[k, :, :], n_obs[k]))
                  for k in range(mean.shape[0])])

num_comp_init = 6
init_params = D2Initialiser().initialise_parameters(data, num_comp_init)
options = Options(init_params)

options.plot_monitor = True

model = FlowVBAnalysis(data, options)
