import torch
from torch import nn
from torch import optim
from engine import Engine
IN=torch.tensor([[0,1,0,1],[1,0,1,0],[1,1,0,0],[0,0,1,1]],dtype=torch.float32)
OUT=torch.tensor([[0,0],[1,1],[1,0],[0,1]],dtype=torch.float32)
M=Engine()
with torch.inference_mode():
    out=M(IN)
    out=torch.round(torch.sigmoid(out))
    print(out)
loss_fn=nn.BCEWithLogitsLoss()
Opt=optim.SGD(params=M.parameters(),lr=0.05)
for epoch in range(1000):
    M.train()
    out=M(IN)
    Loss=loss_fn(out,OUT)
    Opt.zero_grad()
    Loss.backward()
    Opt.step()
    if epoch%100==0:
        print(f"{epoch} Loss:{Loss:.4f}")
with torch.inference_mode():
    out=M(IN)
    out=torch.round(torch.sigmoid(out))
    print(out)
torch.save(M.state_dict(),"Wgh.pth")