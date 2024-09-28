from prompts import prompt_temple
from llms import deepseek
def identify_issues(text):
    # 使用OpenAI API识别多音字和易读错字
    prompt_1 = prompt_temple.prompt_gene
    few_shots = prompt_temple.few_shots
    prompt = prompt_1.format(few_shots=few_shots, text=text)
    # print(prompt)
    output = deepseek.get_respones(prompt)
    return output