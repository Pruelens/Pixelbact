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

<p align="center">

  <img src="https://user-images.githubusercontent.com/13136496/233967796-28c6eb54-7cc2-4687-b8ef-652ca340d17a.png" width="480">

</p>
