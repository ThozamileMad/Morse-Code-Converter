
let_num = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

morse_code = ["● ▬", "▬ ● ● ●", "▬ ● ▬ ●", "▬ ● ●", "●", "● ● ▬ ●", "▬ ▬ ●",
              "● ● ● ●", "● ●", "● ▬ ▬ ▬", "▬ ● ▬", "● ▬ ● ●", "▬ ▬", "▬ ●",
              "▬ ▬ ▬", "● ▬ ▬ ●", "▬ ▬ ● ▬", "● ▬ ●", "● ● ●", "▬", "● ● ▬",
              "● ● ● ▬", "● ▬ ▬", "▬ ● ● ▬", "▬ ● ▬ ▬", "▬ ▬ ● ●",
              '● ▬ ▬ ▬ ▬', '● ● ▬ ▬ ▬', '● ● ● ▬ ▬', '● ● ● ● ▬', '● ● ● ● ●',
              '▬ ● ● ● ●', '▬ ▬ ● ● ●', '▬ ▬ ▬ ●●', '▬ ▬ ▬ ▬ ●', '▬ ▬ ▬ ▬ ▬']

morse_code_dict = {k: v for k, v in zip(let_num, morse_code)}

print("Morse Code Converter.")

convert = "y"
while convert == "y":
    string = input("\nEnter string: ").upper()
    conversion_lst = [morse_code_dict[item] for item in string if item in let_num]
    conversion = "   ".join(conversion_lst)
    print(f"\nConversion:\n{conversion}")

    convert = input("\nEnter y to continue converting or n to stop: ").lower()

