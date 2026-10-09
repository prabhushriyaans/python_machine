import torch
from engine import Engine
IN=torch.tensor([[0,1,0,1],[1,0,1,0],[1,1,0,0],[0,0,1,1]],dtype=torch.float32)
OUT=torch.tensor([[0,0],[1,1],[1,0],[0,1]],dtype=torch.float32)
M=Engine()
M.load_state_dict(torch.load("wgh.pth"))
with torch.inference_mode():
    out=M(IN)
    out=torch.round(torch.sigmoid(out))
    print(out)
# if out==OUT:
#     print("Yes the Model is trained and optimised.")