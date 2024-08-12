# Python - Everything is Object

This project delves into how Python handles objects, references, and mutability. The questions are designed to help you understand how Python manages different types of objects, how references work, and how these concepts influence the behavior of Python code.

## Resources

To understand these concepts more deeply, it's recommended to review the following topics:
- Objects and values
- Aliasing
- Mutable vs immutable types
- How Python passes arguments to functions


## Tasks

### 0. Who am I?
**Question:** What function would you use to print the type of an object?
**Answer:** [0-answer.txt](./0-answer.txt)

### 1. Where are you?
**Question:** How do you get the variable identifier (memory address in CPython)?
**Answer:** [1-answer.txt](./1-answer.txt)

### 2. Same object?
**Question:** In the following code, do `a` and `b` point to the same object?
```python
a = 89
b = 100
```
**Answer:** [2-answer.txt](./2-answer.txt)

### 3. Same object with equality?
**Question:** In the following code, do `a` and `b` point to the same object?
```python
a = 89
b = 89
```
**Answer:** [3-answer.txt](./3-answer.txt)

### 4. Simple assignment
**Question:** In the following code, do `a` and `b` point to the same object?
```python
a = 89
b = a
```
**Answer:** [4-answer.txt](./4-answer.txt)

### 5. Addition and assignment
**Question:** In the following code, do `a` and `b` point to the same object?
```python
a = 89
b = a + 1
```
**Answer:** [5-answer.txt](./5-answer.txt)

### 6. Is equal
**Question:** What do these 3 lines print?
```python
s1 = "Best School"
s2 = s1
print(s1 == s2)
```
**Answer:** [6-answer.txt](./6-answer.txt)

### 7. Is the same
**Question:** What do these 3 lines print?
```python
s1 = "Best"
s2 = s1
print(s1 is s2)
```
**Answer:** [7-answer.txt](./7-answer.txt)

### 8. Is really equal
**Question:** What do these 3 lines print?
```python
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
```
**Answer:** [8-answer.txt](./8-answer.txt)

### 9. Is really the same
**Question:** What do these 3 lines print?
```python
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
```
**Answer:** [9-answer.txt](./9-answer.txt)

### 10. And with a list, is it equal
**Question:** What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
```
**Answer:** [10-answer.txt](./10-answer.txt)

### 11. And with a list, is it the same
**Question:** What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)
```
**Answer:** [11-answer.txt](./11-answer.txt)

### 12. And with a list, is it really equal
**Question:** What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
```
**Answer:** [12-answer.txt](./12-answer.txt)

### 13. And with a list, is it really the same
**Question:** What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
```
**Answer:** [13-answer.txt](./13-answer.txt)

### 14. List append
**Question:** What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
**Answer:** [14-answer.txt](./14-answer.txt)

### 15. List add
**Question:** What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
**Answer:** [15-answer.txt](./15-answer.txt)

### 16. Integer incrementation
**Question:** What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
**Answer:** [16-answer.txt](./16-answer.txt)

### 17. List incrementation
**Question:** What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
**Answer:** [17-answer.txt](./17-answer.txt)

### 18. List assignment
**Question:** What does this script print?
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
**Answer:** [18-answer.txt](./18-answer.txt)

### 19. Copy a list object
**Task:** Write a function `def copy_list(a_list):` that returns a copy of a list.
**Implementation:** [19-copy_list.py](./19-copy_list.py)

### 20. Tuple or not?
**Question:** `a = ()` Is `a` a tuple?
**Answer:** [20-answer.txt](./20-answer.txt)

### 21. Tuple or not?
**Question:** `a = (1, 2)` Is `a` a tuple?
**Answer:** [21-answer.txt](./21-answer.txt)

### 22. Tuple or not?
**Question:** `a = (1)` Is `a` a tuple?
**Answer:** [22-answer.txt](./22-answer.txt)

### 23. Tuple or not?
**Question:** `a = (1, )` Is `a` a tuple?
**Answer:** [23-answer.txt](./23-answer.txt)

### 24. Who am I?
**Question:** What does this script print?
```python
a = (1)
b = (1)
a is b
```
**Answer:** [24-answer.txt](./24-answer.txt)

### 25. Tuple or not?
**Question:** What does this script print?
```python
a = (1, 2)
b = (1, 2)
a is b
```
**Answer:** [25-answer.txt](./25-answer.txt)

### 26. Empty is not empty
**Question:** What does this script print?
```python
a = ()
b = ()
a is b
```
**Answer:** [26-answer.txt](./26-answer.txt)

### 27. Still the same?
**Question:** Will the last line of this script print `139926795932424`?
```python
a = [1, 2, 3, 4]
print(id(a))
a = a + [5]
print(id(a))
```
**Answer:** [27-answer.txt](./27-answer.txt)

### 28. Same or not?
**Question:** Will the last line of this script print `139926795932424`?
```python
a = [1, 2, 3]
print(id(a))
a += [4]
print(id(a))
```
**Answer:** [28-answer.txt](./28-answer.txt)

### 29. Python3: Mutable, Immutable... everything is object!
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

introduction
id and type
mutable objects
immutable objects
why does it matter and how differently does Python treat mutable and immutable objects
how arguments are passed to functions and what does that imply for mutable and immutable objects
If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
