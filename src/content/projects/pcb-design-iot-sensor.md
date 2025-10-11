---
title: "Custom PCB Design for IoT Sensor Nodes"
summary: "Designed custom printed circuit boards using KiCad for IoT sensor nodes, featuring ESP32 microcontroller, power management, and sensor interfaces."
category: "IoT"
image: ""
tech:
  - KiCad
  - PCB Design
  - ESP32
  - Electronics
  - Hardware Design
bullets:
  - "Designed multi-layer PCB with ESP32 microcontroller and sensor interfaces"
  - "Implemented power management circuit with battery charging capability"
  - "Created schematic and PCB layout following design best practices"
  - "Manufactured and tested prototypes for field deployment"
link: ""
github: ""
date: 2023-06-20
draft: false
---

# Custom PCB Design for IoT Sensor Nodes

This project involved designing custom printed circuit boards (PCBs) for IoT sensor nodes using KiCad. The goal was to create a compact, reliable, and cost-effective solution for deploying sensor networks in various environments.

## Project Requirements

### Functional Requirements
- ESP32-based microcontroller for WiFi connectivity
- Support for multiple sensor types (temperature, humidity, motion)
- Battery-powered with solar charging option
- Low power consumption for extended operation
- Compact form factor for easy deployment

### Design Constraints
- Maximum board size: 50mm x 50mm
- Operating voltage: 3.3V
- Battery life: > 6 months on single charge
- Operating temperature: -20°C to 60°C

## Design Process

### 1. Schematic Design

Key components integrated:
- **ESP32-WROOM-32**: Main microcontroller
- **AMS1117-3.3**: Voltage regulator
- **TP4056**: Li-ion battery charger
- **Sensor Interfaces**: I2C and analog inputs
- **Protection Circuits**: Reverse polarity, overcurrent

### 2. PCB Layout

Design considerations:
- **Layer Stack**: 2-layer board for cost optimization
- **Component Placement**: Logical grouping of functional blocks
- **Routing**: Proper trace widths for power and signal integrity
- **Ground Plane**: Solid ground pour for noise reduction
- **Antenna**: Keep-out zones for WiFi antenna

### 3. Power Management

Implemented efficient power system:
```
Solar Panel → Charge Controller → Li-ion Battery → 
Voltage Regulator → ESP32 & Sensors
```

Features:
- Automatic switching between solar and battery
- Battery level monitoring
- Deep sleep mode support
- Low battery indicator LED

## Technical Highlights

### Signal Integrity
- Proper impedance matching for high-speed signals
- Differential pair routing for USB
- Decoupling capacitors near power pins
- Ground stitching vias for EMI reduction

### Thermal Management
- Thermal relief for power components
- Adequate copper pour for heat dissipation
- Component spacing for airflow

### Manufacturing Considerations
- Design Rule Check (DRC) compliance
- Standard component footprints
- Panelization for cost-effective manufacturing
- Test points for debugging

## Prototyping and Testing

### Prototype Manufacturing
- Ordered from PCB manufacturer (JLCPCB)
- SMD assembly for complex components
- Hand soldering for through-hole parts

### Testing Procedure
1. **Visual Inspection**: Check for manufacturing defects
2. **Continuity Test**: Verify connections with multimeter
3. **Power-On Test**: Check voltage levels
4. **Functional Test**: Program and test each subsystem
5. **Field Test**: Deploy in actual environment

### Issues and Fixes
- **Issue**: WiFi signal strength lower than expected
  - **Fix**: Adjusted antenna placement and added ground plane cutout
- **Issue**: Battery draining faster than calculated
  - **Fix**: Optimized deep sleep implementation in firmware

## Design Files

Project includes:
- Complete KiCad schematic
- PCB layout files
- Bill of Materials (BOM)
- Gerber files for manufacturing
- Assembly drawings
- Test procedures

## Performance Results

Achieved specifications:
- ✅ Battery life: 8+ months with daily transmissions
- ✅ WiFi range: 50+ meters in open space
- ✅ Sensor accuracy: Within manufacturer specifications
- ✅ Cost per unit: < $15 at scale

## Lessons Learned

### Design Phase
- Importance of thorough schematic review
- Value of reference designs from manufacturers
- Need for adequate test points and debugging interfaces

### Manufacturing
- Communication with PCB manufacturer is crucial
- Component availability affects project timeline
- Design for manufacturability saves time and cost

### Testing
- Comprehensive testing catches issues early
- Field testing reveals real-world challenges
- Documentation is essential for troubleshooting

## Skills Developed

- **KiCad Proficiency**: Schematic capture and PCB layout
- **Electronics Knowledge**: Circuit design and analysis
- **Manufacturing Process**: Understanding PCB fabrication
- **Testing Methodology**: Systematic approach to validation
- **Documentation**: Creating clear technical documentation

## Future Improvements

- Add LoRa module for long-range communication
- Implement USB-C for modern connectivity
- Design 4-layer board for better signal integrity
- Add more sensor interfaces
- Create modular design for different applications

## Applications

This PCB design has been used for:
- Environmental monitoring stations
- Smart agriculture sensors
- Building automation systems
- Industrial condition monitoring

## Conclusion

This project demonstrates the complete PCB design workflow from concept to production. It combines electrical engineering knowledge with practical manufacturing considerations, resulting in a reliable and cost-effective IoT sensor platform.

The experience gained in PCB design complements my software skills, enabling me to create complete IoT solutions that integrate hardware and software seamlessly.
