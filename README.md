# Personal Assistant Robot Project

This repository contains the full implementation of a voice-controlled personal assistant robot developed as a bachelor thesis project at Stamford University Bangladesh. The robot features voice interaction, autonomous navigation, and various assistant functionalities.

## 📋 Project Overview
A personal assistant robot prototype designed to:
- Respond to voice commands
- Provide weather, time, and Wikipedia information
- Navigate indoor environments autonomously
- Assist with daily tasks through voice interaction

[![Project Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/0.jpg)](https://youtube.com/demo-link)

## ✨ Key Features
- **Voice Interaction**:
  - Speech recognition via Wit.ai
  - Text-to-speech using eSpeak
  - Voice command processing
- **Assistant Functions**:
  - Weather information retrieval
  - Time and schedule management
  - Wikipedia knowledge queries
  - iPhone locating functionality
- **Robotics**:
  - 360-degree manipulator
  - Fuzzy behavior-based navigation
  - Face recognition and tracking
- **Hardware Integration**:
  - Raspberry Pi 3 as main controller
  - Arduino Mega for motor control
  - Custom chassis with 4-wheel drive

## 🛠️ Hardware Requirements
| Component | Specification |
|-----------|---------------|
| Main Controller | Raspberry Pi 3 Model B |
| Motor Controller | Arduino Mega 2560 |
| Motors | 4x DC Gear Motors (6V) |
| Servos | MG996R (10kg torque) |
| Power | 2x LiPo Batteries (7.4V) |
| Sensors | USB Webcam, Microphone |
| Chassis | Custom fiberglass platform |
| Wheels | 65mm Rubber Wheels |

## 💻 Software Stack
- **OS**: Raspberry Pi OS (Stretch)
- **Speech Processing**: Wit.ai + eSpeak
- **Core Programming**: Python 2.7
- **Arduino Programming**: C++
- **Libraries**:
  - PyAudio
  - OpenCV
  - RPi.GPIO
  - Arduino Motor Shield Library

## 🚀 Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/haqueabdali/personal-assistant-robot.git
cd personal-assistant-robot
```

### 2. Hardware Setup
Follow the [Hardware Assembly Guide](https://github.com/haqueabdali/personal-assistant-robot/blob/master/docs/ASSEMBLY.md) for detailed connection instructions.

### 3. Software Installation
```bash
# Install dependencies
sudo apt-get update
sudo apt-get install espeak python-pyaudio python-opencv

# Configure API keys
cp config.example.yaml config.yaml
nano config.yaml  # Add your Wit.ai and other API keys
```

### 4. Flash Arduino
```bash
cd arduino
platformio run --target upload
```

## 🎮 Usage
```bash
# Start the main application
python main.py

# Basic voice commands:
"JOHN, what's the weather?"
"JOHN, what time is it?"
"JOHN, find my iPhone"
"JOHN, move forward"
```

## 📂 Project Structure
```
├── arduino/           # Motor control code
├── docs/              # Project documentation
├── images/            # System diagrams and photos
├── src/               # Python source code
│   ├── brain.py       # Command processing
│   ├── mic.py         # Audio handling
│   ├── stt.py         # Speech-to-text
│   └── tts.py         # Text-to-speech
├── config.yaml        # Configuration file
└── requirements.txt   # Python dependencies
```

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Supervisor: Asma-ull-Hosna (Stamford University Bangladesh)
- Hardware Reference: Raspberry Pi Foundation
- Speech API: Wit.ai
- [Full Project Documentation](https://github.com/haqueabdali/personal-assistant-robot/blob/master/docs/FINAL_REPORT.pdf)

---
**Note**: This is a legacy academic project. Some components may require updating for modern systems. For support, create an issue in the repository.  
