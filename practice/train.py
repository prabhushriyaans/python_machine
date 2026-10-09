import torch
from torch import nn
from torch import optim
from DSA import Queue
IN = torch.tensor([[1, 1], [0, 0], [1, 0], [0, 1]], dtype=torch.float32)
OR = torch.tensor([[1], [0], [1], [1]], dtype=torch.float32)
AND = torch.tensor([[1], [0], [0], [0]], dtype=torch.float32)
XOR = torch.tensor([[0], [0], [1], [1]], dtype=torch.float32)
class OREngine(nn.Module):
    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(2,18)
        self.L2=nn.Linear(18,1)
    def forward(self,x):
        x=self.L1(x)
        x=self.L2(x)
        return x
    
class ANDEngine(nn.Module):
    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(2,18)
        self.L2=nn.Linear(18,1)
    def forward(self,x):
        x=self.L1(x)
        x=self.L2(x)
        return x
    
class XOREngine(nn.Module):
    def __init__(self):
        super().__init__()
        self.L1=nn.Linear(2,18)
        self.R=nn.ReLU()
        self.L2=nn.Linear(18,1)
    def forward(self,x):
        x=self.L1(x)
        x=self.R(x)
        x=self.L2(x)
        return x

def train_and_save_models():
    M1 = OREngine()
    M2 = ANDEngine()
    M3 = XOREngine()
    Q = Queue()
    Q_out = Queue()
    Q.enqueue(M1)
    Q.enqueue(M2)
    Q.enqueue(M3)
    Q_out.enqueue(OR)
    Q_out.enqueue(AND)
    Q_out.enqueue(XOR)
    loss_fn = nn.BCEWithLogitsLoss()
    i = 0

    while not Q.is_empty():
        Model = Q.dqueue()
        target = Q_out.dqueue()
        Opt = optim.Adam(params=Model.parameters(), lr=0.05)

        for epoch in range(1000):
            Model.train()
            out = Model(IN)
            Loss = loss_fn(out, target)
            Opt.zero_grad()
            Loss.backward()
            Opt.step()
            if epoch % 100 == 0:
                print(f"epoach:{epoch} Loss:{Loss.item():.4f}")

        print()
        torch.save(Model.state_dict(), f"M{i}.pth")
        i += 1


if __name__ == "__main__":
    train_and_save_models()
        
