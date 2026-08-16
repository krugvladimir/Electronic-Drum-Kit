# electronic_drums.rb — Ruby версия

DRUMS = {
  '1' => { name: 'Бас', freq: 80 },
  '2' => { name: 'Снэр', freq: 200 },
  '3' => { name: 'Хай-хэт', freq: 1000 },
  '4' => { name: 'Том 1', freq: 150 },
  '5' => { name: 'Том 2', freq: 120 },
  '6' => { name: 'Райд', freq: 800 },
  '7' => { name: 'Крэш', freq: 600 },
  '8' => { name: 'Перкуссия', freq: 400 }
}

def play_sound(freq, duration)
  system("beep -f #{freq} -l #{duration}")
end

puts "\e[36m🥁 Electronic Drum Kit (Ruby)\e[0m"
puts "Клавиши для игры:"
puts "  [1] Бас   [2] Снэр   [3] Хай-хэт"
puts "  [4] Том1  [5] Том2   [6] Райд"
puts "  [7] Крэш  [8] Перк"
puts "Нажмите q для выхода"

loop do
  print "\e[33m> \e[0m"
  input = gets.chomp.strip.downcase
  break if input == 'q'
  if DRUMS.key?(input)
    drum = DRUMS[input]
    puts "Играем #{drum[:name]}"
    3.times do |i|
      play_sound(drum[:freq] + (drum[:freq] * 0.02 * i).to_i, 30)
      sleep 0.01
    end
  else
    puts "Неизвестная команда."
  end
end
