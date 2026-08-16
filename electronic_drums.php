<?php
// electronic_drums.php — PHP версия

$drums = [
    '1' => ['name' => 'Бас', 'freq' => 80],
    '2' => ['name' => 'Снэр', 'freq' => 200],
    '3' => ['name' => 'Хай-хэт', 'freq' => 1000],
    '4' => ['name' => 'Том 1', 'freq' => 150],
    '5' => ['name' => 'Том 2', 'freq' => 120],
    '6' => ['name' => 'Райд', 'freq' => 800],
    '7' => ['name' => 'Крэш', 'freq' => 600],
    '8' => ['name' => 'Перкуссия', 'freq' => 400]
];

function play_sound($freq, $duration) {
    exec("beep -f $freq -l $duration");
}

echo "\033[36m🥁 Electronic Drum Kit (PHP)\033[0m\n";
echo "Клавиши для игры:\n";
echo "  [1] Бас   [2] Снэр   [3] Хай-хэт\n";
echo "  [4] Том1  [5] Том2   [6] Райд\n";
echo "  [7] Крэш  [8] Перк\n";
echo "Нажмите q для выхода\n";

while (true) {
    echo "\033[33m> \033[0m";
    $input = trim(fgets(STDIN));
    $input = strtolower($input);
    if ($input == 'q') break;
    if (isset($drums[$input])) {
        $d = $drums[$input];
        echo "Играем {$d['name']}\n";
        for ($i = 0; $i < 3; $i++) {
            play_sound($d['freq'] + (int)($d['freq'] * 0.02 * $i), 30);
            usleep(10000);
        }
    } else {
        echo "Неизвестная команда.\n";
    }
}
?>
