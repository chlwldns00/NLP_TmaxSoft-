



def keyword_extractor(tokenizinedList):
    idx=0 #### gpt로 키워드 뽑는 부분

    answer=tokenizinedList[idx] #토큰화된것중에 타겟질문에 대한 해답을 index로 반환해주는 idx
    context="" #gpt 시스템에서는 context가 존재하지않는거 같다. 혹은 context로 어떤것을 넣어줘야할지는 미정.
    prompt=answer+context+' 이 문장의 핵심 키워드들을 중요한 순서대로 dict자료형으로 뽑아줘'
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You arre a helpful assistant."},
            {"role":"user","content":prompt}
        ]
    )


    keyword_dict=completion.choices[0].message.content
    # print(type(keyword_dict))
    keyword_dict=eval(keyword_dict) #str->dict type difference

    print(completion.choices[0].message.content)
    return keyword_dict