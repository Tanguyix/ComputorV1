def sqrt(nb, precision):
    root = nb
    while root * root >= nb + precision or root * root <= nb - precision:
        root = (root + nb / root) / 2
    return(root)