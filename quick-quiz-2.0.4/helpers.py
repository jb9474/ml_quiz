from math import log



def entropy(pos, neg):
    # entropy as -plog_2 p-(1-p)log_2(1-p)

    p_dot = float(pos)/(pos+neg)

    print p_dot
    # print log(0, 2)

    entropy = -p_dot*log(p_dot, 2)-(1-p_dot)*log(1-p_dot,2)

    print entropy


entropy(2,2)