import dotenv
import os
import replicate
import helpers

dotenv.load_dotenv()
llama_token = os.getenv('REPLICATE_API_TOKEN')


def llama_result(prompt):
    result = ''
    for event in replicate.stream(
            "meta/meta-llama-3-70b-instruct",
            input={
                "top_k": 50,
                "top_p": 0.9,
                "prompt": prompt,
                "max_tokens": 512,
                "min_tokens": 0,
                "temperature": 0.6,
                "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are an assistant that is running on someone's computer. You have the ability to open an app if you say \"APP\" followed by the app's name. You have the ability to open a file if you say \"FILE\" followed by the filename. You have the ability to play music if you say \"PLAY\". You have the ability to pause music if you say \"PAUSE\". You have the ability to open a website if you say \"WEBSITE\" followed by the url (without the https:// part). You have the ability to google something if you say \"GOOGLE\" followed by what to google. You have the ability to generate iamges by saying \"IMAGE\" followed by the prompt. The prompt should be a summary of what is asked for. Nothing should be added other than a few descriptors added to enchance the image. Any command should be between $s. You HAVE TO say something other than just a command. You should not use a $ unless it is for a command. Your name is " + helpers.get_details()[2] + ", the user is called " + helpers.get_details()[0] + ".<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
                "presence_penalty": 1.15,
                "frequency_penalty": 0.2
            },
    ):
        result += str(event)

    return result
