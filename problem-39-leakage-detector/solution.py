def solve(columns):
    # TODO: Return the columns whose lowercase name contains a leakage keyword.
    columns = columns
    res = []
    err = {'target', 'label', 'future', 'outcome', 'post'}

    for i in columns:
        
        for j in err:
            if j in i.lower():
                res.append(i)
    return res
