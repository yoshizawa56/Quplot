# Quplot
PyQtによるmatplotlibのGUIアプリ
![DEMO](https://github.com/yoshizawa56/Quplot/blob/master/screen.gif)

# インストール方法
## MAC
[https://github.com/yoshizawa56/Quplot_mac/releases](https://github.com/yoshizawa56/Quplot_mac/releases) から圧縮ファイルをダウンロード。
圧縮ファイルを解凍して、解答されたファイルをAppricationに追加して使用しようしてください。

## Windows
未対応（対応予定）

# 使い方

# データ形式
テキスト形式とCSV形式に対応しています。

## コメント
- テキスト、CSVともに共通。
- 「#」がコメントとして認識されます。
- ファイルの1行目が「##」から始まる場合は、列名と認識します。
- ファイルの2行目が「##」から始まる場合は、プロットの際に表示する列のラベル（LaTeX表式）と認識します。
- 「##」行では「スペースタブ」を区切り文字として、各列を認識します。

例）
```
##x   sin_x   cos_x   log_x
##x   \sin x  \cos x  \log x
```

## テキスト形式
区切り文字はスペースまたはタブ

## CSV形式
区切り文字はカンマ
