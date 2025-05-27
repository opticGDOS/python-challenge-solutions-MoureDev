morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Crear diccionario inverso para decodificar Morse a texto
morse_to_text = {value: key for key, value in morse_code.items()}

entrada = input('Tu texto: ').strip()

if entrada and entrada[0] in ('.', '_', ' '):  
    palabras_morse = entrada.split('  ')  
    texto_traducido = []
    
    for palabra in palabras_morse:
        letras = palabra.split()  #
        palabra_traducida = ''.join(morse_to_text.get(letra, '?') for letra in letras)
        texto_traducido.append(palabra_traducida)

    print('Texto:', ' '.join(texto_traducido))

else:  
    morse = ' '.join(morse_code.get(char.upper(), '?') for char in entrada if char != ' ')
    print('Morse:', morse)

