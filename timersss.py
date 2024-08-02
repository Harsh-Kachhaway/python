import schedule
import time


def asdf():
    print("hello")
def bh():
    print("jk")

schedule.every(3).seconds.do(asdf)
schedule.every(1).seconds.do(bh)
while True:
    schedule.run_pending()
