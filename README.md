# 自动批处理多个网页转pdf，适用于[cpp-learning](https://github.com/chengxumiaodaren/cpp-learning)项目，它是CPP的复习资料
- 识别markdown文件的链接
- 主要针对微信公众号文章进行处理，其它链接也完全适用
- 访问微信公众号文章，它写着"该公众号已迁移"，要点击"访问文章"
- 网页中，有些图片没有加载上，需要自动滚动网页
- 对这些文章进行打印，并按照顺序提供编号。
- Python代码。ChatGpt代码生成+修改。
- 支持中断处理，允许在之前的PDF生成过程中继续生成。具体来说，比如你生成了50个PDF，然后想中断处理其它事情，过一段时间，你完全可以从第51个PDF开始生成。

## 强烈安利[cpp-learning](https://github.com/chengxumiaodaren/cpp-learning)项目，真的写得太好了！！！

# 潜在问题和解决方案
- 同时短时间访问微信公众号文章链接，平台会识别到并提示你要进行人机验证(你要点一下)
  - ChatGPT搜索"避免被识别爬虫"
- 处理较慢
  - 减少自动滚动数目
  - 有些位置的time.sleep可以省略，或者减少时间
- 处理过程没有隐藏
  - 用headless等方式应该能解决问题。chrome_options.add_argument('--headless')


## 细节
0. 这种业务代码，一般用"chatgpt生成+逐步修改"的方式完成

1. 有些图片没有加载上，document.body.scrollHeight无法识别高度正确。一怒之下，模拟按"Page Down"20次。可以试一下10次，应该也没问题。

2. 微信页面访问多了，会有"环境异常的提示"，可以过一会，从下一篇文章开始继续处理。可以随时终止和开始，选择终止，然后从下一个index编号开始，"if index<=xxx: continue"。

3. 运行时间有点长，一个多小时看着是需要，吃饭的时候处理。pdf就不给了，毕竟是别人的项目，它在GitHub也没开源，只给了微信链接，就当点击一下

4. pdf打印的方法参考这个代码，可以迁移到其它网页导出pdf，基本没什么问题。除了某CSDN，emmm

5. 针对pdf链接、一直Page Down它会加载新内容的网页，这个语句不要执行，"WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))"。其实这个语句没什么用。
