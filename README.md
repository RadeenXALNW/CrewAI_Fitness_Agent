## Your Personal Fitness Agent :muscle: :leg:
at first import the repository
```
git clone --branch master https://github.com/RadeenXALNW/crewai_fitnessagent.git
```
change your directory to repo directory
```
cd crewai_fitnessagent
```
Then lock your poetry
```
poetry lock
```
Install all the necessary dependencies
```
poetry install
```

Next, we introduce another awesome tool Browserless a valuable tool that mimics a full-fledged browser environment. By using Browserless locally with Docker, you can simulate website functionalities seamlessly. If Docker isn’t installed yet, do so by following the installation instructions online as it is an essential developer tool.
So, when you have docker, run this:

```
docker run -d --rm --name browserless -p 3000:3000 browserless/chrome
```

***Make sure below two packages have these two versions.***

 - crewai  Version: 0.11.2
 - pydantic Version: 2.7.0
```
pip show crewai pydantic
```
Make sure to set your all environment variables and API keys. 
```
export variable_name=<api_key>
export model_name=<model_name>
```
Now run the main.py and play with it :shipit:
```
poetry run python main.py
```
>[!TIP]
>Make sure you have a stable internet connection.

>[!NOTE]
>Sometimes API fails to generate properly.

>[!CAUTION]
>Mixtral 8*7b sometimes can cause rate limit error. We,therefore set max request per minute parameter.


**Here is a sample of fitness plan after analyzing your diet and health parameters.**

![Fitness Plan for 30 days](https://github.com/RadeenXALNW/crewai_fitnessagent/assets/66905164/5b6a49f9-8a7a-4a67-aa5f-69a17133a2bf)
