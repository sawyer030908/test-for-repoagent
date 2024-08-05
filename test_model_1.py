from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# 加载模型和tokenizer
model_name = "C:/Users/Sawyer/Llama3-ChatQA-1.5-8B"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 添加pad_token并设置
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# 设置pad_token_id为eos_token_id以避免警告
model.config.pad_token_id = tokenizer.pad_token_id

# 编写生成回复的函数
def generate_response(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    inputs["attention_mask"] = torch.ones_like(inputs["input_ids"], dtype=torch.long)  # 明确设置attention_mask
    outputs = model.generate(
        inputs.input_ids, 
        attention_mask=inputs.attention_mask, 
        max_length=max_length, 
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# 测试对话
if __name__ == "__main__":
    prompt = "你好, Llama3!"
    response = generate_response(prompt)
    print("Llama3:", response)
