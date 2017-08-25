---
layout: single
title: 一碰minimal-mistakes就上手
date: 2017-07-12 22:14:02
excerpt: 第一篇網誌，並且簡介minimal-mistakes配合Github架設。
categories:
- 教學
tags:
- minimal-mistakes
- Jekyll
- Github
- DISQUS
---

{% include toc title = "目錄" %}

## 緣起不滅
>『花開成簇，水聚為川，依舊是寂寞，唯有在花與水交映的剎那，花因水而清麗，水因花兒澄淨了。人生大抵也是如此，即是到最後，花謝水枯，仍不肯忘記，那一場初初的緣起。』 - 張曼娟

身為一位腦包資料科學家的我，最近找到一個[網站](https://andybega.github.io)，裡面有很多資料處理與呈現的方式非常美觀。
仔細觀察了一下他[Github](https://github.com/andybega/)，發現他大部分程式都是用R寫的(殘念了)，但是在角落有個很特別的repository在呼喚我。
那天開始我戀愛了！無可救藥地愛上了[minimal-mistakes](https://mmistakes.github.io/minimal-mistakes/)，這也是我建立這個獨立小blog的原因！
對我而言網站架設、網頁設計的概念非常有限，只有在大學時期曾經在一間實驗室打工，當時做的事情不過就是架個Linux伺服器，作為主要網頁伺服器的備援。
而剛出社會工作的我，由於從來沒寫過像樣的網站，上網找了一下相關教學盡是一堆妖魔鬼怪，先從前端三巨頭HTML5, CSS3, JavaScript，一直到node.js, TypeScript，什麼都還沒開始學就搞得我一個頭兩個大。
看到minimal-mistakes能夠利用Github建立起有留言板功能的簡易blog，又是開放的MIT License讓大家能自由客製化自己的頁面，根本佛心。

## 整裝備戰
> 『啊，我要準備什麼？』

首先一定要有[Github](https://github.com/)帳號，雖然想架設在自己的網站伺服器也可以，但是對於一介窮逼的我而言還是架在Github上好了，當然你還要有一些基礎的Git知識。
接著為了讓網站有留言版的功能，還要申請個[DISQUS](https://disqus.com/)帳號，讓網頁偽裝成有動態物件的感覺，事實上是委託給別的網站處理。
接著，準備一顆樂觀的心情，以及一個下午能夠荒廢的時光。

## 架站101
如果你的英文跟我差不多好(爛？)，可以直接到官方網站的[Quick-Start](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)得到最新最完整的資訊。
也可以看我在這邊自以為的班門弄斧...

### I Gonna Fork You Up!
無須多言，馬上趕到minimal-mistakes的[Github](https://github.com/mmistakes/minimal-mistakes)，怒fork到自己的reposiroty並clone下來。
接下來就是比較tricky的地方了，由於腦殘的我一開始沒留心閱讀[Github相關文檔](https://help.github.com/articles/user-organization-and-project-pages/)，害我來來回回搞了一整天。

文檔主要有兩個重點：
- 如果要做為個人網頁使用(就像這個網站)，那麼網址為"帳號名稱.github.io"(我是將repository也命名成這樣啦，不過影響應該不大)。重點來了，branch一定要預設為`master`！
- 如果要做為Project專用網頁，那麼網址為"帳號名稱.github.io/專案名稱"。branch要預設為`gh-pages`。

改好fork下來的repository名稱，如果你要作為Project裝用網頁就checkout一個新的branch，名稱為`gh-pages`。
接著將`Gemfile`這個檔案內容改成如下所示：
{% highlight ruby %}
    source "https://rubygems.org"

    gem "github-pages", group: :jekyll_plugins

    group :jekyll_plugins do
      gem "jekyll-paginate"
      gem "jekyll-sitemap"
      gem "jekyll-gist"
      gem "jekyll-feed"
      gem "jemoji"
    end
{% endhighlight %}
接著移除掉不相干的檔案，以免以後clone網站下來要花個十年半載，要刪除的檔案有：`.editorconfig`, `.gitattributes`, `.github`, `/docs`, `/test`, `CHANGELOG.md`, `minimal-mistakes-jekyll.gemspec`, `README.md`,`screenshot-layouts.png`, `screenshot-layouts.png`。

### 基本設定
接著就是重頭戲了，打開`_config.yml`，要開始對網站進行一些基礎設定。
- `locale: "[地區]"` 我是打`zh-TW`啦，你想崇洋媚外打個`en`,`en-GB`,`en-US`也是可以。
- `title: "[網站名稱]"` 也就是顯示在最上方的網站名稱
- `name: "[顯示使用者]"` 你的名字<s>電影還不錯</s>，預設會顯示在左側簡介。
- `url: "[網址]"` 依照前一個章節說明，設定為"https://帳號名稱.github.io"，當然好野人有網域也是可以自行填寫。
- `baseurl: "[專案名稱]"` 如果你的網頁是給專案使用才要填這個，我是直接無視。
- `repository: "[Github帳號]/[專案名稱]"` 照著填就對啦，你的Github帳號以及fork下來的minimal-mistakes名稱。
- `comments`底下的`provider: "disqus"`告訴網站要用DISQUS留言板，而`shortname`就是你在[DISQUS網站](https://disqus.com/)上建立的留言板代號。當然還可以做其他留言設定，不過我覺得這樣足矣。但是注意在設定DISQUS留言版的時候，語言選用`English`而不要選`Chinese`，因為我得了一種看簡體字會屎的病。

中間我跳掉一大部分，因為我有點懶得用！接著在`# Social Sharing`這部分，就參考以下代碼：
{% highlight ruby %}
    social:
      type:  # Person or Organization (defaults to Person)
      name:  # If the user or organization name differs from the site's name
      links:
        - "https://twitter.com/yourTwitter"
        - "https://facebook.com/yourFacebook"
        - "https://instagram.com/yourProfile"
        - "https://www.linkedin.com/in/yourprofile"
        - "https://plus.google.com/your_profile"
{% endhighlight %}
接著`# Site Author`部分，也就是左側欄位表現自我的部分，交給大家自由發揮。
而最後值得一提的是`# Defaults`底下的`comments: true`設定成每個post預設可留言。

這樣大抵上就要完成了！

### 基本架構
現在剩下的就是右上方那一列導覽列沒有設定，這時候點擊的話就會直接404找不到網頁，與其找不到還不如自己寫一份404專用網頁。
- 先建立`_pages`資料夾，並在底下建立一份`404.md`的文檔，範例如下。
{% highlight markdown %}
    ---
    title: "無此頁面"
    layout: single
    excerpt: "作者腦殘了，沒有準備這個頁面！"
    sitemap: false
    permalink: /404.html
    ---

    這個頁面可能因為作者腦殘沒設定好，或是版本更新年久失修，請聯絡我或是嘗試搜尋一下吧！

    <script type="text/javascript">
      var GOOG_FIXURL_LANG = 'zh-TW';
      var GOOG_FIXURL_SITE = '{{ site.url }}'
    </script>
    <script type="text/javascript"
      src="//linkhelp.clients.google.com/tbproxy/lh/wm/fixurl.js">
    </script>
{% endhighlight %}
- 在`_data`底下有個`navigation.yml`檔案，用來描述上方導覽列的內容及連結關係，範例如下。
{% highlight markdown %}
    # main links
    main:
      - title: "網誌"
        url: /year-archive/
      - title: "類別"
        url: /categories/
      - title: "作品"
        url: /works/
      - title: "關於"
        url: /about/
{% endhighlight %}
- 接著回到`_pages`底下建立對應的頁面，其中我們以`網誌`為例，建立`year-archive.md`文檔，請參考[Github原始碼](https://github.com/KodeWorker/KodeWorker.github.io/blob/master/_pages/year-archive.md)。
- 最後終於可以開始寫文章了，每一篇文章的檔案格式為`YEAR-MONTH-DAY-title.md`，而且文檔要存在`_posts`目錄下。
依照[Jekyll格式](https://jekyllrb.com/docs/posts/)，稍微摸一下應該不難上手。

## 何去何從
> 『這是我交付給你的最後一項任務，永續的任務。在這個世界上，要表現快樂、感到快樂，不需要任何理由。接著你就能去愛，去做你想做的事。』 - 深夜加油站遇見蘇格拉底

接下來的任務就是盡可能的快樂，讓閱讀網誌的人快樂，就是持之以恆的紀錄研究與生活的點滴，並且慢慢將這個網頁客製成心目中理想的型態。

## 更新紀錄

- **[2017-07-12]** 改變內文字體大小，預設的真的大得有點誇張，所以修改`/_sass/minimal-mistakes/_pages.scss`底下尋找到`.page__content`並且設定物件內`p`的屬性`font-size: 12px`。

- **[2017-07-12]** 網站標題稍微有點小，解決方法是到`/_sass/minimal-mistakes/_mashthread.scss`內設定`.site-title`的`font-size: 2em;`。
學習是永無止盡的，哪天我把minimal-mistakes摸熟了，再來分享一些客製化的心得吧。

- **[2017-07-21]** jekyll rouge 支援多種語言 highlight，但是整篇code落落長看得人眼花，對過長的程式區段加入高度限制及捲軸。方法是直接到`/_sass/minimal-mistakes/_syntax.scss`內，在最外層加入以下程式碼。
{% highlight scss %}
    .highlight {
        max-height: 300px;
        overflow-y: scroll;
    }
{% endhighlight %}

- **[2017-07-22]** 在讀取頁面`archive`的標題大小，竟然比類別名稱還要大，為了改變這一個項目，修改`/_sass/minimal-mistakes/_archive.scss`內的設定。

- **[2017-07-22]** `/_pages/year-archive.md`原本頁面一直很不親民，看到了一篇[文章](http://chris.house/blog/building-a-simple-archive-page-with-jekyll/)介紹之後驚為天人，其他`archive`類型頁面也應該可以整理程較簡潔的格式，[catagory-archive範例](https://blog.webjeda.com/jekyll-categories/)。

- **[2017-08-24]** 今天編輯網誌時發現一個很有趣的現象，顯示.jpg檔時有可能會方向錯誤，原因是檔案中遺失了方位的標記，詳見這個[StackOverflow頁面](https://stackoverflow.com/questions/19434073/how-can-i-avoid-that-github-rotates-my-jpg-in-my-readme-md)。最懶人的解決方法是，開啟圖像編輯軟體，然後往一邊旋轉90度四次(共360度)再儲存圖檔即可。
