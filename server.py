from flask import Flask, request, send_file
import PyPDF2
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('file')
    merger = PyPDF2.PdfFileMerger()

    for file in files:
        merger.append(file)

    output_filename = 'merged.pdf'
    merger.write(output_filename)
    merger.close()

    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
