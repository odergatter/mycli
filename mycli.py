import sys
import datetime

def main():
    if len(sys.argv) > 1 :
        if sys.argv[1] == "now":
            print(datetime.datetime.now())
        elif sys.argv[1] ==  "utcnow":
            print(datetime.datetime.utcnow())


if __name__ == "__main__":
    main()
