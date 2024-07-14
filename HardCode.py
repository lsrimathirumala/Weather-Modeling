import matplotlib.pyplot as plt

def quadratic_temperature_model(day, a, b, c):
    """Calculate temperature based on a quadratic model."""
    temperature = a * day**2 + b * day + c
    return temperature

def main():
    """Main function to run the temperature model."""
    # Fixed coefficients for the quadratic equation: ax^2 + bx + c
    a = 1
    b = 4
    c = 4

    while True:
        try:
            # Get the number of days to model from the user
            num_days = int(input("Enter the number of days to model: "))
            if num_days <= 0:
                raise ValueError("Number of days must be a positive integer.")
            break
        except ValueError as e:
            print(e)
            continue

    # Lists to store day and corresponding temperature values
    days = list(range(1, num_days + 1))
    temperatures = [quadratic_temperature_model(day, a, b, c) for day in days]

    # Plotting
    plt.plot(days, temperatures, label=f'Temperature: {a}x^2 + {b}x + {c}')
    plt.title('Weather Modeling')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
