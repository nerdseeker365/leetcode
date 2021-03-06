
/*Screen
由于小编在和HR聊天的时候告知自己的选择窗口比较紧，所以电面当天下午收到Onsite通知。简短截说：A家的Onsite一共有七轮，前五轮每轮四十五分钟，后两轮是三十分钟的culture fit.

Distribute策略：当Cache数据量巨大的时候，需要用多个Node来存储Cache。由于Cache本质上是Key-value-pair，那么可以通过对Key进行类似Hash的Sharding可以决定Value需要存储/读取的Node.
Cache策略：基本上就是Pull (on-demand)/Push(regular update)的区别。具体情况要考虑需求的具体情况，比如对与Cache数据实时性的要求，对于Performance要求等，一定程度上也考察面试者的沟通能力。
Failure case以及Scalability的讨论，主要是展示面试者思考问题的全面性。
从第三轮开始，连续三轮Coding interviews: 每轮除去了面试官讨论的时间，大概只有三十分钟做Coding，加之每个解法都需要编译出结果，所以感觉时间比较紧迫。

基于数据结构的算法题：Encode an alien dictionary using a tree and then produce a dictionary using topological traversal. Topological sorting类型，Leetcode中等难度。
算法题：实现Regular expression match，比Leetcode的原题多一两个通配符，但思路想通，做过Leetcode那道题的朋友，写这题难度不大。
DP题，具体题目实在无法记得，印象中是中等难度的Leetcode的DP题，sorry.

最后的两轮面试比较轻松。和两位Non-technical面试官聊天，很多Behavior questions，主要考察面试者是否适合公司文化。比如，为什么选择Airbnb？ 如何改进Airbnb现有的产品？你最想做的事？给你三分钟，教他一件事？这种类型的问题。最好面试前看看网上关于Airbnb文化相关的讨论，答题尽量贴合的它家的做事风格，一般来说，过关问题不大。

Onsite三点半面完所有七轮，五点左右接到Offer，整个面试体验还是非常不错的。

Reflection

小编感觉A家的面试主要有两个重点：Bug free code and culture fit. 三轮Coding越快写完越有利，很多面试官有Follow-up question，都做出来的话对拿Offer很有帮助。
系统设计题，面试官问的非常详细，最好仔细看看类似题目的讨论（关注包子博客是必须的）。多插一句，有的面试官比较拽，态度不是很好，遇到这种情况，
个人心态要处理好，不要着急，更不要get defensive，好好做题是关键！整体来看，A家办公条件非常Fancy，Work-life balance应该也不错，每个季度有500刀的Airbnb credit，鼓励员工使用Airbnb旅游。
Offer package整体上中规中矩，如果认同A家的文化和愿景，这是一个很理想的可以改变世界的地方。
 * */