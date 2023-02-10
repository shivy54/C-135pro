import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("filtered_dataset.csv")


star_names = data["star_name"].tolist()
mass = data["mass"].tolist()
radius = data["radius"].tolist()
distance = data["distance"].tolist()
gravity = data["gravity"].tolist()


plt.bar(star_names, mass)
plt.xlabel("Star Name")
plt.ylabel("Mass (kg)")
plt.title("Star Name vs Mass")
plt.xticks(rotation=90)
plt.show()

plt.bar(star_names, radius)
plt.xlabel("Star Name")
plt.ylabel("Radius (m)")
plt.title("Star Name vs Radius")
plt.xticks(rotation=90)
plt.show()

plt.bar(star_names, distance)
plt.xlabel("Star Name")
plt.ylabel("Distance (light years)")
plt.title("Star Name vs Distance")
plt.xticks(rotation=90)
plt.show()

plt.bar(star_names, gravity)
plt.xlabel("Star Name")
plt.ylabel("Gravity (m/s^2)")
plt.title("Star Name vs Gravity")
plt.xticks(rotation=90)
plt.show()
