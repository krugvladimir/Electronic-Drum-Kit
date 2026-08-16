// electronic_drums.rs — Rust версия

use std::collections::HashMap;
use std::io::{self, Write};
use std::process::Command;
use std::thread;
use std::time::Duration;
use colored::*;

struct Drum {
    name: String,
    freq: u32,
}

fn main() {
    let mut drums = HashMap::new();
    drums.insert("1", Drum { name: "Бас".to_string(), freq: 80 });
    drums.insert("2", Drum { name: "Снэр".to_string(), freq: 200 });
    drums.insert("3", Drum { name: "Хай-хэт".to_string(), freq: 1000 });
    drums.insert("4", Drum { name: "Том 1".to_string(), freq: 150 });
    drums.insert("5", Drum { name: "Том 2".to_string(), freq: 120 });
    drums.insert("6", Drum { name: "Райд".to_string(), freq: 800 });
    drums.insert("7", Drum { name: "Крэш".to_string(), freq: 600 });
    drums.insert("8", Drum { name: "Перкуссия".to_string(), freq: 400 });

    println!("{}", "🥁 Electronic Drum Kit (Rust)".cyan());
    println!("Клавиши для игры:");
    println!("  [1] Бас   [2] Снэр   [3] Хай-хэт");
    println!("  [4] Том1  [5] Том2   [6] Райд");
    println!("  [7] Крэш  [8] Перк");
    println!("Нажмите q для выхода");

    loop {
        print!("\x1b[33m> \x1b[0m");
        io::stdout().flush().unwrap();
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let input = input.trim().to_lowercase();
        if input == "q" { break; }

        if let Some(drum) = drums.get(input.as_str()) {
            println!("Играем {}", drum.name);
            // Имитация реверберации
            for i in 0..3 {
                let _ = Command::new("beep")
                    .args(&["-f", &(drum.freq + (drum.freq as f32 * 0.02 * i as f32) as u32).to_string(), "-l", "30"])
                    .status();
                thread::sleep(Duration::from_millis(10));
            }
        } else {
            println!("Неизвестная команда.");
        }
    }
}
