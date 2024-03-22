if False:
    try:
        exec("imp" + "ort matplotlib.pyplot as plt")
    except:
        pass

class Debug:
    THRESHOLD = 100
    xs = []
    ys = {}

    @staticmethod
    def process(data, timestamp):
        Debug.xs.append(timestamp)
        for y_name, y_val in data:
            if y_name not in Debug.ys:
                Debug.ys[y_name] = []
            Debug.ys[y_name].append(y_val)
        if len(Debug.xs) % Debug.THRESHOLD == 0:
            Debug.plot()

    @staticmethod
    def plot():
        try:
            for y in Debug.ys.values():
                plt.plot(Debug.xs, y)
            plt.show()
        except:
            pass
