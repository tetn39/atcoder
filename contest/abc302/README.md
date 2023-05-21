# ABC300: A~D
[ABC302](https://atcoder.jp/contests/abc302)

## A問題
ただの割り算、かと思えば指数表記がどうすればいいかわからなかったし、数が大きくて誤差も出たしよくわからなかった

## B問題（未達成）
行列から文字列を探す
sの座標、nの座標の差が1以下の時になんたら？みたいなことをしようとしてややこしすぎてだめだった

## C問題
順列、ハミング距離の問題
個人的にはB問題より簡単だった
sの順列をすべて出し、ハミング距離（前の文字との違い）が1だったら続ける、じゃなかったら終わり。みたいな感じで回していく

## D問題
二分探索な問題
ぱっと見C問題みたいな組み合わせを全通り試せば行けそうだけど、計算量的にダメだろうなと。
そこでAの1つを基準として、Bの中から適した数字を探すってイメージで、Bを昇順に並べて二分探索した

計算量的にはAの数だけ二分探索した計算量（わかんない）だから大丈夫


## 振り返り
A問題が全然わからなくて絶望し、B問題もよくわからなくて絶望した。
でもCとDが比較的早く解けて、Aも解けて一安心
