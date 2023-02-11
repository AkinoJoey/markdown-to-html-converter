# マークダウンを HTML に変換するプログラムを作成
# ex. python3 file-converter.py markdown inputfile outputfile
# markdown は実行するコマンド、inputfile は .md ファイルへのパス、出力パスはプログラムを実行した後に作成される .html です。

import markdown
import sys

inputfilePath = sys.argv[2]
outputFilePath = sys.argv[3]

with open(inputfilePath, "r", encoding="utf-8") as f:
    markdownString = f.read()

htmlString = markdown.markdown(markdownString,extensions=['extra'])

with open(outputFilePath,"w") as f:
    f.write(htmlString)


