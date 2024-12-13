# Save the HTML content to a file
html_file_path = "vehicle_status.html"
with open(html_file_path, "w") as html_file:
    html_file.write(html_content)

print(f"HTML file generated: {html_file_path}")

# Plot the parking slot status
def plot_parking_slots(latest_status):
    total_slots = 10  # Limited to 10 slots
    slot_status = ["Available"] * total_slots

    for number_plate, (_, status, slot) in latest_status.items():
        if status == "Inside" and slot is not None:
            slot = int(slot)  # Ensure slot is an integer
            slot_status[slot - 1] = f"Occupied by {number_plate}"

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(range(1, total_slots + 1), [1] * total_slots, color=['green' if status == "Available" else 'red' for status in slot_status])
    ax.set_yticks(range(1, total_slots + 1))
    ax.set_yticklabels([f"Slot {i}" for i in range(1, total_slots + 1)])
    ax.set_xlabel("Status")
    ax.set_title("Parking Slot Status")

    for i, status in enumerate(slot_status):
        ax.text(0.5, i + 1, status, va='center', ha='center', color='white')

    plt.show()

plot_parking_slots(latest_status)

#pattern printing
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot peak times
def plot_peak_times(df, column, title):
    # Convert the time column to datetime
    df[column] = pd.to_datetime(df[column], format='%H:%M:%S').dt.time

    # Count the occurrences of each hour
    df['Hour'] = pd.to_datetime(df[column], format='%H:%M:%S').dt.hour
    peak_times = df['Hour'].value_counts().sort_index()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(peak_times.index, peak_times.values, marker='o')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Vehicles')
    plt.title(title)
    plt.grid(True)
    plt.xticks(range(24))
    plt.show()

# Read the Excel file
excel_path = 'detection_log.xlsx'
df = pd.read_excel(excel_path)

# Plot peak times for entry and exit
plot_peak_times(df, 'Entry Time', 'Peak Entry Times')
plot_peak_times(df, 'Exit Time', 'Peak Exit Times')