## 使用技術
![Static Badge](https://img.shields.io/badge/python-blue)
![Static Badge](https://img.shields.io/badge/PIL-black)
![Static Badge](https://img.shields.io/badge/pytesseract-black)
![Static Badge](https://img.shields.io/badge/pdf2image-black)
![Static Badge](https://img.shields.io/badge/poppler-brown)

# pdf_to_img

## プロジェクトの概要
pdfを画像に変換して，特定領域を新たな画像として抽出し，その画像から文字列を抽出するモジュール．

## 環境
| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| python                | 3.11.5     |

## ディレクトリ構成
```
.
├── manager.py
└── modules
    ├── __init__.py
    ├── __pycache__
    │   ├── CropImages.cpython-311.pyc
    │   ├── __init__.cpython-311.pyc
    │   ├── convertToImage.cpython-311.pyc
    │   ├── def_name.cpython-311.pyc
    │   ├── img_crop.cpython-311.pyc
    │   └── pdf_to_img.cpython-311.pyc
    ├── det_name.py
    ├── img_crop.py
    ├── pdf_to_img.py
    └── requirements.txt
```

## ライブラリのインストール
```
pip install -r requirements.txt
```
```
brew install poppler
```
