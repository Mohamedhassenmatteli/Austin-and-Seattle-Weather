import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv("seattle_weather.csv",nrows=12) 
austin_weather = pd.read_csv("austin_weather.csv",nrows=12)
month_map = {
    1: "Jan",
    2: "Feb",
    3:  "Mar",
    4:  "Apr",
    5:  "May",
    6:  "Jun",
    7:  "Jul",
    8:  "Aug",
    9:  "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

seattle_weather['MONTH'] = seattle_weather['DATE'].map(month_map)
austin_weather['MONTH'] = austin_weather['DATE'].map(month_map)
# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color = "b")
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color = "b", linestyle = "--")
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color = "b", linestyle = "--")

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color = "r")
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color = "r", linestyle = "--")
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color = "r", linestyle = "--")




plt.show()