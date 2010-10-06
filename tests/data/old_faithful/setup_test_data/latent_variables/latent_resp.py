import numpy as np


# Input
num_features = 2

smm_dof = np.array([1.2229925934177996, 0.9826643925115144,
                    1.4869089126906136, 1.3288076795137300,
                    1.1632232859308667, 1.3175057718922212])

log_smm_mixweight = np.array([-1.6721413112654266, -3.6999710088630837,
                           -2.1376494304674489, -1.8989322242159465,
                           -1.2048610548948746, -1.5565226223711184])

log_det_precision = np.array([7.7276002040845810, 9.9261851701446968,
                              8.2755737065916559, 7.1337207702042233,
                              8.6450307455295494, 7.6497863928896201])

nws_dof = np.array([71.4990939155272400, 27.2055924272281220,
                    52.5168876481344640, 61.1501598507271140,
                    101.8780165180325200, 77.7502496403505180])

nws_scale_matrix_inv = np.array([[[0.9984995530022003, -0.4017356268696714],
                                   [-0.4017356268696714, 0.6256298158408907]],
                                 [[33.7614619993468350, -18.7869991858440170],
                                  [-18.7869991858440170, 11.3712392964398830]],
                                 [[0.8879716047189388, -0.9658252119870427],
                                  [-0.9658252119870427, 2.7495113978245249]],
                                 [[0.7035985286678833, -0.6890997926745869],
                                  [-0.6890997926745869, 1.1755994305621917]],
                                 [[1.1208124050115840, -0.6892580427070595],
                                  [-0.6892580427070595, 0.9269925552772419]],
                                 [[1.2412619589270877, -1.0297242600553977],
                                  [-1.0297242600553977, 1.1452470584603904]]])


nws_mean = np.array([[0.3001771880773990, 0.8330875088550247],
                     [-0.3586513930493177, -0.6512485727344066],
                     [0.9767345347954340, 0.3413160007425610],
                     [-1.2366316856224024, -0.7727830849769666],
                     [0.6398603088022538, 0.4260097693173131],
                     [-1.2724817720206010, -1.1980268704642587]])

nws_scale = np.array([23.9802943842041960, 2.8275036186810238,
                      21.5954085298635330, 29.5957283010434940,
                      32.9147387316129430, 29.2331705808944380])

# Output
latent_resp = np.genfromtxt("latent_resp.csv", delimiter=',')