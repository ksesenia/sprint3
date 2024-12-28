class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result = []
        for letter in original_text:
            if (alphabet.find(letter.lower()) == -1):
                result.append(letter)
            else:
                index = alphabet.find(letter.lower())
                index = (index+shift) % 33
                result.append(alphabet[index])
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result = []
        for letter in cipher_text:
            if (alphabet.find(letter.lower()) == -1):
                result.append(letter)
            else:
                index = alphabet.find(letter.lower())
                index = (index - shift) % 33
                result.append(alphabet[index])

        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))