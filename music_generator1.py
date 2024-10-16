import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import io

def generate_music(prompt):
    # Mock function to simulate music generation
    # In a real scenario, this would call an API
    return f"Generated music based on: {prompt}"

def play_music():
    # Create a simple tone or load a sample audio file
    # Here, we'll create a simple sine wave tone
    tone = AudioSegment.sine(frequency=440, duration=1000)  # 1 second of A4 tone
    play(tone)

def main():
    st.title("AI Music Generator")

    prompt = st.text_input("Enter a description for the music:")

    if st.button("Generate Music"):
        if prompt:
            with st.spinner("Generating music..."):
                try:
                    music_description = generate_music(prompt)
                    st.success(music_description)
                    if st.button("Play Music"):
                        play_music()
                except Exception as e:
                    st.error(f"Error generating music: {e}")
        else:
            st.warning("Please enter a description.")

if __name__ == "__main__":
    main()