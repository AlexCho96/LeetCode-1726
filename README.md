# LeetCode - 1726. Tuple with Same Product

## Statement
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.


### Example 1
> **Input**: nums = [2,3,4,6] <br>
**Output**: 8 <br>
**Explanation**: There are 8 valid tuples: <br>
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3) <br>
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

### Example 2
> **Input**: nums = [1,2,4,5,10] <br>
**Output**: 16 <br>
**Explanation**: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2) <br>
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1) <br>
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4) <br>
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
