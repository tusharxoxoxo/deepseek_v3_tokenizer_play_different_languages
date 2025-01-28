# pip3 install transformers
# python3 deepseek_tokenizer.py
import transformers

chat_tokenizer_dir = "./"

tokenizer = transformers.AutoTokenizer.from_pretrained(
    chat_tokenizer_dir, trust_remote_code=True
)

# result = tokenizer.encode("china!")

result_chinese = tokenizer.tokenize("我叫 Tushar")
result_hindi = tokenizer.tokenize("मेरा नाम तुषार है")
result_french = tokenizer.tokenize("je m'appelle Tushar")
result_english = tokenizer.tokenize("My name is Tushar")
result_arabic = tokenizer.tokenize("اسمي توشار")
result_russian = tokenizer.tokenize("Меня зовут Тушар")

print("'My name is Tushar' in different languages")
print("english",result_english)
print("chinese",result_chinese)
print("hindi",result_hindi)
print("french",result_french)
print("arbic",result_arabic)
print("russian",result_russian)
