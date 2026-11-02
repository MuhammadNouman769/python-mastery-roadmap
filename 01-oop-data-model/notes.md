# 01 OOP & Data Model

## Day 1-2: `__str__` aur `__repr__`

### Meri samajh (apne alfaaz mein)
- `__str__`: print() par dikhta hai, insaan ke parhne ke liye.
- `__repr__`: list/debug mein dikhta hai, code jaisa, quotes ke saath.
- Agar `__str__` na ho to `print(obj)` bhi `__repr__` hi dikhata hai.
- Sirf ek likhni ho to `__repr__`.

### Mini example
```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book(title={self.title!r})"
```

---

## Interview Questions

### Q1. `__str__` aur `__repr__` mein kya farq hai?
`__str__` end user ke liye readable representation deta hai, aur `print()` aur `str()` isi ko call karte hain. `__repr__` developer ke liye unambiguous representation deta hai, jo debugging mein kaam aata hai, aur ideally us se object dobara bana sakte hain. Agar sirf ek implement karna ho to `__repr__` karni chahiye, kyunke `__str__` na ho to Python `__repr__` par fall back karta hai.

### Q2. List print karne par `__repr__` kyun chalta hai?
Containers jaise list, dict, tuple apne elements ko `__repr__` se dikhate hain, `__str__` se nahi. Is liye `print(students)` mein `__repr__` chalta hai, jabke loop mein `print(student)` karne par `__str__` chalta hai.

### Q3. Agar sirf `__str__` likhi ho, `__repr__` nahi, to kya hoga?
`print(obj)` to theek chalega, lekin list print karne ya shell mein object dekhne par default `<__main__.Student object at 0x...>` dikhega, jo debugging ke liye bekaar hai. Isi liye `__repr__` zaroor likhni chahiye.

### Q4. Agar sirf `__repr__` likhi ho, `__str__` nahi, to kya hoga?
`print(obj)` aur `str(obj)` dono `__repr__` hi use karenge. Koi error nahi aata.

### Q5. f-string mein `!r` kya karta hai?
Value par `repr()` call karta hai, is liye strings quotes ke saath dikhti hain. Misal: `f"{name!r}"` se `'Ali'` banta hai, `Ali` nahi.

### Q6. Kya `eval(repr(obj))` se object wapas ban sakta hai?
Ideally haan, yeh `__repr__` ka goal hai, lekin har class mein zaroori nahi. Is liye `__repr__` mein `!r` lagana acha hai.

### Q7. `print(obj)` aur `repr(obj)` mein kaun sa method call hota hai?
`print(obj)` `__str__` ko call karta hai (na ho to `__repr__`), jabke `repr(obj)` hamesha `__repr__` ko call karta hai.

### Tip
Interview mein sirf definition mat do, chhota example bhi do (upar wala `Book` class). Isse lagta hai ke tumne sach mein code kiya hai.

---

## Aaj ki galtiyan / seekh
- `__repr__` mein `!r` lagana zaroori hai taake strings quotes ke saath aayein.
- Classes ke beech 2 blank lines (PEP 8).