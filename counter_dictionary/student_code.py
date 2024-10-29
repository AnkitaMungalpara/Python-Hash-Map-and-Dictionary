

def validate(data, template, parent=[]) : # Should return (True, '')
    # if data ans template both are dictionary
    if isinstance(data, dict) and isinstance(template, dict):
        # check if no extra keys
        for k in data:
            if k not in template:
                # found Extra keys
                parent.append(k)
                return  (False, f'mismatched keys: {".".join(parent)}')
                #mismatched keys: name.middle'
        # check if no missing keys
        for k in template:
            if k not in data:
                # missing keys
                parent.append(k)
                return  (False, f'mismatched keys: {".".join(parent)}')
            
        # top level check done now iterateover dictionary and validate
        for k in template:
            if k in data:
                parent.append(k)
                ret = validate(data[k], template[k], parent)
                if ret[0]==True:
                    parent.pop()
                else:
                    return ret
        for k in data:
            if k in template:
                parent.append(k)
                ret = validate(data[k], template[k], parent)
                if ret[0]==True:
                    parent.pop()
                else:
                    return ret


    if isinstance(template, type):
        if not isinstance(data, template):
            return (False,f"bad type: {".".join(parent)}")
    
    return (True,"")
