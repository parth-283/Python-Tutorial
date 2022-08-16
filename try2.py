
try:
    # f = open("doseNot.txt")
    f1 = open("DemoText.txt")

except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
    print("Run anyway...")
    # f.close()
    f1.close()