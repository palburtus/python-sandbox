def normalize_name(name):
    name = name.replace(' sr', '')
    name = name.replace(' .sr', '')

    name = name.replace(' jr', '')
    name = name.replace(' .jr', '')

    name = name.replace(' Sr', '')
    name = name.replace(' .Sr', '')

    name = name.replace(' Jr', '')
    name = name.replace(' .Jr', '')

    name = name.replace(' SR', '')
    name = name.replace(' .SR', '')

    name = name.replace(' JR', '')
    name = name.replace(' .JR', '')
    
    name = name.replace(' II', '')
    name = name.replace(' III', '')
    name = name.replace(' IV', '')

    name = name.replace('.', '')

    return name