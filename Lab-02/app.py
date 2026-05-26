from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# index
@app.route("/")
def home():
    return render_template('index.html')

# CAESAR
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)

    return render_template(
        'caesar.html',
        encrypted_text=encrypted_text,
        plain_text=text,
        key=key
    )

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)

    return render_template(
        'caesar.html',
        decrypted_text=decrypted_text,
        cipher_text=text,
        key=key
    )
    
# VIGENERE
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = VigenereCipher()
    encrypted_text = cipher.vigenere_encrypt(text, key)
    return f"<h3>Vigenere - Encrypt</h3>text: {text}<br/>key: {key}<br/>encrypted text: <b>{encrypted_text}</b><br/><br/><a href='/vigenere'>← Back</a>"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return f"<h3>Vigenere - Decrypt</h3>text: {text}<br/>key: {key}<br/>decrypted text: <b>{decrypted_text}</b><br/><br/><a href='/vigenere'>← Back</a>"

# RAIL FENCE
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, key)
    return f"<h3>Rail Fence - Encrypt</h3>text: {text}<br/>rails: {key}<br/>encrypted text: <b>{encrypted_text}</b><br/><br/><a href='/railfence'>← Back</a>"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, key)
    return f"<h3>Rail Fence - Decrypt</h3>text: {text}<br/>rails: {key}<br/>decrypted text: <b>{decrypted_text}</b><br/><br/><a href='/railfence'>← Back</a>"

# PLAYFAIR
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted_text = cipher.playfair_encrypt(text, matrix)
    return f"<h3>Playfair - Encrypt</h3>text: {text}<br/>key: {key}<br/>matrix: {matrix}<br/>encrypted text: <b>{encrypted_text}</b><br/><br/><a href='/playfair'>← Back</a>"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted_text = cipher.playfair_decrypt(text, matrix)
    return f"<h3>Playfair - Decrypt</h3>text: {text}<br/>key: {key}<br/>matrix: {matrix}<br/>decrypted text: <b>{decrypted_text}</b><br/><br/><a href='/playfair'>← Back</a>"

# TRANSPOSITION
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = TranspositionCipher()
    encrypted_text = cipher.encrypt(text, key)
    return f"<h3>Transposition - Encrypt</h3>text: {text}<br/>key: {key}<br/>encrypted text: <b>{encrypted_text}</b><br/><br/><a href='/transposition'>← Back</a>"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = TranspositionCipher()
    decrypted_text = cipher.decrypt(text, key)
    return f"<h3>Transposition - Decrypt</h3>text: {text}<br/>key: {key}<br/>decrypted text: <b>{decrypted_text}</b><br/><br/><a href='/transposition'>← Back</a>"

# MAIN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)