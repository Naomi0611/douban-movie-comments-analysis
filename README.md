# 复仇者联盟与惊奇队长豆瓣短评分析
  漫威作为目前全球电影届最大的IP之一，在今年接连推出了两部电影，分别是《惊奇队长》和《复仇者联盟4：终局之战》。虽然两部电影都取得了
票房丰收，但是两部电影在网络上的口碑似乎相差甚远，所以，我爬取了国内比较专业的电影爱好者社区关于两部电影的短评，进行比较分析，看看这两部电影在观众眼中究竟如何。<br> 
## 1.获取数据
  https://github.com/kilone/douban-movie-comments-analysis/tree/master/Crawler<br>
  通过爬虫获取数据后保存在MySQL数据库中，主要获取两个方面的数据：1.用户评论与评分信息；2.评论者信息，主要是用户所在地。  
  数据样本  
  ![评论数据](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/movie_comments.png)   
  ![用户数据](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/user_information.png)
## 2.数据分析
  https://github.com/kilone/douban-movie-comments-analysis/tree/master/DataAnalysis<br>
  ### 1.计算两部电影的平均评分
  网站评分分为五个级别：力荐，推荐，还行，较差，很差。分别赋值5分，4分，3分，2分，1分，在滤除未评分的用户后，计算出两部电影的评分分别是3.9分和3.2分。由此看来，两部电影的评分差距还是比较大的。<br>
  ![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/%E5%B9%B3%E5%9D%87%E5%88%86%E5%AF%B9%E6%AF%94.png)
  ### 2.各级别评分人数对比
  ![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/%E5%90%84%E7%BA%A7%E8%AF%84%E5%88%86%E7%82%B9%E8%B5%9E%E6%95%B0%E5%AF%B9%E6%AF%94.png)<br>
  通过上表，我们可以看出来《复仇者联盟》的评分主要集中在“力荐”上，而《惊奇队长》则比较分散，“还行”占多数。从这个角度来看，复仇者联盟又一次胜出了。<br>
  ### 3.各级别评分的点赞数对比
  ![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/%E5%90%84%E7%BA%A7%E8%AF%84%E5%88%86%E7%82%B9%E8%B5%9E%E6%95%B0%E5%AF%B9%E6%AF%94.png)<br>
  从点赞数来看，《复仇者联盟》再一次主要集中在“力荐”上，而《惊奇队长》仍然是集中在“还行”上。而且，《复仇者联盟》的点赞总数更是远远超过《惊奇队长》。这说明《复仇者联盟》不仅在评分上大大超过《惊奇队长》，在热度上也同样远胜于《惊奇队长》。
## 3.词频统计
### 1.复仇者联盟词频统计
  ![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/avengers_frequency.png)   
  从词频统计来看，《复仇者联盟》中，“十年”，“时间”，“情怀”等词占有较高比例，因为这一部是系列最后一部，所以大家在评论时带着比较重的情怀的，从一定程度上来说，打分也有情怀加分的影响。此外，“钢铁侠”，“美队”，这两位超级英雄也有较高的频率，说明这两位英雄在《复仇者联盟》中是毫无疑问的主角，在影迷心中有着非常重要的地位。
### 2.复仇者联盟词云
  ![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/Avengers_cloud.png)   
### 3.惊奇队长词频统计
![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/captain_frequency.png)   
从词频统计来看，前20的词语中，只有惊奇队长一位角色名，因为这是一部关于惊奇队长的个人电影，所以惊奇队长毫无疑问占C位。另外，“女主”和“女性”都出现在了前
20中，说明《惊奇队长》作为漫威系列第一部女性超级英雄电影，女性这个关键词获得了很高的讨论度。
### 4.惊奇队长词云
![](https://github.com/kilone/douban-movie-comments-analysis/blob/master/DataAnalysis/images/captain_cloud.png)
