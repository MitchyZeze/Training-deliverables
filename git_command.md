## git ブランチモデル

### ブランチの種類

- master
  - リリース時点のソースコードを管理するブランチ
- develop(master から派生)
  - 開発作業の主軸となるブランチ
- feature(develop から派生)
  - 実装する機能毎のブランチ(feature/○○, feature/xx など)
- release
  - develop での開発作業完了後、リリース時の微調整を行うブランチ
- hotfix
  - リリースされた製品に致命的なバグ(クラッシュなど)があった場合に緊急対応するためのブランチ

### ブランチモデル

#### 開発作業の流れ

1. master ブランチから develop ブランチを作成
1. develop ブランチから実装する機能毎に feature ブランチを作成
1. feature ブランチで実装完了した機能は develop ブランチにマージ
1. リリース作業開始時点で、develop から release ブランチを作成
1. リリース作業完了時点で、release から develop,master ブランチにマージ

#### リリース後の障害対応の流れ

1. master ブランチから hotfix ブランチを作成
1. hotfix ブランチで障害対応が完了した時点で、develop,master ブランチにマージ

## Git command

| idx  | command 名  |                             command 構文                             |                                                  機能                                                   |
| :--: | :---------: | :------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: |
|  1   |    init     |                              `git init`                              |                                           git の準備をする。                                            |
|  2   |     add     |                         `git add ファイル名`                         |                                      共有するファイル選択をする。                                       |
| 3.1  |   commit    |                     `git commit -m "メッセージ"`                     |                                      選択したファイルを記録する。                                       |
| 3.2  |   commit    |                         `git commit --amend`                         |              コミットメッセージの修正。vim が立ち上がり、修正後保存してエディタを閉じる。               |
| 3.3  |   commit    |                    `git commit -am "メッセージ"`                     |                                   add してコミットする一連のコマンド                                    |
|  4   |   remote    |                   `git remote add リモート名 URL`                    |                                      リモートを登録する。(補足 1)                                       |
| 5.1  |    push     |                     `git push リモート名 master`                     |                                 リモートにファイルをアップデートする。                                  |
| 5.2  |    push     | `git push --force-with-lease origin git rev-parse --abbrev-ref HEAD` |                                現在のブランチを origin に強制 push する                                 |
| 5.3  |    push     |          `git push origin git rev-parse --abbrev-ref HEAD`           |                                 現在の美ブランチを origin に push する                                  |
|  6   |   branch    |                             `git branch`                             |                                        ブランチの一覧を表示する                                         |
|  7   |    pull     |                     `git pull リモート名 master`                     |                                 リモートのファイルの変更点を取得する。                                  |
| 8.1  |   status    |                            `git status `                             |                                    コミット後のファイルを把握する。                                     |
| 8.2  |   status    |                             `git status`                             |                                  add したファイルを確認する。(補足 2)                                   |
|  9   |    diff     |                             `git diff `                              |                                      変更内容を把握する。(補足 3)                                       |
| 10.1 |     log     |                              `git log`                               |                    リポジトリにコミットされたログメッセージを確認することができる。                     |
| 10.2 |     log     |                             `git log -p`                             |                                変更差分を確認することができる。(補足 4)                                 |
| 10.3 |     log     |                       `git log --prety=short`                        |                                コミットメッセージの 1 行目のみを表示する                                |
| 10.4 |     log     |                          `git log --graph`                           |                                       ブランチを視覚的に確認する                                        |
| 11.1 |  checkout   |                        `git checkout master`                         |                                       master ブランチへ切り替える                                       |
| 11.2 |  checkout   |                           `git checkout -`                           |                                      1 つ前のブランチに切り替える                                       |
| 11.3 |  checkout   |                      `git checkout -b feature`                       |                                  feature ブランチを作成して切り替える                                   |
|  12  |    merge    |                     `git merge --no-ff feature`                      |    feature ブランチを master にマージする。マージコミットのメッセージ入力で vim が立ち上がる(補足 5)    |
| 13.1 |    reset    |                     `git reset --hard ハッシュ`                      |                                      ハッシュ値まで前の状態に戻す                                       |
| 13.2 |    reset    |                        `git reset HEAD~数字`                         |                               HEAD から数字分前のコミットへとリセットする                               |
| 13.3 |    reset    |                       `git reset HEAD@{数字}`                        |                   git reflog で管理されている HEAD から数字分前の状態へとリセットする                   |
| 13.3 |    reset    |                 `git reset --hard origin/ブランチ名`                 |                                 origin のブランチへリセットする(補足 7)                                 |
|  14  |   reflog    |                             `git reflog`                             |               git コマンドで行われた変更のログを確認できる。元の状態に復元することも可能                |
| 15.1 |   rebase    |                        `git rebase -i HEAD~2`                        | 歴史を改ざんする。現在のブランチの HEAD を含めた 2 つまでの歴史を対象としてエディタが立ち上がる(補足 6) |
| 15.2 |   rebase    |                       `git rebase ブランチ名`                        |                                       別ブランチの変更を取り込む                                        |
| 15.3 |   rebase    |                       `git rebase --continue`                        |                                         rebase を続ける(補足 8)                                         |
| 16.1 |    stash    |                             `git stash`                              |                                           変更を一時退避する                                            |
| 16.2 |    stash    |                           `git stash pop`                            |                                   git stash で一時退避した変更を戻す                                    |
|  17  |    fetch    |                             `git fetch`                              |                        リモートの変更点を取得する(pull と違ってマージはされない)                        |
|  18  |    clone    |                      `git clone リポジトリURL`                       |                                          リポジトリを複製する                                           |
|  19  |    blame    |                        `git blame ファイル名`                        |                                      ファイルの変更履歴を確認する                                       |
|  20  | cherry-pick |                      `git cherry-pick ハッシュ`                      |                                  ハッシュで指定したコミットを取り込む                                   |

# 補足

1. > 一般的には「origin」として登録されている。
2. > add されたファイルが緑色、add されていないファイルが赤色で表示される。
3. > 変更前のコードが赤色、変更後のコードが緑色で表示される。
4. > 上下キーで常時範囲を変えることができ、Q キーで終了することができる。
5. - > `esc`キーを押してニュートラルなモードに変更してコマンド入力を可能にする
   - > `:q`保存済みのファイルを開いている vim から抜ける
   - > `:q!`ファイルを保存しないで vim を抜ける
   - > `wq`ファイルを保存してから vim を抜ける
6. > `pick`を削除して`fixup`に書き換えて保存してエディタを閉じる。
7. > 強制 push された場合にローカルと origin の差分を解消するために用いることが可能
8. > git rebase でコンフリクトした場合に解消して続きを実施するのに用いることが可能
