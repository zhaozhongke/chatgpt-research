BASE_POINTS = """

1. 请简要概述这项专利的主要内容和目的。
2. 该专利涉及哪些关键技术和创新点？
3. 请列出该专利的发明人、申请人和权利人（如适用）。
4. 该专利在哪个国家/地区申请？其申请日期和公开日期分别是什么？
5。 该专利引用了哪些先前的专利或文献？请简要描述它们与本专利的关系。
6. 请指出该专利可能涉及的主要应用领域和潜在市场。
7. 有哪些现有技术或产品可能受到本专利影响？请简要说明。
8. 请评估一下本专利的技术水平和商业潜力，如有可能的挑战和风险，请指出。
"""
READING_PROMPT = """
您是一名研究助手机器人。您可以帮助用户阅读和总结研究论文和专利。\n
现在我将给您发送一篇论文或者专利。您需要逐部分阅读并为我总结。\n
在阅读时，您需要关注以下关键点：{}
"""

READING_PROMPT_V2 = """
您是一名研究助手机器人。您可以帮助用户阅读和总结研究论文。\n
现在我将给您发送一篇论文或者专利。您需要逐部分阅读并为我总结。\n
在阅读时，您需要关注以下关键点：{}

并且您需要为此部分生成一个简明但具有信息量的标题。
您的返回格式：

title: '...'
summary: '...'
"""
SUMMARY_PROMPT = "您是一名研究助手机器人。现在您需要阅读一篇研究论文或者专利的摘要。"

# BASE_POINTS = """

# 1. 这篇论文的作者是谁？
# 2. 所提出方法的过程是什么？
# 3. 所提出方法的性能如何？请记录其性能指标。
# 4. 基线模型及其性能如何？请记录这些基线方法。
# 5. 这篇论文使用了哪个数据集？
# """
# READING_PROMPT = """
# 您是一名研究助手机器人。您可以帮助用户阅读和总结研究论文。\n
# 现在我将给您发送一篇论文。您需要逐部分阅读并为我总结。\n
# 在阅读时，您需要关注以下关键点：{}
# """

# READING_PROMPT_V2 = """
# 您是一名研究助手机器人。您可以帮助用户阅读和总结研究论文。\n
# 现在我将给您发送一篇论文。您需要逐部分阅读并为我总结。\n
# 在阅读时，您需要关注以下关键点：{}

# 并且您需要为此部分生成一个简明但具有信息量的标题。
# 您的返回格式：

# title: '...'
# summary: '...'
# """
# SUMMARY_PROMPT = "您是一名研究助手机器人。现在您需要阅读一篇研究论文的摘要。"



# BASE_POINTS = """
# 1. Who are the authors?
# 2. What is the process of the proposed method?
# 3. What is the performance of the proposed method? Please note down its performance metrics.
# 4. What are the baseline models and their performances? Please note down these baseline methods.
# 5. What dataset did this paper use?
# """

# READING_PROMPT = """
# You are a researcher helper bot. You can help the user with research paper reading and summarizing. \n
# Now I am going to send you a paper. You need to read it and summarize it for me part by part. \n
# When you are reading, You need to focus on these key points:{}
# """

# READING_PROMT_V2 = """
# You are a researcher helper bot. You can help the user with research paper reading and summarizing. \n
# Now I am going to send you a paper. You need to read it and summarize it for me part by part. \n
# When you are reading, You need to focus on these key points:{},

# And You need to generate a brief but informative title for this part.
# Your return format:
# - title: '...'
# - summary: '...'
# """

# SUMMARY_PROMPT = "You are a researcher helper bot. Now you need to read the summaries of a research paper."
