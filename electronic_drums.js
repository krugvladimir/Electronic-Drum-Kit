// electronic_drums.js — JavaScript версия

const readline = require('readline');
const { exec } = require('child_process');

const drums = {
    '1': { name: 'Бас', freq: 80 },
    '2': { name: 'Снэр', freq: 200 },
    '3': { name: 'Хай-хэт', freq: 1000 },
    '4': { name: 'Том 1', freq: 150 },
    '5': { name: 'Том 2', freq: 120 },
    '6': { name: 'Райд', freq: 800 },
    '7': { name: 'Крэш', freq: 600 },
    '8': { name: 'Перкуссия', freq: 400 }
};

function playSound(freq, duration) {
    const cmd = `beep -f ${freq} -l ${duration}`;
    exec(cmd, (err) => { /* игнорируем ошибки */ });
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log('\x1b[36m🥁 Electronic Drum Kit (JavaScript)\x1b[0m');
console.log('Клавиши для игры:');
console.log('  [1] Бас   [2] Снэр   [3] Хай-хэт');
console.log('  [4] Том1  [5] Том2   [6] Райд');
console.log('  [7] Крэш  [8] Перк');
console.log('Нажмите q для выхода');

rl.on('line', (input) => {
    input = input.trim().toLowerCase();
    if (input === 'q') {
        rl.close();
        return;
    }
    if (drums[input]) {
        const drum = drums[input];
        console.log(`Играем ${drum.name}`);
        // Имитация реверберации
        for (let i = 0; i < 3; i++) {
            playSound(drum.freq + Math.round(drum.freq * 0.02 * i), 30);
        }
    } else {
        console.log('Неизвестная команда.');
    }
});
