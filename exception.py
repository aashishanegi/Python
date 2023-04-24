try:
    a=10
    b=0
    c='a'
    d=a/b
    e=a/c
except Exception as e:
    print("oops",e.__class__,"has occurred")
