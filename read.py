import pandas as pd

def load_data():
    df = pd.DataFrame(pd.read_csv("debate.csv", encoding="latin-1"))
    return df

if __name__ == "__main__":
    load_data()
