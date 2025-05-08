# Bubble Sort Project

This project implements the **Bubble Sort** algorithm in Python. It works with both Python lists and linked lists. Additionally, I have written tests to verify the correctness of the algorithm.

## Features

| **Feature**                | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **Bubble Sort Algorithm**  | Can sort both list and linked list types.                                      |
| **Tests**                  | Written using the `unittest` module. Tests exist for both list and linked list. |
| **GitHub Actions**         | Automates test runs after each change for continuous integration.              |

## Usage

You need to have Python and the required packages installed.

| **Step**                | **Command/Instruction**                                                           |
|--------------------------|-----------------------------------------------------------------------------------|
| **Sorting Lists**        | Use the `bubble_sort` function from the `sorting_algorithms.py` file.           |
| **Sorting Linked Lists** | Use the `convert_to_linked_list` function from the `ds.py` file.                 |

## `__iter__` Method

To make it easier to loop over the linked list, I added the `__iter__` method. This method allows you to iterate over the linked list just like a normal Python list, making the code more readable and useful.

**Example usage:**

```python
sorted_ll = bubble_sort(linked_list)
for node in sorted_ll:
    print(node.value)g
AI Assistance
In this project, I used AI assistance at various stages of development. AI helped me write the algorithms and debug issues, making the code work correctly and more efficiently.

Error vs Failure
Term	Description
Error	An issue that prevents the program from running and usually causes it to crash. For example, using the wrong data type.
Failure	A test failure, where the program does not produce the expected result. In this case, the program continues to run, but the tests do not pass.