import random
import matplotlib.pyplot as plt
import numpy as np
import math

class Stock:
    def __init__(self, name: str, ipo: float):
        self.name = name
        self.ipo = ipo
    def symmetric_random_walk(self, time_steps: int) -> list[tuple[float, int]]:
        price = self.ipo
        price_over_time = []
        for time_elapsed in range(time_steps+1):
            if time_elapsed == 0:
                price_over_time.append((price, time_elapsed))
                continue
            price += random.choice([-1, 1])
            price_over_time.append((price, time_elapsed))
        return price_over_time
    def random_walk_with_drift(self, trend: float, volatility: float, time_steps: int, dt: float = 1/252) -> list[tuple[float, int]]:
        price = self.ipo
        price_over_time = []
        for time_elapsed in range(time_steps+1):
            if time_elapsed == 0:
                price_over_time.append((price, time_elapsed))
                continue
            white_noise = random.gauss(0, 1)
            price += trend * dt + volatility * math.sqrt(dt) * white_noise
            price_over_time.append((price, time_elapsed))
        return price_over_time
    def geometric_brownian_motion(self, trend: float, volatility: float, time_steps: int, dt: float = 1/252):
        price = self.ipo
        price_over_time = []
        for time_elapsed in range(time_steps+1):
            if time_elapsed == 0:
                price_over_time.append((price, time_elapsed))
                continue
            white_noise = random.gauss(0, 1)
            price *= np.exp(((trend) - (volatility)**2 / 2) * dt + (volatility) * white_noise * math.sqrt(dt))
            price_over_time.append((price, time_elapsed))
        return price_over_time
    

apple = Stock("AAPL", 1000)

class StockChart:
    def __init__(self, data: list[tuple[float, int]], stock_name: str, xstart: int = 0):
        np_data = np.array(data)

        print(np.round(np.arange(min(np_data[:, 0]), max(np_data[:, 0]), round(max(np_data[:, 0]) - min(np_data[:, 0])) / 10), 2))

        plt.plot(np_data[:, 1], np_data[:, 0])
        plt.xticks(np.arange(xstart, np_data.shape[0], np.round(np_data.shape[0] / 10)))
        plt.yticks(np.round(np.arange(min(np_data[:, 0]), max(np_data[:, 0]), round(max(np_data[:, 0]) - min(np_data[:, 0])) / 10), 2))
        plt.xlim(xstart, np_data.shape[0])
        plt.ylim(min(np_data[:, 0]), max(np_data[:, 0]))
        plt.xlabel("Zeit [d]")
        plt.ylabel("Aktienpreis [€]")
        ax = plt.gca()
        ax.ticklabel_format(useOffset=False)
        plt.title(stock_name)
        plt.show()

StockChart(apple.symmetric_random_walk(1000), "Apple (Random Walk, symmetrisch)")
StockChart(apple.random_walk_with_drift(80, 40, 1000), "Apple (Random Walk, mit Drift)")
StockChart(apple.geometric_brownian_motion(.08, .04, 1000), "Apple (geometrische Brownsche Bewegung)")