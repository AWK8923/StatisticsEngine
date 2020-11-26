from statisticsengine.lib import readfile, stats


def main():
    print("+--------------------------+\n"
          "|    AWK's Stats Engine    |\n"
          "+--------------------------+\n"
          "| 1. One Variable Stats    |\n"
          "| 2. Linear Regression     |\n"
          "+--------------------------+\n")
    selection = input("Please input a selection: ")

    if selection == "1":
        print("+--------------------------+\n"
              "|    AWK's Stats Engine    |\n"
              "+--------------------------+\n"
              "| 1. Print Statistics      |\n"
              "| 2. Create Box Plot       |\n"
              "| 3. Both                  |\n"
              "+--------------------------+\n")
        selection = input("Please input a selection: ")
        if selection == "1":
            print("Please specify the location of your data: ")
            stats.onevariablestatistics(readfile.read(input()))
            quit(0)
        if selection == "2":
            print("Please specify the location of your data: ")
            stats.createboxplot(readfile.read(input()))
            quit(0)
        if selection == "3":
            data = input("Please specify the location of your data: ")
            stats.onevariablestatistics(readfile.read(data))
            stats.createboxplot(readfile.read(data))
            quit(0)
        else:
            print("Please input 1, 2, or 3")
            quit(1)

    if selection == "2":
        x = input("Please specify the location of your x-axis data: ")
        y = input("Please specify the location of your y-axis data: ")
        xlabel = input("Please specify your x-axis label: ")
        ylabel = input("Please specify your y-axis label: ")
        title = input("Please specify your graph's title: ")
        stats.linearregression(readfile.read(x), readfile.read(y))
        stats.createlineplot(readfile.read(x), readfile.read(y), xlabel, ylabel, title)
        reex = input("Would you like to automatically re-express your data? (y/n)")
        if reex == "N" or reex == "n":
            quit(0)
        if reex == "Y" or reex == "y":
            stats.reexpress(readfile.read(x), readfile.read(y), xlabel, ylabel, title)
        

    else:
        print("Please input 1 or 2")
        quit(1)
