two rounds 第一轮：Word search 2 using trie
第二轮：valid parenthesis。 follow up： given a list of pairs of left and right parenthesis which could be any character. 注意，可能会有重复，而且会交叉，比如：给你（)和 ( a 和 ) b 
input 是 （a ) b. From 1


电面coursera, 写了两道题，都是Leetcode原题。
（1）double pow(double a, int b); 
(2) solve sudoku

都是Data Scientist的职位
[color=#555555][font=Tahoma,]第一轮是recruiting researcher面，有问个比较general的问题：Coursera现在想做private tutoring，但不知道该不该进入这个market，你会从什么角度切入这个问题。[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]第二轮是HM的tech面：[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]1. 怎么求课程长度和用户是否购买证书之间的likelihood，已知课程越长价格越高[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]2. 课程长度和课程价格都当做binary variable，写了一个model，让你interprete里面的coefficient[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]3. 上一步里的model，如果从总体enrollment level来model，和by course level的model，怎样比较coefficients，怎样比较standard errors[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]4. SQL：一个学生enrollment table，求每个学生的最好成绩，和对应的course session。如果highest score有duplicate怎么办？（这个面试的时候很容易忽略）[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]（这题我后来发现自己写漏了一句话……）[/font][/color][color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]5. 给个bernoulli distribution，n个trial，k个success，p=k/n，求p的95% CI; 如果要让CI变为原来的10倍小，n应该要多大。[/font][/color][color=rgb(255, 255, 255)][/color]
[color=rgb(255, 255, 255)][/color]
[color=#555555][font=Tahoma,]感想：其实考的都是很基本的东西，所以要注意回答的大方向正确，还有不要粗心……[/font][/color]



LinkedIn上直接骚扰recruiter拿到的面试。 
电面 1. HR Phone Screen 
2. 烙印电面 (1) A well-formed expression is a string consisting of nested matching left and right parenthesis. For example, the following are well-formed expressions: empty string () (()()) but the following are not: )( (( (2) Now, suppose that both parentheses () and brackets are allowed in well-formed expressions. For example, the following are well-formed expressions: () () but the following are not: [) ( (3) Finally, suppose that you are given a list of character pairs (i.e., (left, right)) which are considered matching. For example, if matching = [('A', ‘a’), ('')], then the following is a well-formed expressions: Aa but the following is not: aA 3. 白人Maneger电面 Let's play a game of Boggle! Given a grid with characters (e.g. the following), ECEA ALEP HNBO QTTY Find all the words that can be formed using the letters in the grid. For instance, you can perform the words elan, celeb, cape, peace, etc…. - The grid of letters can be used in every direction (see PEACE) - No position can be used twice within the same word. (e.g. POPE is not a valid word on this board) Onsite: 1. 国人。2.5 小时的Coding Task。利用现成的RESTful API实现你需要登录以查看此链接.的策略。考察点包括：1. 算法和游戏策略的效果 2. 代码结构（封装，复用性）等等 3. Coding Style 2. 白人Maneger。45分钟Behavior。 3. 白人，ABC shadow。45分钟。你需要登录以查看此链接.。 4. 亚裔。Behavior。45分钟。 5. 白人。Design url shortener。最后一个follow up需要用到类似kafka的消息系统。45分钟。 6. HR聊天。30分钟。 7. Maneger聊天。30分钟。 目前Coursera的主要盈利途径还是卖Verified Certificate（这个有点囧）。感觉员工也对未来的盈利模式没有什么看法，但是对在线教育事业很有热情。 

链接: https://instant.1point3acres.com/thread/138148/post/1587315
来源: 一亩三分地