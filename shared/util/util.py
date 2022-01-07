import collections


def recursiveUpdate(d: dict, u: dict) -> dict:
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = recursiveUpdate(d.get(k, {}), v)
        else:
            d[k] = v
    return d
