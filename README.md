# Github_Project_cpp_interview_print_to_pdf
GitHub项目"cpp interview"，c++的八股文，识别markdown文件的链接，访问微信公众号文章，它写着"该公众号已迁移"，要点击”访问文章“，然后对这些文章进行打印，并按照顺序提供编号。python代码批处理

主要针对微信公众号文章进行处理

0. 这种业务代码，一般用"chatgpt生成+逐步修改"的方式完成

1. 有些图片没有加载上，document.body.scrollHeight无法识别高度正确。一怒之下，模拟按"Page Down"20次

2. 微信页面访问多了，会有"环境异常的提示"，可以过一会，从下一篇文章开始继续处理。可以随时终止和开始，选择终止，然后从下一个index编号开始

3. 运行时间有点长，一个多小时看着是需要，吃饭的时候处理。pdf就不给了，毕竟是别人的项目，它在GitHub也没开源，只给了微信链接，就当点击一下

4. pdf打印的方法参考这个代码，可以迁移到其它网页导出pdf，基本没什么问题。除了某CSDN，emmm

5. 针对pdf链接，这个语句不要执行，"WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))"
