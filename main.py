from pathlib import Path
import polars
import sys

def main():
    Path("input").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)
    polars.DataFrame({"col1": [0, 2], "col2": [3, 7]}).write_csv(Path("output").joinpath("df.csv"))
    print(polars.__version__, file=sys.stderr)


if __name__ == "__main__":
    main()
