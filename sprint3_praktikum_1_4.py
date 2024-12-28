class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt: bool):
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result = []
        for letter in text:
            if (alphabet.find(letter.lower()) == -1):
                result.append(letter)
            else:
                index = alphabet.find(letter.lower())
                if is_encrypt:
                    index = (index + shift) % 33
                else:
                    index = (index - shift) % 33
                result.append(alphabet[index])
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))