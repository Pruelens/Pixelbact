# Pixelbact
This is a very rough script to generate Opentrons python files that can be used to spot pixel agar art. 
If you find it interesting and would like to know more about how it works, you can send me a message.

### How to:

Open the colorexcel.xlsx file and color in one of the Sheets by typing the number corresponding with a color. On the right side of the canvas you can find the legend.

Run "python getcoords.py"    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enter the name of the Sheet which you want to generate the OT python file of.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enter a name for your design
 
To use the generated design you will need an Opentrons with a P10. Additionally, you'll need to add '1828grid_504_wellplate_1ul.json' as a custom labware.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Load the OT python file  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Position a square petridish in the middle of position 5 of the OT deck.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calibrate the pipette that it nearly touches the agar.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Press run and enjoy the show...  

<p align="center">

  <img src="https://user-images.githubusercontent.com/13136496/233967796-28c6eb54-7cc2-4687-b8ef-652ca340d17a.png" width="480">

</p>
