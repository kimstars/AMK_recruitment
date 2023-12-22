def solve(recv1):
    recv = recv

    recv = recv.split("= ")[1]
    recv = (recv[1:-1]).split(",")

    recv = [int(i) for i in recv]

    res = (max(recv))
    return res