import matplotlib.pyplot as plt

# The data for the first graph, with x and y values for each series
temperature_data = [(1, 23), (2, 25), (3, 28), (4, 30), (5, 32)]
humidity_data = [(1, 50), (2, 55), (3, 60), (4, 65), (5, 70)]
pressure_data = [(1, 1013), (2, 1015), (3, 1017), (4, 1018), (5, 1020)]

# The data for the second graph, with x and y values for each series
wind_data = [(1, 5), (2, 10), (3, 15), (4, 20), (5, 25)]
rainfall_data = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 1)]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot the data for the first graph
ax1.plot(*zip(*temperature_data), label='Temperature')
ax1.plot(*zip(*humidity_data), label='Humidity')
ax1.plot(*zip(*pressure_data), label='Pressure')
ax1.legend()
ax1.set_title('hi')
ax1.set_xlabel('Day')
ax1.set_ylabel('Weather Value')

# Plot the data for the second graph
ax2.plot(*zip(*wind_data), label='Wind Speed')
ax2.plot(*zip(*rainfall_data), label='Rainfall')
ax2.legend()

# Save the figure to a PDF file
fig.savefig('weather_data.pdf')
