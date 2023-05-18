'''
second lesson
Guidelines for Prompting
In this lesson, you'll practice two prompting principles and their related tactics in order to write effective prompts for large language models.
'''
import openai
import os


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = ''

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# fact_sheet_chair = """
# OVERVIEW
# - Part of a beautiful family of mid-century inspired office furniture, 
# including filing cabinets, desks, bookcases, meeting tables, and more.
# - Several options of shell color and base finishes.
# - Available with plastic back and front upholstery (SWC-100) 
# or full upholstery (SWC-110) in 10 fabric and 6 leather options.
# - Base finish options are: stainless steel, matte black, 
# gloss white, or chrome.
# - Chair is available with or without armrests.
# - Suitable for home or business settings.
# - Qualified for contract use.

# CONSTRUCTION
# - 5-wheel plastic coated aluminum base.
# - Pneumatic chair adjust for easy raise/lower action.

# DIMENSIONS
# - WIDTH 53 CM | 20.87”
# - DEPTH 51 CM | 20.08”
# - HEIGHT 80 CM | 31.50”
# - SEAT HEIGHT 44 CM | 17.32”
# - SEAT DEPTH 41 CM | 16.14”

# OPTIONS
# - Soft or hard-floor caster options.
# - Two choices of seat foam densities: 
#  medium (1.8 lb/ft3) or high (2.8 lb/ft3)
# - Armless or 8 position PU armrests 

# MATERIALS
# SHELL BASE GLIDER
# - Cast Aluminum with modified nylon PA6/PA66 coating.
# - Shell thickness: 10 mm.
# SEAT
# - HD36 foam

# COUNTRY OF ORIGIN
# - Italy
# """
# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# After the description, include a table that gives the 
# product's dimensions. The table should have two columns.
# In the first column include the name of the dimension. 
# In the second column include the measurements in inches only.

# Give the table the title 'Product Dimensions'.

# Format everything as HTML that can be used in a website. 
# Place the description in a <div> element.

# Technical specifications: ```{fact_sheet_chair}```
# """

personal_property = '''
负债：980000
固定资产：1100000
流动资产：450000
每月收入：20000
每月开支：5000
'''

personal_property_target = '''
3年内还清贷款，并且储蓄满1000000
'''

# prompt = f""""
# 你的任务是帮助分析这个人的财务状况，并给出理财建议。

# 这个人的财务状况是：```{personal_roperty}```
# """

# prompt = f""""
# 你的任务是帮助分析这个人的财务状况和财务目标，并给出理财建议。

# 这个人的财务状况是：```{personal_property}```
# 这个人的财务目标是：```{personal_property_target}```
# """

# prompt = f""""
# 你的任务是帮助分析这个人的财务状况和财务目标，并给出理财建议。

# 这个人的财务状况是：```{personal_property}```
# 这个人的财务目标是：```{personal_property_target}```

# 这个人可以通过网页输入财务状况以及财务目标，然后点击按钮，前端将这些信息发送给后端，请输出html格式的web
# """

prompt = f""""
你的任务是帮助写一个web页面，让用户可以输入以下信息：

```{personal_property}```
```{personal_property_target}```

"""


response = get_completion(prompt)
print(response)