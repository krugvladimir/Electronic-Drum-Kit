// ElectronicDrums.java — Java версия

import java.util.HashMap;
import java.util.Scanner;

public class ElectronicDrums {
    private static final HashMap<String, Drum> drums = new HashMap<>();
    
    static class Drum {
        String name;
        int freq;
        Drum(String name, int freq) { this.name = name; this.freq = freq; }
    }

    static {
        drums.put("1", new Drum("Бас", 80));
        drums.put("2", new Drum("Снэр", 200));
        drums.put("3", new Drum("Хай-хэт", 1000));
        drums.put("4", new Drum("Том 1", 150));
        drums.put("5", new Drum("Том 2", 120));
        drums.put("6", new Drum("Райд", 800));
        drums.put("7", new Drum("Крэш", 600));
        drums.put("8", new Drum("Перкуссия", 400));
    }

    private static void playSound(int freq, int duration) {
        try {
            Runtime.getRuntime().exec(new String[]{"beep", "-f", String.valueOf(freq), "-l", String.valueOf(duration)});
        } catch (Exception e) { /* ignored */ }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\u001B[36m🥁 Electronic Drum Kit (Java)\u001B[0m");
        System.out.println("Клавиши для игры:");
        System.out.println("  [1] Бас   [2] Снэр   [3] Хай-хэт");
        System.out.println("  [4] Том1  [5] Том2   [6] Райд");
        System.out.println("  [7] Крэш  [8] Перк");
        System.out.println("Нажмите q для выхода");

        while (true) {
            System.out.print("\u001B[33m> \u001B[0m");
            String input = scanner.nextLine().trim().toLowerCase();
            if (input.equals("q")) break;
            if (drums.containsKey(input)) {
                Drum d = drums.get(input);
                System.out.println("Играем " + d.name);
                // Имитация реверберации
                for (int i = 0; i < 3; i++) {
                    playSound(d.freq + (int)(d.freq * 0.02 * i), 30);
                    try { Thread.sleep(10); } catch (Exception e) {}
                }
            } else {
                System.out.println("Неизвестная команда.");
            }
        }
        scanner.close();
    }
}
