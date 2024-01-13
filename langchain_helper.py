from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# This loads the .env file which has the API Key
load_dotenv()

def generate_company_name(company_type, response_number, max_char):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['company_type', 'number_company', 'number_char'],
        #template="I wanna build a {company_type} company. Please suggest 7 cool, trendy, name not more than 7 characters."
        template="I wanna build a {company_type} company. Please suggest {response_number} cool, trendy, name not more than {max_char} characters."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="company_name")

    response=name_chain.invoke({'company_type': company_type, 'response_number': response_number, 'max_char': max_char})

    #name = llm.invoke("I wanna build a tech company. Please suggest a 13 cool, trendy, AI name not more than 7 characters.")

    return response

if __name__ == "__main__":
    print(generate_company_name("AI", 3, 7))

    
