import census2010

print("Which state would you like data for?")

State = raw_input("> ")
if State in census2010.allData:
    print("Next question.")
else:
    print("State not found!")
    exit()

print("Which county within %s") % State

County = raw_input("> ")
if County in census2010.allData['%s' % State]:
    requestPop = census2010.allData[('%s') % State][('%s') % County]['pop']
    print('The 2010 population of %s was ' + str(requestPop)) % (County)

    requestTracts = census2010.allData[('%s') % State][('%s') % County]['tracts']
    print('The amount of tracts for %s was ' + str(requestTracts)) % County
else:
    print("County not found!")
    exit()
