# 復習問題

## years_listの作成
years_list = ['1994', '1995', '1996', '1997', '1998']
print(years_list)

## 3番目の要素をみる
print(years_list[2])

## 末尾の要素をみる
print(years_list[-1])

## thingsリストを作成する
things = ['mozzarella', 'cinderella', 'salmonella']
print(things)

## thingsの要素で人間を参照しているものをタイトルケースにして表示する
things[1].capitalize()
print(things)

## チーズの要素を大文字にしてリスト表示
things[0] = things[0].upper()
print(things)

## 病気に関連する要素を削除してリストを表示
things.remove('salmonella')
print(things)

## surpriseリストを作成する
surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise)

## 最後の要素を小文字にして、逆順にしてから先頭文字を大文字に戻す。
ele = surprise.pop().lower()[::-1].upper()
surprise.append(ele)
print(surprise)