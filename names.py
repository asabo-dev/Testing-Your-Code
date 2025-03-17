from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

"""We could use this approach to test our different programs
by importing the funtions and executing them as shown above.
OR we can use a much more efficient method which is the unit test
provided by Python to authomate the tests.
."""
