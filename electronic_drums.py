

### 1. `electronic_drums.py` (Python)

```python
# electronic_drums.py — Python версия

import sys
import random
import time
import threading
from colorama import init, Fore, Style

init(autoreset=True)

# Эмуляция звуков с помощью частот (без внешних библиотек)
DRUM_SOUNDS = {
    'kick': {'freq': 80, 'desc': 'Бас'},
    'snare': {'freq': 200, 'desc': 'Снэр'},
    'hihat': {'freq': 1000, 'desc': 'Хай-хэт'},
    'tom1': {'freq': 150, 'desc': 'Том 1'},
    'tom2': {'freq': 120, 'desc': 'Том 2'},
    'ride': {'freq': 800, 'desc': 'Райд'},
    'crash': {'freq': 600, 'desc': 'Крэш'},
    'perc': {'freq': 400, 'desc': 'Перкуссия'}
}

DRUM_KEYS = {
    '1': 'kick', '2': 'snare', '3': 'hihat',
    '4': 'tom1', '5': 'tom2', '6': 'ride',
    '7': 'crash', '8': 'perc'
}

class ElectronicDrums:
    def __init__(self, kit='rock'):
        self.kit = kit
        self.effects = {'reverb': True, 'delay': False}
        self.pattern = []
        self.bpm = 120
        self.recording = False

    def play_sound(self, drum):
        """Воспроизводит звук барабана (эмуляция)"""
        freq = DRUM_SOUNDS[drum]['freq']
        # Добавляем эффекты
        if self.effects['reverb']:
            # Имитация реверберации: короткие эхо
            for i in range(3):
                self._beep(int(freq * (1 + i * 0.02)), 30)
                time.sleep(0.01)
        else:
            self._beep(freq, 100)

    def _beep(self, freq, duration):
        """Воспроизводит звук через системный beep"""
        import os
        if os.name == 'nt':
            import winsound
            winsound.Beep(freq, duration)
        else:
            os.system(f'beep -f {freq} -l {duration} 2>/dev/null')

    def play_pattern(self):
        """Воспроизводит записанный паттерн"""
        if not self.pattern:
            print("Нет записанного паттерна.")
            return
        print(f"Воспроизведение паттерна ({len(self.pattern)} ударов)...")
        step_time = 60 / self.bpm
        for drum in self.pattern:
            self.play_sound(drum)
            time.sleep(step_time)

    def run(self):
        print(f"{Fore.CYAN}🥁 Electronic Drum Kit (Python){Style.RESET_ALL}")
        print(f"Набор сэмплов: {self.kit}")
        print("Клавиши для игры:")
        print("  [1] Бас   [2] Снэр   [3] Хай-хэт")
        print("  [4] Том1  [5] Том2   [6] Райд")
        print("  [7] Крэш  [8] Перк")
        print("  [r] Реверберация  [d] Дилей  [p] Паттерн  [s] Запись")
        print("Нажмите q для выхода")

        while True:
            cmd = input(f"{Fore.YELLOW}> {Style.RESET_ALL}").strip().lower()
            if cmd == 'q':
                break
            elif cmd == 'r':
                self.effects['reverb'] = not self.effects['reverb']
                print(f"Реверберация: {'вкл' if self.effects['reverb'] else 'выкл'}")
            elif cmd == 'd':
                self.effects['delay'] = not self.effects['delay']
                print(f"Дилей: {'вкл' if self.effects['delay'] else 'выкл'}")
            elif cmd == 'p':
                self.play_pattern()
            elif cmd == 's':
                self.recording = not self.recording
                if self.recording:
                    self.pattern = []
                    print("Запись начата...")
                else:
                    print(f"Запись завершена. {len(self.pattern)} ударов.")
            elif cmd in DRUM_KEYS:
                drum = DRUM_KEYS[cmd]
                if self.recording:
                    self.pattern.append(drum)
                desc = DRUM_SOUNDS[drum]['desc']
                print(f"Играем {desc}")
                self.play_sound(drum)
            else:
                print("Неизвестная команда.")

def main():
    kit = input("Выберите набор (rock/electronic/jazz): ").strip().lower()
    if kit not in ['rock', 'electronic', 'jazz']:
        kit = 'rock'
    drums = ElectronicDrums(kit)
    drums.run()

if __name__ == "__main__":
    main()
