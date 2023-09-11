# Medical_ChatBot
![image](https://img.shields.io/badge/-LangChain-32CD32?logo=LangChain&logoColor=white&style=for-the-badge)
![image](https://img.shields.io/badge/-llama2_7b-0467DF.svg?style=for-the-badge&logo=Meta&logoColor=white)
![image](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)

The app is a conversational interface allowing users to ask medical questions and receive answers from the Gale Encyclopedia of Medicine. Under the hood, the system uses the large language model LLama2-7b to understand the question and formulate an appropriate response. It searches through the Gale encyclopedia text to find the most relevant section to the user's query. This information is distilled into a natural language answer, with the source cited at the end. The interactive Streamlit interface creates a smooth conversation flow for diagnosing medical concerns. Users can ask follow-up questions and clarify specifics to get the necessary information. With the reliability of a medical reference book and the convenience of a chatbot, this app makes it easy to get answers to medical questions conversationally.

![Screenshot 2023-09-11 180312](https://github.com/AminHaghdadi/Medical_ChatBot/assets/87299853/f8fe39e2-672b-4552-ad4d-8b22e42018c6)
## Deployment

To deploy this project run

1:
```bash
  git clone https://github.com/AminHaghdadi/Medical_ChatBot.git
```
2: install requirements:
```bash
  pip install -r requirement.txt 
```
3:
Download the llama2-7b model from this link :
[Llama-2-7B](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin)

4:
Add model to llama2-7b folder

5: Run in Terminal
```bash
streamlit run main.py
```

## Reference Book
![91GcaWaZrXL](https://github.com/AminHaghdadi/Medical_ChatBot/assets/87299853/287ebadf-ee1a-4209-a4b2-1113aca28c51)
you can find this book in Data folder
