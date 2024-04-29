import numpy as np

def inverse_kinematics(to, Target):
    global uLINK

    lambda_val = 0.5
    idx = FindRoute(to)
    ForwardKinematics(1)
    err = CalcVWerr(Target, uLINK[to])
    
    for _ in range(10):
        J = CalcJacobian(idx)
        err = CalcVWerr(Target, uLINK[to])
        
        if np.linalg.norm(err) < 1E-6:
            return np.linalg.norm(err)
        
        for nn, j in enumerate(idx):
            uLINK[j].q = uLINK[j].q + dq[nn]
        
        ForwardKinematics(1)

    return np.linalg.norm(err)