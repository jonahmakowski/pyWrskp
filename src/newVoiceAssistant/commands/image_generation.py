import replicate
import dotenv
import os
import commands.webBrowser as webBrowser
import audio

dotenv.load_dotenv()
generation_token = os.getenv('REPLICATE_API_TOKEN')


def image_generation(prompt):
    output = replicate.run(
        "lucataco/open-dalle-v1.1:1c7d4c8dec39c7306df7794b28419078cb9d18b9213ab1c21fdc46a1deca0144",
        input={
            "width": 1024,
            "height": 1024,
            "prompt": prompt,
            "scheduler": "KarrasDPM",
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "apply_watermark": True,
            "negative_prompt": "worst quality, low quality",
            "prompt_strength": 0.8,
            "num_inference_steps": 60
        }
    )

    image_counter = 1
    for image in output:
        audio.speak('Here is image {}'.format(image_counter))
        webBrowser.open_webpage(image, https=False)
        image_counter += 1
