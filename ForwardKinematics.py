# 順運動学の関数
def forward_kinematics(j):
    global uLINK

    if j == 0:
        return
    if j != 1:
        mom = uLINK[j].mother
        uLINK[j].p = uLINK[mom].R @ uLINK[j].b + uLINK[mom].p
        uLINK[j].R = uLINK[mom].R @ rodrigues(uLINK[j].a, uLINK[j].q)
    forward_kinematics(uLINK[j].sister)
    forward_kinematics(uLINK[j].child)