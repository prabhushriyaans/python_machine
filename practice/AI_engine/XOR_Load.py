import torch
# from torch import optim
from torch import nn
X=torch.tensor([[1,0],[0,0],[0,1],[1,1]],dtype=torch.float32)
Y=torch.tensor([[1],[0],[1],[0]],dtype=torch.float32)
torch.manual_seed(42)
class Neuron(nn.Module):
    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(2,6)
        self.R=nn.ReLU()
        self.L2=nn.Linear(6,1)
    def forward(self,x):
        x=self.L1(x)
        x=self.R(x)
        x=self.L2(x)
        return x
M=Neuron()
M.load_state_dict(torch.load("XOR.pth"))
with torch.inference_mode():
    out=M(X)
    out=torch.round(torch.sigmoid(out))
    print(out)