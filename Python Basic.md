# Python Basic
## 一. tube
### 1. tube[0]=value, tube is immutable for first level
```
tu = (1,2,3)
tu[1] = 4
Output->TypeError: 'tuple' object does not support item assignment
tu = (1, [2, 3, 4], 5)
tu[1][0] = 6
print tu
Output->(1, [6, 3, 4], 5)
```
### 2. tube + tube, tube * 3
```
tu = (1,2,3)
print tu + tu
print tu * 3
Output->(1, 2, 3, 4, 1, 1, 2, 3, 4, 1)
        (1, 2, 3, 4, 1, 1, 2, 3, 4, 1, 1, 2, 3, 4, 1)
```
### 3. tube and ()
```
tu = (2)
print type(tu)
tu = (2,)
print type(tu)
tu = 1,2,3
Output-><type 'int'>
        <type 'tuple'>
        <type 'tuple'>
```
### 4. tube method build-in
```
tu = (1, 2, 3, 1)
print tu.index(1)
print tu.count(1)
Output->0
        1
```
