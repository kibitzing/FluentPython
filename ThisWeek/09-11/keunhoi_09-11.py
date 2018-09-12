# Searching deactivated ReLU
ReLUs = [('layer1-1', 'relu', 2.3),
('layer1-2', 'relu', 0),
('layer1-3', 'relu', 2.5),
('layer2-1', 'relu', 1.2),
('layer2-2', 'relu', 4.3),
('layer3-1', 'relu', 0),
('layer3-2', 'relu', 0),
('layer4-1', 'relu', 0),
('layer4-2', 'relu', 0)
]
print('{:^20} || {:^9}'.format('Deactivated ReLUs','value'))
fmt = '{:^20} || {:^9f}'
for layer, _, val in ReLUs:
    if val == 0:
        print(fmt.format(layer,val))

# Searching deactivated PReLU
PReLUs = [('layer1-1', 'prelu', 0.02, 2.3),
('layer1-2', 'prelu', -0.3, -1.7),
('layer1-3', 'prelu', 0.3, 2.5),
('layer2-1', 'prelu', 0.7, 1.2),
('layer2-2', 'prelu', 0.4, 4.3),
('layer3-1', 'prelu', -0.9, -1.5),
('layer3-2', 'prelu', -0.00005, -0.002),
('layer4-1', 'prelu', -0.0024, -0.014),
('layer4-2', 'prelu', -0.3, 0.4)
]
print('{:^20} || {:^12} || {:^12}'.format('Deactivated PReLUs','alpha_val', 'value'))
fmt = '{:^20} || {:^12f} || {:^12f}'
for layer, activation, alpha, val in PReLUs:
    if abs(alpha) <= 0.01:
        print(fmt.format(layer, alpha, val))

# namedtuple
from collections import namedtuple

Models = namedtuple('Model', 'model_num body activation optimizer')
model1 = Models('model1', 'vgg', 'relu', 'sgd')
model2 = Models('model2', 'vgg', 'relu', 'Adam')
model3 = Models('model3', 'resnet', 'relu', 'sgd')
model4 = Models('model4', 'resnet', 'relu', 'Adam')

print(Models._fields)