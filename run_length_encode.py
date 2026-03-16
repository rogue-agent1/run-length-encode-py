#!/usr/bin/env python3
"""Run-length encoding and decoding."""
def rle_encode(s):
    if not s:return""
    result=[];count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:count+=1
        else:result.append(f"{count}{s[i-1]}");count=1
    result.append(f"{count}{s[-1]}");return"".join(result)
def rle_decode(s):
    import re;return"".join(c*int(n) for n,c in re.findall(r"(\d+)(.)",s))
