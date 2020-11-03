import PlotData as pd
import ReadFile as rf
import Stats as st
xdata = rf.read("x.txt")
ydata = rf.read("y.txt")
st.linearregression(xdata, ydata)
