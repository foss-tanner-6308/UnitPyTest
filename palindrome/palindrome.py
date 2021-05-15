def pali(s):
    s = s.lower().replace(" ", "")
    if str(s) == str(s)[::-1]:
        return True
    else:
        return False