Essentially the project started as me wanting to find out more about firmware and how it can be integrated with MCUs. 
Since I had no (real) need for any macro actions, I just decided to keep my design clean & simple, creating nifty volume up-down and brightness up-down buttons. At first, I thought of using a rotary encoder for this but eventually decided against it due to finding them too small and otherwise finnicky.

Features:
  4 buttons that turn volume up, volume down, brightness up, brightness down respectively (from 1-4)
  .0.91 inch OLED, SSD1306. Programmed with circuit python to display the switch number when a button is pressed.
  <img width="867" height="634" alt="image" src="https://github.com/user-attachments/assets/90aee860-71a1-4af5-b7a1-f78fe068ffe6" />
    
    My finished schematic, next time I make a similiar design I plan to just use labels to connect components and their legs to a GPIO pin. basically what was done with the OLED but also applied to switches (and other arbitrary/miscallaneous components used).


  
<img width="636" height="443" alt="image" src="https://github.com/user-attachments/assets/223e8825-69a1-4f47-a05b-d121b7821438" />
