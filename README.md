# degenerator
It's less than a generator

It's a simple app to generate some random stuff.

Flow:
1. get random fun fact
2. generate text with gpt upon the fact
3. get two random pictures
4. get style transfer between those pictures
5. show text + pic

# How to run:

1. Put [this files](https://huggingface.co/gpt2/tree/main) to `/models/`
2. Get your own token from your profile [here](https://deepai.org/) and put it in `/token.txt`
    - You can log in with google account.
    - 5$ free limit (10 requests - 1 cent)
3. Install docker 
4. Run app  
    `sudo docker build . -t degenerator:v1`  
    `sudo docker run -p 8000:8000 degenerator:v1`
5. Run streamlit ui  
    `cd ui/`  
    `pip install streamlit`  
    `streamlit run degenerator_ui.py`
6. Open `localhost:8501` in your browser  
    - be aware that single run can take up to 1-2 minutes
7. Generate, enjoy, degenerate!