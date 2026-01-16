Essentially the project started as me wanting to find out more about firmware and how it can be integrated with MCUs. 
Since I had no (real) need for any macro actions, I just decided to keep my design clean & simple, creating nifty volume up-down and brightness up-down buttons. Also created a rotary encoder to act as the tab button when rotated.

Features:
  4 buttons that turn volume up, volume down, brightness up, brightness down respectively (from 1-4)
  .0.91 inch OLED, SSD1306. Programmed with circuit python to display the switch number when a button is pressed.
  EC11 rotary encoder that corresponds to the tab key.

<img width="972" height="680" alt="image" src="https://github.com/user-attachments/assets/bdda1656-4ca5-4943-a737-3dee730fe672" />

    
    My finished schematic, next time I make a similiar design I plan to just use labels to connect components and their legs to a GPIO pin. basically what was done with the OLED but also applied to switches (and other arbitrary/miscallaneous components used).

<img width="462" height="623" alt="image" src="https://github.com/user-attachments/assets/ec1fa104-8217-410f-a6e4-dcb5fcde6118" />


The PCB design I found fairly simplistic, since KiCad is already able to put components on a pcb format once you have assigned it a footprint in the schematic.
After that, routing and rearrangement of components fortunately went smoothly. In hindsight, I probably should have made it slightly larger with a more unique layout (can be remedied if I every try the keyboard tutorial).

<img width="770" height="504" alt="image" src="https://github.com/user-attachments/assets/c7ec0319-f9ae-41e6-b372-84293de0cee5" />

<img width="556" height="633" alt="image" src="https://github.com/user-attachments/assets/0f1b05bd-3fe6-43bf-989c-5f466107935a" />


The CAD model - certainly the hardest part of my design. I have never used 3d software (atleast not to this extent) before, so it was a very steep learning curve. But eventually through looking at tutorials (and ample help from the hackboard tutorial) - I was able to gain some digital literacy and learn enough features to make the case. I also used a 3d model of the pcb to use in the assembled step file.

<img width="693" height="890" alt="image" src="https://github.com/user-attachments/assets/e42884d3-01a9-42f6-a47e-5627576fe614" />


The 3D viewer tool in KiCad enables to see my PCB in a stimulated, 3D format. I saved this as a step file and imported it into the assembled hackpad.

<img width="322" height="216" alt="image" src="https://github.com/user-attachments/assets/a6694dfb-71af-480a-b3fa-f6c999c37588" />

Finally, the BOM list. ALl of the components I will be using are going to be included in the free kit provided - so there is no extra cost or grant I require.However, I have still made a list for clarity.



