import torch 
from torch import nn
from torch import optim
X=torch.tensor([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]],dtype=torch.float32)
Y=torch.tensor([[0],[1],[1],[0],[1],[0],[0],[1]],dtype=torch.float32)

class Engine(nn.Module):
    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(3,64)
        self.R=nn.ReLU()
        self.L2=nn.Linear(64,1)
    def forward(self,x):
        x=self.L1(x)
        x=self.R(x)
        x=self.L2(x)
        return x
M=Engine()

with torch.inference_mode():
    out=M(X)
    out=torch.round(torch.sigmoid(out))
    print(out)

loss_fn=nn.BCEWithLogitsLoss()
Opt=optim.SGD(M.parameters(),lr=0.1)
for epoch in range(10000):
    M.train()
    out=M(X)
    loss=loss_fn(out,Y)
    Opt.zero_grad()
    loss.backward()
    Opt.step()
    if epoch%1000==0:
        print(f"{epoch} Loss:{loss}")

with torch.inference_mode():
    out=M(X)
    out=torch.round(torch.sigmoid(out))
    print(out)