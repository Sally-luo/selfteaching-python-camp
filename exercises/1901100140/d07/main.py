from mymodule import stats_word
sample_text="""
愚公移山

太行、王屋二山的背面，住了一个九十岁的老翁，名叫愚公。二山占地广阔，挡住去路，使他和家人往来极为不便。
一天，愚公召集家人説：“让我们各尽其力，铲平二山，开条道路，直通豫州，你们认为怎样？”
大家都异口同声赞成，只有他的妻子表示怀疑，并説：“你边开凿一个小丘的力量都没有，怎么可能铲平太行、王屋二山呢？况且，凿出的土石又丢到哪里去呢？”

大家都热烈地説：“把土石丢进渤海里。”
于是愚公就和儿孙，一起开挖土，把土石搬运到渤海里去。
愚公的邻居是个寡妇，有个儿子八岁也兴致勃勃地走来帮忙。
寒来暑往，他们要一年才能往返渤海一次。

住在黄河河畔的智叟，看见他们这样辛苦，取笑愚公説：“你不是很愚蠢吗？你已一把年纪了，就是用尽你的气力，也不能
挖去山的一角呢？”
愚公叹息道：“你有这样的成见，是不会明白的。你比那寡妇的小儿子还不如呢！就算我死了，还有我的儿子，我的孙子，我的
曾孙子，他们一直传下去。而这二山是不会加大的，总有一天，我们会把它们铲平。”
智叟听了，无话可説。
二山的守护神被愚公的坚毅精神吓倒，便把此事奏知天帝。天帝佩服愚公的精神，就命两位大力神背走二山。

How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high mountains,mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land,the mountains blocded yugong's way making it inconvenient for him
and his family to  get around.
One day yugong gathered his family together and siad,"Let's do our best to level these two mountains.We shall
open a road that leads to Yuzhou.What do you think?"

All but his wife agreed with him.
"You don't have the strength to cut even a small mound,"muttered his wife."How on earth do you suppose
you can level Mount Taixing and Mount Wangwu?Moreover,Where will all the earth and rubble go?"
"Dump them into the sea of Bohai!"said everone.

So yugong,his sons,and his grandsons started to break up rocks and remove the earth.They transported 
the earth and rubble to the sec of Bohai.

Now Yugong's neighbour was a widow who had an only child eight years old.Evening the young boy offered
his help eagerly.

Summer went by and Winter came.It took Yugong and his crew a full year to travel back and forth once.

On the bank of the Yellow River dwelled on old man much respected for his wisdom.When he saw their 
back-breaking labour,he ridiculed Yugong saying,"Are't you foolish,my friend?you are very old now,and 
with whatever remains of your waning strength,you won't be able to remove even a corner of the mountain."

Yugong uttered a sigh and said,"A biased person like you will never understand.You can't even cpmpare 
with the widow's little boy!"

"Even if I were dead,there will still be my children,my grandchildren,my great grandchildren,my great
great grandchildren. They descendants will go on forever.But these mountains will not grow any taler.We
shall level them one day!"he declared with confidence.

The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and his crew were,they were struck
with fear and reported the incident to the Emperor of Heavens.

Filled with admiratiion for Yugong,the Emperor of Heavens ordered tow mighty gods to carry the mountains awawy.
"""

result=stats_word.stats_text(sample_text)

print("统计结果",result)


