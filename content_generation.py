import os
from groq import Groq
from exa_py import Exa

class APIError(Exception):
    pass

class LearningScheduler:
    def __init__(self, exa_key, groq_key, prompt_file):
        self.exa = Exa(exa_key)
        self.groq_client = Groq(api_key=groq_key)
        self.prompt_template = self.load_prompt_template(prompt_file)

    def load_prompt_template(self, prompt_file):
        try:
            with open(prompt_file, 'r') as file:
                return file.read()
        except Exception as e:
            raise APIError(f"Error loading prompt template: {e}")

    def fetch_resources(self, topic):
        try:
            response = self.exa.search(topic, num_results=1)
            resources = []
            for item in response.results:
                resources.append({
                    "title": item.title,
                    "url": item.url,
                    "score": item.score,
                    "published_date": item.published_date,
                    "author": item.author
                })
            return resources
        except Exception as e:
            raise APIError(f"Error fetching resources for topic '{topic}': {e}")

    def generate_content(self, prompt, model='llama3-70b-8192'):
        try:
            response = self.groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model
            )
            return response.choices[0].message.content
        except Exception as e:
            raise APIError(f"Error generating content: {e}")

    def create_schedule(self, goal, duration, style):
        prompt = self.prompt_template.format(goal=goal, duration=duration, style=style)
        schedule = self.generate_content(prompt)
        return schedule

    def extract_topics(self, schedule):
        topics = []
        for line in schedule.split('\n'):
            if "Main topics to cover" in line or "Topic" in line:
                topic = line.split(":")[-1].strip()
                if topic:
                    topics.append(topic)
        return topics

    def append_resources(self, schedule, topics):
        all_resources = []
        for topic in topics:
            fetched_resources = self.fetch_resources(f"latest resources related to {topic}")
            if fetched_resources:
                for resource in fetched_resources:
                    all_resources.append(f"* {resource['url']}")
        
        motivation = 'Be brave enough to find the life you want and courageous enough to chase it. Then start over and love yourself the way you were always meant to!'
        schedule = f"{schedule}\n\n**Additional Resources**\n\n" + "\n".join(all_resources) + "\n\n" + motivation
        return schedule

    def create_learning_plan(self, goal, duration, style):
        try:
            schedule = self.create_schedule(goal, duration, style)
            topics = self.extract_topics(schedule)
            final_schedule = self.append_resources(schedule, topics)
            return final_schedule
        except Exception as e:
            raise APIError(f"Error creating learning plan: {e}")
