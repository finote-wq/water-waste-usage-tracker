# Water Waste & Usage Tracker
# This program estimates household water waste
# and displays statistics to encourage water conservation.


def main():
    print("=" * 50)
    print("          WATER WASTE & USAGE TRACKER")
    print("=" * 50)
    print("This program helps estimate household water waste")
    print("and provides statistics about water usage.")
    print()

    try:
        # Get information from the user
        household_size = int(
            input("Enter the number of people in your household: ")
        )

        days_tracked = int(
            input("Enter the number of days being tracked: ")
        )

        total_water_used = float(
            input("Enter total water used in gallons: ")
        )

        water_wasted = float(
            input("Enter estimated water wasted in gallons: ")
        )

        # Validate the information
        if household_size <= 0:
            raise ValueError("Household size must be greater than zero.")

        if days_tracked <= 0:
            raise ValueError("Number of days must be greater than zero.")

        if total_water_used < 0:
            raise ValueError("Water usage cannot be negative.")

        if water_wasted < 0:
            raise ValueError("Water waste cannot be negative.")

        if water_wasted > total_water_used:
            raise ValueError(
                "Estimated water waste cannot exceed total water usage."
            )

        # Calculate statistics
        average_daily_usage = total_water_used / days_tracked

        water_used_per_person = (
            total_water_used / household_size
        )

        waste_percentage = (
            water_wasted / total_water_used
        ) * 100 if total_water_used > 0 else 0

        potential_savings = water_wasted

        # Display statistics
        print("\n" + "=" * 50)
        print("              WATER USAGE STATISTICS")
        print("=" * 50)

        print(f"Household Size:              {household_size} people")
        print(f"Days Tracked:                 {days_tracked} days")
        print(f"Total Water Used:             {total_water_used:.2f} gallons")
        print(f"Estimated Water Wasted:       {water_wasted:.2f} gallons")
        print(f"Average Daily Usage:          {average_daily_usage:.2f} gallons")
        print(f"Total Usage Per Person:       {water_used_per_person:.2f} gallons")
        print(f"Water Waste Percentage:       {waste_percentage:.2f}%")
        print(f"Potential Water Savings:      {potential_savings:.2f} gallons")

        print("\n" + "=" * 50)

        # Provide a conservation message
        if waste_percentage <= 10:
            print("Great job! Your estimated water waste is relatively low.")
        elif waste_percentage <= 25:
            print("There may be opportunities to reduce your water waste.")
        else:
            print("Consider finding ways to reduce unnecessary water waste.")

        print("=" * 50)

    except ValueError as error:
        print("\nERROR:", error)
        print("Please enter valid numerical information.")

    finally:
        print("\nThank you for using the Water Waste & Usage Tracker!")
        print("Every effort to conserve water can make a difference.")


if __name__ == "__main__":
    main()
