myApp = App("chrome.app")
if not myApp.window(): # chrome not open
    App.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    wait(10)
myApp.focus()
wait(1)


wait("1392883544404.png", FOREVER)


click("1392883741646.png")

type("http://10.112.18.28/testcases/symbol/BoxMarkerSymbol.html\n")

wait("1392884154681.png", FOREVER)


click("1392882778695.png")
if exists("1392882825935.png"):
    print("create box marker symbol success!")
else:
    print("create box marker symbol fail!")

click("1392884525302.png")
if exists("1392884539217.png"):
    print("create box marker symbol(json) success!")
else:
    print("create box marker symbol(json) fail!")
    
doubleClick("1392885884712.png")

type("55000")
        
click("1392884721664.png")

if exists("1392884749355.png"):
    print("set extent width success!")
else:
    print("set extent width fail!")
doubleClick(find("1392885400212.png").right().find("1392885665897.png"))
type("90000")
        
click("1392884721664.png")

if exists("1392884874286.png"):
    print("set extent height success!")
else:
    print("set extent height fail!")
doubleClick(find("1392885422517.png").right().find("1392885665897.png"))    
type("500000")
        
click("1392884721664.png")

if exists("1392884956412.png"):
    print("set extent depth success!")
else:
    print("set extent depth fail!")

click("1392884996587.png")

if exists("1392885018993.png"):
    print("set tilt + 30 success!")
else:
    print("set tilt + 30 fail!")

click("1392885066449.png")
click("1392885066449.png")

if exists("1392885097714.png"):
    print("set tilt - 30 success!")
else:
    print("set tilt - 30 fail!")

doubleClick("1392885160730.png")
type("145")
click("1392885184156.png")
if exists("1392885212829.png"):
    print("set tilt  success!")
else:
    print("set tilt fail!")

click("1392886744095.png")
click("1392886744095.png")
click("1392886744095.png")
if exists("1392886801194.png"):
    print("set heading + 30 success!")
else:
    print("set heading + 30 fail!")

click("1392886838690.png")
click("1392886838690.png")
if exists("1392886861619.png"):
    print("set heading - 30 success!")
else:
    print("set heading - 30 fail!")


doubleClick(find("1392887108781.png").left().find("1392887121837.png"))
type("90")
click("1392887150799.png")

if exists("1392887181313.png"):
    print("set heading success!")
else:
    print("set heading fail!")
    
dragDrop("1392949672422.png","1392949687298.png" )

click("1392887213432.png")
click("1392887213432.png")
click("1392887213432.png")
if exists("1392887260658.png"):
    print("set up offset success!")
else:
    print("set up offset fail!")
