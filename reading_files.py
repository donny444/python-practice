from asyncore import read
from re import sub


with open("Subscription.txt", "r") as subscription_file:
    readFile = subscription_file.read()
    print(readFile)