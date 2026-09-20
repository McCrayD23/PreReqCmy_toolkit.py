def calculate_average(numbers):
    """Calculates and returns the average of a list of numbers. Returns 0 is empty."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max_and_min(numbers):
    """Finds highest and lowest numbers using a loop. Returns (max, min)."""
    if not numbers:
        return (None, None)

    highest = numbers[0]
    lowest = numbers[0]

    for num in numbers:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    return (highest, lowest)

def count_occurrences(items, target):
    """Counts how many times target appears in items."""
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

def is_palindrome(text):
    """Checks if text is a palindrome, ignoring spaces and case."""
    cleaned = text.lower().replace(" ", "")

    return cleaned == cleaned[::-1]

def create_report(title, scores):
    """Generates a formatted report string incorporating internal helper functions."""
    avg = calculate_average(scores)
    max_val, min_val = find_max_and_min(scores)

    report = f"==={title} ===\n"
    report += f"Average: {avg:.2f}\n"
    report += f"Max: {max_val}\n"
    report += f"Min: {min_val}"

    return report

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    print ("\n--- Edge Case Testing ---")

    # Empty list edge case testing

    print(f"Empty list average: {calculate_average([])}")
    print(f"Empty list max/min: {find_max_and_min([])}")

    # String edge cases (mixed case, spaces, single character)
    print(f"Panama palindrome: {is_palindrome('A man a plan a canal Panama')}")
    print(f"Single character palindrome: {is_palindrome('a')}")

    # Multiple occurrences count

    print(f"Count of 10 in [10, 20, 10, 10]: {count_occurrences([10, 20, 10, 10], 10)}")
    
