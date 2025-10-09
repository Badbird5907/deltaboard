# Deltaboard

Deltaboard is a TKL mechanical keyboard, directly using the [Keychron K8](https://www.keychron.com/products/keychron-k8-tenkeyless-wireless-mechanical-keyboard) as inspiration.
The hardest part building this project was routing all the switches and components for the RP2040.

## Features:
- TKL Layout
- Kailh MX hotswap sockets
- OLED display
- Integrated RP2040
- USB-C
- RGB lighting
- EC11 Encoder
- QMK/VIA firmware

## Screenshots

### Schematic
![Schematic](https://raw.githubusercontent.com/Badbird5907/deltaboard/refs/heads/master/images/schematics.png)

### PCB
![PCB](https://raw.githubusercontent.com/Badbird5907/deltaboard/refs/heads/master/images/pcb.png)

### Front
![Front](https://raw.githubusercontent.com/Badbird5907/deltaboard/refs/heads/master/images/front.png)

### Back
![Back](https://raw.githubusercontent.com/Badbird5907/deltaboard/refs/heads/master/images/back.png)

### Case
![Case](https://raw.githubusercontent.com/Badbird5907/deltaboard/refs/heads/master/images/Render.PNG)

## BOM

| Name                     | Quantity | $ Total (USD) | Notes                                          | Links                                                                                                 |
|--------------------------|----------|---------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Cherry MX2A Brown RGB    | 84       | $35.92        | 90x, Free shipping (0.42c/switch)              | [Aliexpress](https://www.aliexpress.com/item/1005007917791662.html)                                   |
| DUROCK Stabilizer        | 1        | $8.74         | V3 BS 4x2u 1x6.25u                             | [Aliexpress](https://www.aliexpress.com/item/1005006528731543.html)                                   |
| M3 Heat Insert           | 1        | $2.39         | 50x, Free shipping                             | [Aliexpress](https://www.aliexpress.com/item/1005003582355741.html)                                   |
| M3 Screws (6mm)          | 1        | $1.94         | 50x, Free shipping                             | [Aliexpress](https://www.aliexpress.com/item/4001199728978.html)                                      |
| Wormier Pudding Keycaps   | 1        | $17.91        |                                                | [Amazon](https://www.amazon.ca/XVX-Keycaps-Universal-Compatiability-Keyboard/) |
| Kailh MX Hotswap Sockets | 90       | $11.35        | 50x + 30x + 10x, Free shipping                 | [Aliexpress](https://www.aliexpress.com/item/1005007225352311.html)                                   |
| I2C OLED Display (0.91") | 1        | $2.25         | Free shipping                                  | [Aliexpress](https://www.aliexpress.com/item/1005005301005280.html)                                   |
| EC11 Rotary Encoders     | 1        | $3.40         | 20mm Half Handle, Free shipping                | [Aliexpress](https://www.aliexpress.com/item/1005004907970664.html)                                   |
| Encoder Cap              | 1        | $2.23         | Half Handle Lid, Free shipping                 | [Aliexpress](https://www.aliexpress.com/item/1005004907970664.html)                                   |
| LCSC Parts               | 1        | $27.33        | $12.47 total, $3 handling fee, $11.86 shipping. This covers both MCU and diodes / leds. | [BOM](https://github.com/Badbird5907/deltaboard/blob/master/Production/PCB/BOM-deltaboard.csv)        |
| PCB                      | 1        | 35.93         | 20.70 pcb + 15.23 shipping                     |
**TOTAL: 149.39 USD**
