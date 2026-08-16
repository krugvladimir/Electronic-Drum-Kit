// electronic_drums.cs — C# версия

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

class ElectronicDrums
{
    static Dictionary<string, (string name, int freq)> drums = new Dictionary<string, (string, int)>
    {
        {"1", ("Бас", 80)}, {"2", ("Снэр", 200)}, {"3", ("Хай-хэт", 1000)},
        {"4", ("Том 1", 150)}, {"5", ("Том 2", 120)}, {"6", ("Райд", 800)},
        {"7", ("Крэш", 600)}, {"8", ("Перкуссия", 400)}
    };

    static void PlaySound(int freq, int duration)
    {
        try
        {
            Process.Start("beep", $"-f {freq} -l {duration}");
        }
        catch
        {
            Console.Beep(freq, duration);
        }
    }

    static void Main()
    {
        Console.WriteLine("\u001B[36m🥁 Electronic Drum Kit (C#)\u001B[0m");
        Console.WriteLine("Клавиши для игры:");
        Console.WriteLine("  [1] Бас   [2] Снэр   [3] Хай-хэт");
        Console.WriteLine("  [4] Том1  [5] Том2   [6] Райд");
        Console.WriteLine("  [7] Крэш  [8] Перк");
        Console.WriteLine("Нажмите q для выхода");

        while (true)
        {
            Console.Write("\u001B[33m> \u001B[0m");
            string input = Console.ReadLine().Trim().ToLower();
            if (input == "q") break;
            if (drums.ContainsKey(input))
            {
                var d = drums[input];
                Console.WriteLine($"Играем {d.name}");
                for (int i = 0; i < 3; i++)
                {
                    PlaySound(d.freq + (int)(d.freq * 0.02 * i), 30);
                    Thread.Sleep(10);
                }
            }
            else
            {
                Console.WriteLine("Неизвестная команда.");
            }
        }
    }
}
