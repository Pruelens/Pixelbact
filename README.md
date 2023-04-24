# pixelbact
A custom script 

This is a very rough script to generate Opentrons python file that can be used to spot pixel agar art. 
If you find it interesting and would like to understand how it works, you can send me a message.

How to:
Open the colorexcel.xlsx file and color in one of the Sheets by typing the number corresponding with a color. On the right side of the canvas you can find the legend.

Run "python getcoords.py"
  Enter the name of the Sheet which you want to generate the OT python file of.
  Enter a name of your design
 
To use the generated design you will need an Opentrons with a P10. Additionally, you'll need to add '1828grid_504_wellplate_1ul.json' as a custom labware.
  Load the OT python file
  Position a square petridish in the middle of position 5 of the OT deck.
  Calibrate the pipette that it nearly touches the agar
  Press run and enjoy the show...
  
![image](https://user-images.githubusercontent.com/13136496/233966003-2d9a5aa3-28e9-4d44-9e38-ddb33ba4d9ae.png)
