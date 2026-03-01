

def congratulations(pm, tester, *developers):
        print("Happy New Year! Take care of yourself and your loved ones!")
        print("For:")

        print(pm)
        print(tester)

        for dev in developers:
            names = dev.split()
            for name in names:
                  print(name)
           
congratulations("Alice", "Mike", "Roman Victoria")