import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

def ask_gpt(prompt, questions, answers, x):
	
	
	pastContext = "Past Conversation:"
	for i in range(len(questions) ):
		pastContext = pastContext + "\nMe: " + questions[i]
		pastContext = pastContext = "\nYou: " + answers[i]
	
	if (int(x)==1):
		print("PAST CONTEXT:")
		print(pastContext)
		print("PROMPT")
		print(prompt)
		

	ans = openai.ChatCompletion.create(
    model="gpt-4",
    # messages=[
    #         {"role": "system", "content": "You are a genius scholar with strong, but extremely well informed opinions."},
    #         # {"role": "user", "content": "C reate a webpage's worth of Hacker news threads responding to a post about the TV show Black Mmirror. Make sure to include some contrarian opinions, personal anecdotes, and reference specific episodes."}
    #         {"role": "user", "content": """Write a 2,000 word paper on the following prompt:
    #         "In the 1940s, the work of Austrian economist F. A. Hayek and Austrian economic historian Karl Polanyi emerged out of the maelstrom of two world wars and attempted to address the question of whether or not capitalism was beneficial to society overall. (For Hayek, this question was linked to questions of individualism.) In your paper, describe the viewpoints of these two theorists on capitalism. How and why did they see capitalism as either supportive or destructive of social relations? On what did they base their opposing viewpoints? In your view, who offers the more and less persuasive arguments about capitalism and why?"
    #         """}
    # ])
    messages=[
            {"role": "system", "content": "You are a helpful assistant called Foo"},
            # {"role": "user", "content": "C reate a webpage's worth of Hacker news threads responding to a post about the TV show Black Mmirror. Make sure to include some contrarian opinions, personal anecdotes, and reference specific episodes."}
            {"role": "user", "content": prompt},
	        {"role": "assistant", "content": pastContext}

    ])
	return ans['choices'][0]['message']['content']

