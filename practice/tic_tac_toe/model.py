import torch.nn as nn
class TicTacToeNet(nn.Module):

    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(9,78)
        self.R1=nn.ReLU()
        self.L2=nn.Linear(78,256)
        self.R2=nn.ReLU()
        self.L3=nn.Linear(256,9)


    def forward(self, x):
        x=self.L1(x)
        x=self.R1(x)
        x=self.L2(x)
        x=self.R2(x)
        x=self.L3(x)
        return x