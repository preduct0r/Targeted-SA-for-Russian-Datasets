from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2ForSequenceClassification
model_name_or_path = "sberbank-ai/rugpt2large"
# model_name_or_path = "/home/den/released_models/rugpt2large"
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2ForSequenceClassification.from_pretrained(model_name_or_path).cuda()
text = "Александр Сергеевич Пушкин родился в "
# input_ids = tokenizer.encode(text, return_tensors="pt").cuda()
# out = model.generate(input_ids.cuda())
# generated_text = list(map(tokenizer.decode, out))[0]
# print(generated_text)