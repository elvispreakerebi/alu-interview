# Rain Water Retention Calculator

## Description
This project contains a solution to calculate how many square units of water will be retained after it rains, given a list of non-negative integers representing wall heights.

## Task Requirements
* Create a function that calculates how many square units of water will be retained after it rains
* Prototype: `def rain(walls)`
* Parameters:
  * `walls`: a list of non-negative integers representing wall heights
* Return: Integer indicating total amount of rainwater retained
* Notes:
  * Walls have a width of 1 unit
  * Assume that the ends of the list (before index 0 and after index walls[-1]) are not walls
  * If the list is empty, return 0

## Examples
```python
walls = [0, 1, 0, 2, 0, 3, 0, 4]
rain(walls) # Returns: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
rain(walls) # Returns: 6