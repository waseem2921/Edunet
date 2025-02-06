import pandas as pd

import matplotlib.pyplot as plt

# Function to collect fitness data
def collect_data():
    data = {
        'Date': [],
        'Steps': [],
        'Calories': [],
        'Distance': [],
        'ActiveMinutes': []
    }

    while True:
        date = input("Enter the date (YYYY-MM-DD) or 'stop' to finish: ")
        if date.lower() == 'stop':
            break
        steps = int(input("Enter the number of steps: "))
        calories = int(input("Enter the number of calories burned: "))
        distance = float(input("Enter the distance covered (in km): "))
        active_minutes = int(input("Enter the active minutes: "))

        data['Date'].append(date)
        data['Steps'].append(steps)
        data['Calories'].append(calories)
        data['Distance'].append(distance)
        data['ActiveMinutes'].append(active_minutes)

    return data

# Function to save data to Excel
def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('fitness_data.xlsx', index=False)
    print("Data saved to fitness_data.xlsx")

# Function to generate pie chart
def generate_pie_chart(data):
    labels = ['Steps', 'Calories', 'Distance', 'ActiveMinutes']
    sizes = [sum(data['Steps']), sum(data['Calories']), sum(data['Distance']), sum(data['ActiveMinutes'])]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Fitness Data Distribution')
    plt.show()

# Main function
def main():
    data = collect_data()
    save_to_excel(data)
    generate_pie_chart(data)

if __name__ == "__main__":
    main()