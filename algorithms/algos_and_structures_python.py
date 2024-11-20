# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:  # Base case for recursion
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):  # Traverse the array
        if arr[i] == target:  # Return index if target is found
            return i
    return -1  # Return -1 if target is not found

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2  # Calculate the midpoint
        if arr[mid] == target:  # Target found
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:  # Visit unvisited neighbors
            dfs(graph, neighbor, visited)
    return visited

# Breadth-First Search (BFS)
from collections import deque

def bfs(graph, start):
    visited = set()  # Initialize visited set
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()  # Visit the first vertex in the queue
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Fibonacci Numbers
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):  # Compute Fibonacci numbers iteratively
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

# GCD (Euclid's Algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b  # Replace a with b and b with a % b
    return a
