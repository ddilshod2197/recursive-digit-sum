def raqamlar_yigindi(son):
    if son == 0:
        return 0
    else:
        return son % 10 + raqamlar_yigindi(son // 10)
```

```python
def raqamlar_yigindi(son):
    def yigindi(son):
        if son == 0:
            return 0
        else:
            return son % 10 + yigindi(son // 10)
    return yigindi(son)
```

```python
def raqamlar_yigindi(son):
    yigindi = 0
    while son > 0:
        yigindi += son % 10
        son //= 10
    return yigindi
