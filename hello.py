numbers = [3, 2, 0, 1]
input_value = 18

def process_number(number):
    try:
        result = input_value / number
        print(f"18 / {number} = {result}")

    except Exception as e:
        result = 0
        print(f"Error occurred: {e}")
        print(f"Default result = {result}")

def main():
    for num in numbers:
        process_number(num)

if __name__ == "__main__":
    main()
