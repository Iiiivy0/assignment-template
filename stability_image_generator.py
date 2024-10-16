import streamlit as st
import requests

# Set your Stability AI API key
api_key = 'sk-VtlcWP76OU8OqFCvfYaJ3vlPIXjr2i5GKC6597k4HGRLydWe'

def generate_image(prompt):
    url = "https://api.stability.ai/v1/generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "width": 512,
        "height": 512,
        "samples": 1
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    image_url = response.json()['artifacts'][0]['url']
    return image_url

def main():
    st.title("AI Image Generator")

    prompt = st.text_input("Enter a description for the image:")

    if st.button("Generate Image"):
        if prompt:
            with st.spinner("Generating image..."):
                try:
                    image_url = generate_image(prompt)
                    st.image(image_url, caption='Generated Image', use_column_width=True)
                except Exception as e:
                    st.error(f"Error generating image: {e}")
        else:
            st.warning("Please enter a description.")

if __name__ == "__main__":
    main()