Essentially the project started as me wanting to find out more about firmware and how it can be integrated with MCUs. 
Since I had no (real) need for any macro actions, I just decided to keep my design clean & simple, creating nifty volume up-down and brightness up-down buttons. At first, I thought of using a rotary encoder for this but eventually decided against it due to finding them too small and otherwise finnicky.

Features:
  4 buttons that turn volume up, volume down, brightness up, brightness down respectively (from 1-4)
  .0.91 inch OLED, SSD1306. Programmed with circuit python to display the switch number when a button is pressed.
  <img width="867" height="634" alt="image" src="https://github.com/user-attachments/assets/90aee860-71a1-4af5-b7a1-f78fe068ffe6" />
    
    My finished schematic, next time I make a similiar design I plan to just use labels to connect components and their legs to a GPIO pin. basically what was done with the OLED but also applied to switches (and other arbitrary/miscallaneous components used).

<img width="546" height="803" alt="image" src="https://github.com/user-attachments/assets/de4965e1-3f0f-4501-b733-3233c025a5bf" />

The PCB design I found fairly simplistic, since KiCad is already able to put components on a pcb format once you have assigned it a footprint in the schematic.
After that, routing and rearrangement of components fortunately went smoothly.

<img width="636" height="443" alt="image" src="https://github.com/user-attachments/assets/223e8825-69a1-4f47-a05b-d121b7821438" />

The CAD model - certainly the hardest part of my design. I have never used 3d software (atleast not to this extent) before, so it was a very steep learning curve. But eventually through looking at tutorials (and ample help from the hackboard tutorial) - I was able to gain some digital literacy and learn enough features to make the case. I also used a 3d model of the pcb to use in the assembled step file.

<img width="532" height="736" alt="image" src="https://github.com/user-attachments/assets/75e22d51-d48b-4fb9-a5d5-1c0fd1cc562c" />

The 3D viewer tool in KiCad enables to see my PCB in a stimulated, 3D format. I saved this as a step file and imported it into the assembled hackpad.

<img width="397" height="195" alt="image" src="https://github.com/user-attachments/assets/8a344bd4-3370-4aa2-adab-f993d98a47eb" />

Finally, the BOM list. ALl of the components I will be using are going to be included in the free kit provided - so there is no extra cost or grant I require.However, I have still made a list for clarity.



