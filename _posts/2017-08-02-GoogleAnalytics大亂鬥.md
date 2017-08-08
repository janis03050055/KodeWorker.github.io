---
layout: single
title: Google Analytics 大亂鬥
date: 2017-08-02 15:13:34
excerpt: 分析網站流量，邁向百萬網紅的第一步。
categories:
- 教學
tags:
- minimal-mistakes
- Google Analytics
---

{% include toc title = "目錄" %}

## 前言
當初剛架立這個Github頁面，就發現minimal-mistakes有支援Google Analytics，可是當下只覺得有點鬧，以半開玩笑的態度來觀察一下這個垃圾部落格的流量。
看到之前痞客邦裡面的後台管理界面，紀錄著每天來看我這個邊緣人自言自語的人數，看著人數不斷的成長到一支手數不完，其實還有點小興奮呢！
可是有趣的是，突然有一天在觀察網站流量的時候，突然有來自戰鬥民族的問候，是從Samara Oblast連線過來，連線服務是jsc er-telecom holding samara branch。
經過網路上稍微咕狗一下發現，這個竟然是一個洗流量的駭客程式，網路上有一堆很妙的的人使用一些方式避免錯誤的流量分析。
本渣渣工程師完全沒用過Google Analytics，看到中心竟然有請業界來教學，免費又能去爽吃零食，當然要去互相傷害一發(講師真的這樣說...)。

## 課程總覽
什麼是GA？謂何網站主機的log紀錄，或是其他分析服務會與GA上面的數據有落差？
原因是在於web tracking流量，根據不同服務的設計trigger的機制有所不同，導致數據上會有差異，以下有介紹幾個常用的服務。

**Tracking Services**:
- Google Analytics - .js embeded
- Omniture - .js embeded
- Amazon Alexa - backdoor? biased(w/ donation)老師用的這個字眼有點攻擊性。

而本次課程主講的GA是利用第一方的瀏覽器Cookie，也支援第三方Cookie，所以較不容易被擋下。
Cookie的時效是利用last visit time + 2 years，來判斷unique users，所以你兩年內沒登入頁面幾就被判讀成新的人類囉。
Cookie的建立是利用 GA + "**DOMAIN NAME**"，來建立獨立拜訪者的獨特性，對於大型的網站而言，對於跨網域追蹤時，是滿重要維護的概念。
實務上應用，可能會有多個GA同時監控一個網站(因為監控的利害關係人不同，或監控的目標群體不同)，但是沒有做額外的設定，可能會導致資料遺失。

**基本tracking code**:
- Page View: 主要關注瀏覽者，瀏覽到網頁的特定位置，發出GA訊號進行監控。
- Event: track event例如網頁上的物件觸發，以前Flash物件還活著的時候會用來監控影片觸發(時代的眼淚，Youtube應該算是終結Flash Player的劊子手)，命名建議以英數為主。

**GA tacker 應用情境**：
- Multiple GA case: unique name for each tracker
- 虛擬page name應用：長頁面為了監控特地區段瀏覽、tab切換時event觸發起瀏覽事件、light box(就只是個網頁物件)、實體檔案名稱太複雜看報表不知道在搞什麼。

## 動動手、洞洞腦
GA帳號可以整合同一個Property下的Cookie，讓sales可以利用Cookie來針對目標客群，投遞特定產品促銷。
匯出匯入報表也較方便，但是UA檔不要亂開呀！！！？
老師說亂開UA檔案可是會有毀滅(你的網站)世界的可能！

> 金錢有限，客戶無窮！

**GA控管階層**：
- Account: 控管用帳號
- Property: 不同主題網站(unique UA code)
- View: 針對對應網站目標頁面進行監控
- property and view number limitations?應該是要靠付費提昇數量囉。

利用view的filter來限制連線目錄，但是當下老師不建議我們自行設定Filter，可能會影響到分析數據的完整性。
提到Cross-Domain的時候，我還滿好奇在實際應用上，公司內部的domain竟然也會用到不同的domain name，導致會用到不同property + cross-domain這個情況，來處理類似local issue這種有點腦的問題。

## GA跨隆謀？
**網站商業目的與流程**：
1. 商業目的：一切都一附著商業目的。`Awareness`取向，會跳出曝光型廣告、低品質；`導購`取向，主要由Campaign Site的關鍵頁面監控。
2. 網站規劃
3. 網站開發

**拜訪來源**：
- session: end of session will create a new session while landing a page (24:00 reset, time out, link source changed)
- user: unique user by cookies(為因瀏覽器不同；或是兩年以後登入！)
- difficulies: 特殊網路應用行業，人數大量行為不同，但是來源都相近。以加總人數來分析，無法明確知道來源。

其他幾個比較重要的數據方面，bounce rate對於現在很夯的長頁面單欄設計，不太能衡量網站標準，因為就一長條讀完就跳出了。
這時候老師突然出了的bounce rate計算的考題？！叫我們計算何不直接開個wiki頁面就好了，頁面的bounce就只是landing後直接exit的情形。
頁面的duration數值呈現上，較實際使用者時間短，由於GA是以下個頁面時間減去前一個瀏覽時間差作為duration。
講一堆數據到最終，一切還是由萬惡的KPI來決定成效。

> 就是靠嘴囉！跟我無關！

監控page view在何種頁面情境下點擊預購，監控event來收集點擊來源，以此來規劃網頁的責任歸屬。
找重點頁面才是網站分析的點目標，這時候老師舉了一個很好的活動入口網頁的分析，intro流失率 -> 首頁引導流量(button event) -> 後續導入資訊。

## 四大報表
**主要用這四個報表來分析網站的流量**：
1. Audience: 來訪者輪廓(用Cookie去推估使用者行為)、硬體設備、黏性。
2. Acquisition: 拜訪者來源
3. Behavior: 回訪、瀏覽深度
4. Conversion: URL_BUILDER之類的，這個...要作電子商務會比較重要，對我而言完全不重要！

之前看到location為(no set)的情況，還以為是沒有定位的關係，沒想到老師說是因為之前六都更新，導致系統無法承接。
所以要確認瀏覽者區域，需要選取region才能夠正確顯示區域。
根據頁面的目的，來對不同目的性的頁面坐不同數據的分析(Bounce Rate、Entrance、Exit...)。
目前這個部落格裡面沒有埋任何event，如果要確切分析觀看者的行為模式，因該要去偷埋一些event trigger(感覺就像裝針孔的變態一樣，果然當工程師都愛這一味)。
對於網站的Goal部份，因為這個部落格草創之初就是寫好玩的，當有目標有壓力事情肯定做不好。
但是如果使用者還是執意要入地獄，那注意的就只要好好規劃名稱，方便報表判讀分析。

> 『進入此門之前，放下一切希望』

使用URL_BUILDER導致雙問號出現在URL裡面，會導致頁面無法連結。
Generated URL有雙問號，要把第二個改成`&`；另一個是URL的`#`出現在中段，導致GA判度有可能濾調`#`之後的字串。

## 排除怪咖
有關於戰鬥民族進入部落格的情況，在中午休息時間問了一下老師，他說可以利用Admin -> Property -> Tracking Info 來排除調特定網域的來源。
這下有趣的事情出現了，這位俄羅斯老兄的網域名稱是`!.com`，這...根本是不合法的網域名稱。
這年頭戰鬥民族真的越來越厲害了，連網域都能改的面目全非，這樣只能利用filter來設定rule了。
但是老師說他自己也沒有用過，感覺位子坐得越高，對於技術細節應該越不care、只關注專案重要營運也是人之常情。

## 小結
其實我最想要聽的，是如何阻止怪咖的登入流量引響我的網站數據，可惜要自己去摸索了，不過至少上完課大概知道要從什麼地方開始著手。
不過課程大部份都跟sales比較相關，有點跟我這個只對技術有興趣的工程師而言，收穫算一般般。

(p.s. 當下上課心情其實有一點點差，因為想聽到的東西有點少，害我文章內各種惡言相向...後來才改掉較隨便的字眼)

> 看來我的修為還是不足，還要再內斂一些！

最後我赫然發現...怪咖的網域是`ḷ.com`而不是`!.com`，哦哦哦哦哦哦哦哦哦哦哦哦哦ḷ!ḷ!ḷ!ḷ!ḷ
