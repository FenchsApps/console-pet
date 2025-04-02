

---

# 🐾 Console Pet — Terminal-Based Virtual Pet Simulator  

**Console Pet** is a Python-based terminal game where you care for a digital dog named *Nimbus*. Keep it fed, happy, and alive—or face the consequences!  

## 🚀 Features  
- **Real-time stats**: Hunger and happiness decay over time.  
- **Interactive commands**: Feed, play, or (cruelly) hurt your pet.  
- **ASCII art visuals**: Cute terminal-based dog.  
- **Dynamic responses**: Pet reacts to your actions.  

---

## ⚙️ Installation  

### Requirements  
- Python 3.7+  
- `pip` package manager  

### Steps  
1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/console-pet.git
   cd console-pet
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
   *(If no `requirements.txt`, manually install:)*  
   ```bash
   pip install pyfiglet rich
   ```

3. Run the game:  
   ```bash
   python3 console_pet.py
   ```

---

## 🎮 Usage  

### Commands  
| Command           | Action                          | Effect                     |
|-------------------|---------------------------------|----------------------------|
| `pet --feed`      | Feed Nimbus                     | `+20 Hunger`, `+10 Happy`  |
| `pet --play`      | Play with pet                   | `+15 Happy`, `-10 Hunger`  |
| `pet --woof`      | Make Nimbus bark                | `+5 Happy`                 |
| `pet --stats`     | Show current stats              | Displays hunger/happiness  |
| `pet --hurt`      | Hurt Nimbus (😢)               | `-20 Happy`                |
| `pet --settings`  | Change pet name                 | Updates name               |
| `pet --exit`      | Quit game                       | Exits program              |

### Game Mechanics  
- **Hunger**: Decreases by **4 every 5 seconds** (starves at 0).  
- **Happiness**: Critical at 0 (pet runs away).  

---

## 📦 Compilation (Optional)  

### Linux (PyInstaller)  
```bash
pip install pyinstaller
pyinstaller --onefile console_pet.py
# Binary: ./dist/console_pet
```

### Windows  
```bash
pyinstaller --onefile --windowed --icon=icon.ico console_pet.py
```

---

## 🏗️ Project Structure  
```
.
├── console_pet.py      # Main game script
├── README.md           # This documentation
├── requirements.txt    # Dependencies
└── assets/             # (Optional) Icons/fonts
```

---

## 💻 Code Snippet  
```python
def feed():
    global HUNGER, HAPPY
    HUNGER = min(HUNGER + 20, 100)  # Cap hunger at 100
    print(f"{NAME} happily eats the food!")
```

---

## 🤝 Contributing  
1. Fork the repository.  
2. Create a branch:  
   ```bash
   git checkout -b feature/your-feature
   ```  
3. Submit a **Pull Request**.  

---

## 📜 License  
MIT. See [LICENSE](LICENSE) for details.  

---

### 🛠️ To-Do  
- [ ] Add more pet reactions  
- [ ] Implement mini-games  
- [ ] Save/load progress  

**Star ⭐ the repo if you love it!**  

--- 
