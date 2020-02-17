from packer.measurer import Measurer
import packer.rectangle as r

print("name is: ", __name__)


def main():
    container = r.Rectangle(width=20, height=10)
    item = r.Rectangle(width=5, height=3)
    minSpace = 1
    measurer = Measurer(container, item, minSpace)
    print(measurer.Measure())


if __name__ == "__main__":
    main()

