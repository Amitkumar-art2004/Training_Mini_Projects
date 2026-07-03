import numpy as np
def show_report(data):
    numbers = np.array(data)
    print("\n========== Statistics Report ==========")
    print(f"Total Values        : {numbers.size}")
    print(f"Mean                : {np.mean(numbers)}")
    print(f"Median              : {np.median(numbers)}")
    print(f"Standard Deviation  : {np.std(numbers)}")
    print(f"Minimum Value       : {np.min(numbers)}")
    print(f"Maximum Value       : {np.max(numbers)}")
    print(f"Sum                 : {np.sum(numbers)}")
    print("=======================================")
  
def main():
    print("NumPy Statistics Dashboard")
    print("--------------------------")
    # User input
    values = input(
        "Enter numbers separated by commas: "
    )
    # Convert string input to list of numbers
    dataset = [
        float(num) 
        for num in values.split(",")
    ]
    show_report(dataset)
if __name__ == "__main__":
    main()
