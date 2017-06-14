def words(maneno):
    maneno_dict = {}
    count = 1

    if len({maneno}) > 1:
        for neno in maneno:
            if neno in maneno_dict:
                count += 1
                maneno_dict[neno] = 1
            else:
                maneno_dict[neno] = 1
    else:
        return {maneno: 1}
    
    return maneno_dict