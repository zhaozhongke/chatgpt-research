from gpt_reader.paper.paper import Paper
from gpt_reader.pdf_reader import PaperReader
import os
import glob
import concurrent.futures
import asyncio
import pickle


def summarize_and_save_paper(file_name):
    # Initialize the paper reader
    reader = PaperReader(openai_key='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')

    # Load the paper as a Paper object
    paper = Paper(f'./patent/{file_name}')

    # Summarize the paper using GPT-3
    summary = reader.summarize(paper)

    # Save the digested paper as a pickle file
    with open(f'./patent_output/pickle/digested_paper_{file_name[:-4]}.pkl', 'wb') as f:
        pickle.dump(paper, f)

    # Generate markdown output and save to file
    question_prompt= """
    用中文详细总结这篇专利,并使用markdown输出。包括：
    1. 专利的基本信息，包括专利号、申请日、公开日、申请人、发明人
    2. 专利的摘要和背景
    3. 专利的详细描述
    4. 专利的技术要点和创新点、具体实施方式.
    5. 哪些现有技术或产品可能受到本专利影响？
    """
    md_output = reader.question(paper, question_prompt)
    with open(f'./patent_output/patent_{file_name[:-4]}.md', 'w') as f:
        f.write(md_output)


if __name__ == '__main__':
    dir_path = './patent_output/pickle'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Use concurrent.futures to process papers in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for file_name in glob.glob('./patent/*.pdf'):
            futures.append(executor.submit(summarize_and_save_paper, file_name.split('/')[-1]))

        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f'Error processing paper: {e}')






# print summary of a section
# print("paper_summaries----------------------")
# print(paper.paper_summaries)
# print("paper_summaries[4]----------------------")
# print(paper.paper_summaries[4])

# print(reader.question(paper, '详细总结这篇专利，包括基本信息，技术要点和创新点。 务必不少于3000字.'))
# print(reader.question(paper, '该专利涉及哪些关键技术和创新点？'))
# print(reader.question(paper, '请列出该专利的发明人、申请人和权利人（如适用）。'))
# print(reader.question(paper, '该专利在哪个国家/地区申请？其申请日期和公开日期分别是什么？'))
# print(reader.question(paper, '该专利引用了哪些先前的专利或文献？请简要描述它们与本专利的关系.'))
# print(reader.question(paper, '请指出该专利可能涉及的主要应用领域和潜在市场。'))
# print(reader.question(paper, '有哪些现有技术或产品可能受到本专利影响？请简要说明'))
# print(reader.question(paper, '请评估一下本专利的技术水平和商业潜力，如有可能的挑战和风险，请指出。'))
# print(reader.question(paper, '在您回答这些问题时，请提供足够的详细信息，以便我们对专利的内容有充分的了解。谢谢！'))
