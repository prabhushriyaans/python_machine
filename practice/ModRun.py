import torch
from train import OREngine,ANDEngine,XOREngine
from DSA import Queue
IN = torch.tensor([[1, 1], [0, 0], [1, 0], [0, 1]], dtype=torch.float32)
Q=Queue()
Q.enqueue(OREngine())
Q.enqueue(ANDEngine())
Q.enqueue(XOREngine())
i=0
while not Q.is_empty():
    M=Q.dqueue()
    M.load_state_dict(torch.load(f"M{i}.pth"))
    out=M(IN)
    out=torch.round(torch.sigmoid(out))
    print(out)
    i+=1
    print()

