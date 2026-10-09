import torch 
from torch import nn
from torch import optim 

class Engine(nn.Module):
    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(4,64)
        self.R1=nn.ReLU()
        self.L2=nn.Linear(64,128)
        self.R2=nn.ReLU()
        self.OT=nn.Linear(128,2)
    def forward(self,x):
        x=self.L1(x)
        x=self.R1(x)
        x=self.L2(x)
        x=self.R2(x)
        x=self.OT(x)
        return x

