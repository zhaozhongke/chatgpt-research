import pickle
from gpt_reader.paper.paper import Paper
from gpt_reader.pdf_reader import PaperReader

reader = PaperReader(openai_key='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')
paper = Paper('./US10488230.pdf')
summary = reader.summarize(paper)

# save paper & load
pickle.dump(paper, open('digested_paper.pkl', 'wb'))
paper = pickle.load(open('digested_paper.pkl', 'rb'))
# print summary of a section
print("paper_summaries----------------------")
print(paper.paper_summaries)
print("paper_summaries[4]----------------------")
print(paper.paper_summaries[4])

# print(reader.question(paper, '请简要概述这项专利的主要内容和目的。'))
# print(reader.question(paper, '该专利涉及哪些关键技术和创新点？'))
# print(reader.question(paper, '请列出该专利的发明人、申请人和权利人（如适用）。'))
# print(reader.question(paper, '该专利在哪个国家/地区申请？其申请日期和公开日期分别是什么？'))
# print(reader.question(paper, '该专利引用了哪些先前的专利或文献？请简要描述它们与本专利的关系.'))
# print(reader.question(paper, '请指出该专利可能涉及的主要应用领域和潜在市场。'))
# print(reader.question(paper, '有哪些现有技术或产品可能受到本专利影响？请简要说明'))
# print(reader.question(paper, '请评估一下本专利的技术水平和商业潜力，如有可能的挑战和风险，请指出。'))
# print(reader.question(paper, '在您回答这些问题时，请提供足够的详细信息，以便我们对专利的内容有充分的了解。谢谢！'))
