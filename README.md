# degenerator
It's less than a generator

It's a simple app to generate some random stuff based on GPT2 and deepai neural transfer style.

Flow:
1. get random fun fact
2. generate text with gpt upon the fact
3. get two random pictures
4. get style transfer between those pictures
5. show text + pic

# How to run:

1. Download model   
You can put [this files](https://huggingface.co/gpt2/tree/main) to `models/gpt2` manually or use the following commands:
```
git lfs install
git clone https://huggingface.co/gpt2 models/gpt2
```
2. Get your own token from your profile [here](https://deepai.org/) and put it in `/token.txt`    
    - You can log in with google account.
    - 5$ free limit (10 requests - 1 cent)
3. Install `docker` and `docker-compose`
4. Run app   
To run app use `sudo docker-compose up` command. It will build model and ui containers.
5. Open `localhost:8501` in your browser
    - be aware that single run can take up to 1-2 minutes
6. Generate, enjoy, degenerate!

NB:   
If you want to run model as REST api do the following:
- `sudo docker build . -t degenerator:v1`
- `sudo docker run -p 8000:8000 -v /path/to/models:/models/ degenerator:v1`  

Note that `/path/to/models` must be absolute.

# Authors
- Vasiliy Salikov
- Victor Tolmachev
- Mike Nenashev
